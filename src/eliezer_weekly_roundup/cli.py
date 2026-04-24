from __future__ import annotations

import argparse
import asyncio
import subprocess
import sys
from pathlib import Path

from .report_podcast import (
    NotebookLMGatewayAdapter,
    ReportPodcastOptions,
    ReportPodcastService,
)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="eliezer-roundup",
        description="Create NotebookLM notebooks and podcasts for roundup reports.",
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    generate = subparsers.add_parser(
        "generate-podcast",
        help="Create or reuse a NotebookLM notebook for a report and generate its podcast.",
    )
    generate.add_argument("report_path", type=Path)
    generate.add_argument(
        "--push", action="store_true", help="Commit and push changed assets to GitHub."
    )
    generate.add_argument(
        "--instructions", help="Optional NotebookLM audio instructions."
    )
    generate.add_argument(
        "--language", default="en", help="NotebookLM audio language code."
    )
    generate.add_argument(
        "--audio-format",
        default="deep-dive",
        choices=["deep-dive", "brief", "critique", "debate"],
        help="NotebookLM audio overview format.",
    )
    generate.add_argument(
        "--audio-length",
        default="medium",
        choices=["short", "medium", "long"],
        help="NotebookLM audio overview length.",
    )
    generate.add_argument(
        "--timeout-seconds",
        default=900,
        type=int,
        help="Maximum time to wait for audio generation.",
    )
    generate.add_argument(
        "--storage",
        help="Optional path to notebooklm storage_state.json. Defaults to notebooklm-py discovery.",
    )
    return parser


def discover_repo_root(report_path: Path) -> Path:
    resolved = report_path.resolve()
    result = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=resolved.parent,
        check=True,
        capture_output=True,
        text=True,
    )
    return Path(result.stdout.strip()).resolve()


async def _run_generate_podcast(args: argparse.Namespace) -> int:
    repo_root = discover_repo_root(args.report_path)
    gateway = NotebookLMGatewayAdapter(storage_path=args.storage)
    service = ReportPodcastService(repo_root=repo_root, gateway=gateway)
    result = await service.generate_podcast(
        args.report_path,
        ReportPodcastOptions(
            push=args.push,
            instructions=args.instructions,
            language=args.language,
            audio_format=args.audio_format,
            audio_length=args.audio_length,
            timeout_seconds=args.timeout_seconds,
        ),
    )
    status = "generated" if result.generated_new_audio else "reused"
    print(f"Notebook {result.notebook_id}. Podcast {status} at {result.audio_path}.")
    return 0


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    if args.command == "generate-podcast":
        try:
            return asyncio.run(_run_generate_podcast(args))
        except FileNotFoundError as error:
            print(
                "NotebookLM authentication is missing. Run `uv run notebooklm login` first, "
                "or pass `--storage /path/to/storage_state.json`.\n"
                f"Original error: {error}",
                file=sys.stderr,
            )
            return 1
    parser.error(f"Unknown command: {args.command}")
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
