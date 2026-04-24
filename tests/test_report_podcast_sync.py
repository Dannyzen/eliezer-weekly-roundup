from __future__ import annotations

import asyncio
import json
from pathlib import Path

from eliezer_weekly_roundup.report_podcast import (
    AudioArtifactRecord,
    NotebookRecord,
    ReportPodcastOptions,
    ReportPodcastService,
    SourceRecord,
    parse_report_document,
    upsert_managed_audio_section,
)


class FakeNotebookGateway:
    def __init__(self) -> None:
        self.ensure_notebook_calls: list[tuple[str, str | None]] = []
        self.replace_report_source_calls: list[tuple[str, str, str]] = []
        self.ensure_url_sources_calls: list[tuple[str, tuple[str, ...]]] = []
        self.generate_audio_calls: list[dict[str, object]] = []
        self.notebook = NotebookRecord(
            id="nb-123", title="NotebookLM: Daily Scan: 2026-04-21"
        )

    async def ensure_notebook(
        self, title: str, preferred_notebook_id: str | None = None
    ) -> NotebookRecord:
        self.ensure_notebook_calls.append((title, preferred_notebook_id))
        return self.notebook

    async def replace_report_source(
        self, notebook_id: str, source_title: str, content: str
    ) -> SourceRecord:
        self.replace_report_source_calls.append((notebook_id, source_title, content))
        return SourceRecord(id="src-report", key=source_title)

    async def ensure_url_sources(
        self, notebook_id: str, urls: list[str]
    ) -> list[SourceRecord]:
        self.ensure_url_sources_calls.append((notebook_id, tuple(urls)))
        return [
            SourceRecord(id=f"src-url-{index}", key=url)
            for index, url in enumerate(urls, start=1)
        ]

    async def generate_audio_overview(
        self,
        notebook_id: str,
        output_path: Path,
        *,
        instructions: str | None,
        language: str,
        audio_format: str,
        audio_length: str,
        timeout_seconds: int,
    ) -> AudioArtifactRecord:
        self.generate_audio_calls.append(
            {
                "notebook_id": notebook_id,
                "output_path": output_path,
                "instructions": instructions,
                "language": language,
                "audio_format": audio_format,
                "audio_length": audio_length,
                "timeout_seconds": timeout_seconds,
            }
        )
        output_path.write_bytes(b"fake mp3 bytes")
        return AudioArtifactRecord(id="audio-123", path=output_path)


class FakeGitPublisher:
    def __init__(self) -> None:
        self.calls: list[dict[str, object]] = []

    def commit_and_push(
        self, *, repo_root: Path, paths: list[Path], message: str
    ) -> None:
        self.calls.append({"repo_root": repo_root, "paths": paths, "message": message})


def test_parse_report_document_skips_rss_feed_urls_that_notebooklm_rejects(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "roundups" / "2026-04-22.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        (
            "# Daily Scan: 2026-04-22\n\n"
            "Core source: https://openai.com/index/the-next-evolution-of-the-agents-sdk\n"
            "Feed source: https://openai.com/news/rss.xml\n"
            "Supporting source: https://github.com/openai/openai-agents-python\n"
        ),
        encoding="utf-8",
    )

    parsed = parse_report_document(report_path, repo_root=tmp_path)

    assert parsed.cited_urls == [
        "https://openai.com/index/the-next-evolution-of-the-agents-sdk",
        "https://github.com/openai/openai-agents-python",
    ]



def test_parse_report_document_extracts_urls_and_ignores_managed_audio_block(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "roundups" / "2026-04-21.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        (
            "# Daily Scan: 2026-04-21\n\n"
            "Core source: https://example.com/alpha\n"
            "Supporting source: https://example.com/beta).\n\n"
            "<!-- eliezer-roundup:audio:start -->\n"
            "## Audio Overview\n"
            "- Podcast: [Listen](./2026-04-21.notebooklm.mp3)\n"
            "<!-- eliezer-roundup:audio:end -->\n"
        ),
        encoding="utf-8",
    )

    parsed = parse_report_document(report_path, repo_root=tmp_path)

    assert parsed.title == "Daily Scan: 2026-04-21"
    assert parsed.relative_path.as_posix() == "roundups/2026-04-21.md"
    assert parsed.audio_output_path == report_path.with_suffix(".notebooklm.mp3")
    assert parsed.cited_urls == [
        "https://example.com/alpha",
        "https://example.com/beta",
    ]
    assert "eliezer-roundup:audio:start" not in parsed.source_content
    assert "2026-04-21.notebooklm.mp3" not in parsed.source_content

    without_audio_block = report_path.with_name("2026-04-21-clean.md")
    without_audio_block.write_text(
        "# Daily Scan: 2026-04-21\n\nCore source: https://example.com/alpha\nSupporting source: https://example.com/beta).\n",
        encoding="utf-8",
    )
    reparsed = parse_report_document(without_audio_block, repo_root=tmp_path)
    assert reparsed.source_digest == parsed.source_digest


def test_upsert_managed_audio_section_replaces_existing_block() -> None:
    original = "# Report\n\nBody text.\n"
    first = upsert_managed_audio_section(
        original,
        audio_relative_path="2026-04-21.notebooklm.mp3",
        notebook_title="NotebookLM: Daily Scan: 2026-04-21",
        notebook_id="nb-123",
    )
    second = upsert_managed_audio_section(
        first,
        audio_relative_path="2026-04-21-v2.notebooklm.mp3",
        notebook_title="NotebookLM: Daily Scan: 2026-04-21",
        notebook_id="nb-123",
    )

    assert second.count("eliezer-roundup:audio:start") == 1
    assert "2026-04-21-v2.notebooklm.mp3" in second
    assert "2026-04-21.notebooklm.mp3" not in second


def test_service_creates_notebook_generates_audio_updates_markdown_manifest_and_pushes(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "roundups" / "2026-04-21.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        "# Daily Scan: 2026-04-21\n\nCore source: https://example.com/alpha\n",
        encoding="utf-8",
    )

    gateway = FakeNotebookGateway()
    git_publisher = FakeGitPublisher()
    service = ReportPodcastService(
        repo_root=tmp_path, gateway=gateway, git_publisher=git_publisher
    )

    result = asyncio.run(
        service.generate_podcast(
            report_path,
            ReportPodcastOptions(
                push=True, instructions="make it engaging", timeout_seconds=321
            ),
        )
    )

    assert result.generated_new_audio is True
    assert report_path.with_suffix(".notebooklm.mp3").exists()
    assert gateway.ensure_notebook_calls == [
        ("NotebookLM: Daily Scan: 2026-04-21", None)
    ]
    assert gateway.ensure_url_sources_calls == [
        ("nb-123", ("https://example.com/alpha",))
    ]
    assert gateway.generate_audio_calls[0]["instructions"] == "make it engaging"
    assert gateway.generate_audio_calls[0]["timeout_seconds"] == 321

    updated_markdown = report_path.read_text(encoding="utf-8")
    assert "## Audio Overview" in updated_markdown
    assert "2026-04-21.notebooklm.mp3" in updated_markdown
    assert "nb-123" in updated_markdown

    manifest_path = tmp_path / ".notebooklm-sync.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    entry = manifest["reports"]["roundups/2026-04-21.md"]
    assert entry["notebook_id"] == "nb-123"
    assert entry["audio_artifact_id"] == "audio-123"
    assert entry["audio_path"] == "roundups/2026-04-21.notebooklm.mp3"

    assert len(git_publisher.calls) == 1
    pushed_paths = {
        path.relative_to(tmp_path).as_posix()
        for path in git_publisher.calls[0]["paths"]
    }
    assert pushed_paths == {
        ".notebooklm-sync.json",
        "roundups/2026-04-21.md",
        "roundups/2026-04-21.notebooklm.mp3",
    }


def test_service_reuses_existing_audio_when_source_digest_is_unchanged(
    tmp_path: Path,
) -> None:
    report_path = tmp_path / "roundups" / "2026-04-21.md"
    report_path.parent.mkdir(parents=True, exist_ok=True)
    report_path.write_text(
        "# Daily Scan: 2026-04-21\n\nhttps://example.com/alpha\n", encoding="utf-8"
    )

    parsed = parse_report_document(report_path, repo_root=tmp_path)
    audio_path = report_path.with_suffix(".notebooklm.mp3")
    audio_path.write_bytes(b"existing audio")
    manifest_path = tmp_path / ".notebooklm-sync.json"
    manifest_path.write_text(
        json.dumps(
            {
                "reports": {
                    parsed.relative_path.as_posix(): {
                        "report_path": parsed.relative_path.as_posix(),
                        "notebook_id": "nb-123",
                        "notebook_title": "NotebookLM: Daily Scan: 2026-04-21",
                        "source_digest": parsed.source_digest,
                        "report_source_id": "src-report",
                        "url_source_ids": ["src-url-1"],
                        "audio_artifact_id": "audio-123",
                        "audio_path": parsed.audio_relative_path.as_posix(),
                    }
                }
            },
            indent=2,
        ),
        encoding="utf-8",
    )

    gateway = FakeNotebookGateway()
    git_publisher = FakeGitPublisher()
    service = ReportPodcastService(
        repo_root=tmp_path, gateway=gateway, git_publisher=git_publisher
    )

    result = asyncio.run(
        service.generate_podcast(report_path, ReportPodcastOptions(push=False))
    )

    assert result.generated_new_audio is False
    assert gateway.replace_report_source_calls == []
    assert gateway.generate_audio_calls == []
    assert "2026-04-21.notebooklm.mp3" in report_path.read_text(encoding="utf-8")
    assert git_publisher.calls == []
