# 위키 작업 로그

이 파일은 위키의 시간순 변경 기록이다. 아래 형식으로 새 항목을 추가한다.

`## [YYYY-MM-DD] ingest | 원본 제목`
`## [YYYY-MM-DD] query | 질문 또는 분석 제목`
`## [YYYY-MM-DD] lint | 점검 제목`

## [2026-08-01] setup | 혜영의 연구 세컨드 브레인 초기화

- `raw/`, `wiki/`, `Output/` 구조와 위키 운영 규칙을 만들었다.
- 연구 지식 지도 인덱스를 초기화했다.

## [2026-08-01] setup | ingest 운영 방식 확정

- Web Clipper는 `raw/web/`에 원문만 저장하고, AI Interpreter와 별도 API는 사용하지 않는다.
- 새 자료 3개 또는 24시간 경과 시 대기열을 확인하며, `대기열 처리해줘` 요청이 있을 때만 Codex가 ingest한다.
- 신뢰도는 `high / medium / low`로 관리한다. `high`·`medium`은 제안, `low`는 요약만 생성한다.
- 변경 제안은 `wiki/proposals.md`에서 관리하고, 승인된 항목만 반영한다.
- 상태는 `wiki/.state/ingest-state.json`에 기록하며, 배치 후 로컬 Git 커밋을 만들고 push는 수동으로 한다.

## [2026-08-01] setup | ingest 대기 알림 watcher

- API를 호출하지 않는 `scripts/check_ingest_queue.py`와 macOS LaunchAgent 설정을 추가했다.
- iCloud 볼트의 백그라운드 디렉터리 접근 권한 제약으로 LaunchAgent는 현재 설치하지 않고 중지했다.
- 권한을 허용한 뒤 `tools/README.md`의 설치 절차를 실행하거나, 프로젝트 대화창에서 수동으로 대기열을 확인한다.

## [2026-08-01] ingest | Past, present, and future research of digital twin for smart manufacturing

- `raw/web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing.md`를 변경하지 않고 처리했다.
- `wiki/web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing.md` 요약 페이지를 `draft`·`high` 신뢰도로 생성했다.
- 기존 위키 페이지는 직접 수정하지 않았으며, 개념·주제·방법·아이디어 연결은 `wiki/proposals.md`의 P-001–P-004로 제안했다.
- `wiki/index.md`에 웹 자료를 등록하고, 처리 상태를 `wiki/.state/ingest-state.json`에 `processed`로 기록했다.

## [2026-08-01] ingest | 새 웹 자료 4개

- Nature Editorial, HRC 조립 DES 사례, MaaS simulation-based DT 아키텍처, 제조 DT V&V SLR 원본 4개를 변경하지 않고 처리했다.
- 각 요약 페이지를 `draft`로 생성했다. Nature Editorial은 `medium`, 나머지 peer-reviewed 연구 3개는 `high` 신뢰도로 평가했다.
- 기존 위키 페이지는 직접 수정하지 않았으며, 연결·갱신 제안 P-005–P-008을 `wiki/proposals.md`에 추가했다.
- `wiki/index.md`와 `wiki/.state/ingest-state.json`을 갱신했다. 감지 스크립트는 iCloud 인덱싱·쓰기 권한 문제로 자동 상태 저장이 실패할 수 있어 canonical 상태는 수동으로 기록했다.
