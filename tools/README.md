# ingest 대기 알림 watcher

`check_ingest_queue.py`는 AI API를 호출하지 않는다. 로컬 HyeWIKI Vault(`/Users/Hyeyeong/HyeWIKI`)의 `raw/web/`, `raw/papers/`, `raw/notes/`에 새 파일이 추가되었는지 확인하고, 새 자료가 3개 쌓이거나 가장 오래된 자료가 24시간이 지나면 macOS 알림을 보낸다. LaunchAgent는 실행 코드와 알림용 상태 캐시를 로컬 사용자 폴더에서 사용한다. 저장소의 `wiki/.state/ingest-state.json`은 실제 ingest 시 Codex가 갱신하는 canonical 상태다.

> 로컬 Vault에서도 watcher가 `running` 상태에서 진행하지 않으면 LaunchAgent를 중지하고, Python 실행 파일에 macOS 개인정보 보호 권한을 부여하거나 아래의 수동 확인 방식을 사용한다. AI API 호출은 어느 방식에서도 발생하지 않는다.

## 설치

터미널에서 다음을 실행한다.

```bash
mkdir -p "$HOME/Library/LaunchAgents"
mkdir -p "$HOME/Library/Application Support/LLM Wiki"
cp "scripts/check_ingest_queue.py" "$HOME/Library/Application Support/LLM Wiki/"
cp "tools/com.yeongisfalse.llm-wiki-queue.plist" "$HOME/Library/LaunchAgents/"
launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/com.yeongisfalse.llm-wiki-queue.plist"
```

이미 설치한 watcher를 갱신할 때는 먼저 다음을 실행한다.

```bash
launchctl bootout "gui/$(id -u)/com.yeongisfalse.llm-wiki-queue" 2>/dev/null || true
cp "scripts/check_ingest_queue.py" "$HOME/Library/Application Support/LLM Wiki/"
cp "tools/com.yeongisfalse.llm-wiki-queue.plist" "$HOME/Library/LaunchAgents/"
launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/com.yeongisfalse.llm-wiki-queue.plist"
```

## 확인

```bash
python3 scripts/check_ingest_queue.py --no-notify
```

알림은 대기열을 알려줄 뿐이며, 실제 AI ingest는 프로젝트 대화창에서 `대기열 처리해줘`라고 요청할 때 실행한다.
