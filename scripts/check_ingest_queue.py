#!/usr/bin/env python3
"""Detect ingest-ready sources without calling an AI API."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import subprocess
from datetime import datetime, timedelta, timezone
from pathlib import Path


ROOT = Path(
    os.environ.get("LLM_WIKI_ROOT", str(Path(__file__).resolve().parents[1]))
).expanduser()
RAW_DIR = ROOT / "raw"
STATE_PATH = Path(
    os.environ.get(
        "LLM_WIKI_STATE", str(ROOT / "wiki" / ".state" / "ingest-state.json")
    )
).expanduser()
SOURCE_DIRS = ("web", "papers", "notes")
IGNORED_NAMES = {"AGENTS.md"}
QUEUE_THRESHOLD = 3
AGE_THRESHOLD = timedelta(hours=24)


def utc_now() -> datetime:
    return datetime.now(timezone.utc)


def iso(value: datetime) -> str:
    return value.replace(microsecond=0).isoformat().replace("+00:00", "Z")


def parse_iso(value: str | None) -> datetime | None:
    if not value:
        return None
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError:
        return None


def digest(path: Path) -> str:
    hasher = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            hasher.update(chunk)
    return hasher.hexdigest()


def discover_sources() -> list[Path]:
    sources: list[Path] = []
    for directory in SOURCE_DIRS:
        base = RAW_DIR / directory
        if not base.exists():
            continue
        if platform.system() == "Darwin":
            # iCloud File Provider directories can block os.scandir() from a
            # background LaunchAgent. Spotlight can enumerate them safely.
            result = subprocess.run(
                ["/usr/bin/mdfind", "-onlyin", str(base), 'kMDItemFSName != ""'],
                capture_output=True,
                text=True,
                check=False,
                timeout=20,
            )
            paths = (Path(line) for line in result.stdout.splitlines() if line)
        else:
            paths = base.rglob("*")
        for path in paths:
            if not path.is_file() or path.name in IGNORED_NAMES:
                continue
            if any(part.startswith(".") for part in path.relative_to(RAW_DIR).parts):
                continue
            sources.append(path)
    return sorted(sources)


def load_state() -> dict:
    if not STATE_PATH.exists():
        return {"version": 1, "sources": {}}
    with STATE_PATH.open(encoding="utf-8") as stream:
        state = json.load(stream)
    state.setdefault("version", 1)
    state.setdefault("sources", {})
    return state


def save_state(state: dict) -> None:
    STATE_PATH.parent.mkdir(parents=True, exist_ok=True)
    temporary = STATE_PATH.with_suffix(".tmp")
    with temporary.open("w", encoding="utf-8") as stream:
        json.dump(state, stream, ensure_ascii=False, indent=2)
        stream.write("\n")
    temporary.replace(STATE_PATH)


def apple_quote(value: str) -> str:
    return '"' + value.replace("\\", "\\\\").replace('"', '\\"') + '"'


def notify(count: int, reason: str) -> bool:
    message = f"{count}개 자료가 ingest 대기 중입니다 ({reason}). 프로젝트 대화창에서 '대기열 처리해줘'라고 말하세요."
    if platform.system() != "Darwin":
        print(message)
        return False
    script = (
        f"display notification {apple_quote(message)} "
        f"with title {apple_quote('LLM Wiki ingest 대기')} "
        f"sound name \"Glass\""
    )
    result = subprocess.run(["osascript", "-e", script], check=False)
    if result.returncode != 0:
        print(message)
        return False
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--no-notify", action="store_true", help="알림을 보내지 않고 상태만 갱신")
    parser.add_argument("--dry-run", action="store_true", help="상태 파일을 쓰지 않음")
    args = parser.parse_args()

    now = utc_now()
    state = load_state()
    sources = state["sources"]

    for path in discover_sources():
        relative = path.relative_to(ROOT).as_posix()
        current_hash = digest(path)
        record = sources.get(relative)
        if not record or record.get("content_hash") != current_hash:
            sources[relative] = {
                "content_hash": current_hash,
                "status": "queued",
                "first_seen": iso(now),
                "last_seen": iso(now),
                "last_error": None,
            }
        else:
            record["last_seen"] = iso(now)

    queued = [
        (relative, record)
        for relative, record in sources.items()
        if record.get("status") == "queued"
    ]
    queued.sort(key=lambda item: item[1].get("first_seen", ""))
    oldest = parse_iso(queued[0][1].get("first_seen")) if queued else None
    age_ready = oldest is not None and now - oldest >= AGE_THRESHOLD

    if len(queued) >= QUEUE_THRESHOLD:
        reason = f"새 자료 {len(queued)}개"
    elif age_ready:
        reason = "가장 오래된 자료가 24시간 경과"
    else:
        reason = None

    queue_signature = hashlib.sha256(
        "\n".join(f"{relative}:{record['content_hash']}" for relative, record in queued).encode()
    ).hexdigest()
    queue_info = state.setdefault("queue", {})
    queue_info.update(
        {
            "status": "ready" if reason else "waiting",
            "queued_count": len(queued),
            "oldest_queued": iso(oldest) if oldest else None,
            "last_checked": iso(now),
        }
    )

    if reason:
        last_notified = parse_iso(queue_info.get("last_notified_at"))
        same_queue = queue_info.get("last_notified_signature") == queue_signature
        remind_due = last_notified is None or now - last_notified >= AGE_THRESHOLD
        if not args.no_notify and (not same_queue or remind_due):
            notify(len(queued), reason)
            queue_info["last_notified_at"] = iso(now)
            queue_info["last_notified_signature"] = queue_signature

    if not args.dry_run:
        save_state(state)

    print(
        json.dumps(
            {
                "status": queue_info["status"],
                "queued_count": len(queued),
                "oldest_queued": queue_info["oldest_queued"],
                "reason": reason,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
