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
- `wiki/papers/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing.md` 요약 페이지를 `draft`·`high` 신뢰도로 생성했다.
- 기존 위키 페이지는 직접 수정하지 않았으며, 개념·주제·방법·아이디어 연결은 `wiki/proposals.md`의 P-001–P-004로 제안했다.
- `wiki/index.md`에 웹 자료를 등록하고, 처리 상태를 `wiki/.state/ingest-state.json`에 `processed`로 기록했다.

## [2026-08-01] ingest | 새 웹 자료 4개

- Nature Editorial, HRC 조립 DES 사례, MaaS simulation-based DT 아키텍처, 제조 DT 검증·타당화 SLR 원본 4개를 변경하지 않고 처리했다.
- 각 요약 페이지를 `draft`로 생성했다. Nature Editorial은 출처 신뢰도 `high`(편집적 종합이라는 근거 유형은 별도 표기), 나머지 peer-reviewed 연구 3개도 `high`로 평가했다.
- 기존 위키 페이지는 직접 수정하지 않았으며, 연결·갱신 제안 P-005–P-008을 `wiki/proposals.md`에 추가했다.
- `wiki/index.md`와 `wiki/.state/ingest-state.json`을 갱신했다. 감지 스크립트는 iCloud 인덱싱·쓰기 권한 문제로 자동 상태 저장이 실패할 수 있어 canonical 상태는 수동으로 기록했다.

## [2026-08-01] revise | 신뢰도와 용어 명확화

- Nature Editorial의 출처 신뢰도를 `high`로 조정하고, Editorial이라는 근거 유형과 원 연구 재확인 필요성을 명시했다.
- 검증과 타당화의 약어를 사용하지 않고, 검증(verification)과 타당화(validation)를 처음에 풀어 쓴 뒤 한국어 표현으로 통일했다.

## [2026-08-02] revise | 용어와 4R 설명 보강

- `ingest`를 원본에서 위키 요약·메타데이터·연결 제안으로 구조화하는 초기 처리 단계로 설명했다.
- 4R(Representation·Replication·Reality·Relational)의 단계별 의미와 capability 예시를 추가했다.
- Nature Editorial의 유형 설명을 “특정 주제의 주요 연구와 쟁점을 소개·해설하는 편집 글”로 구체화했다.

## [2026-08-02] apply | 승인된 제안 P-001–P-008 반영

- 혜영님의 명시적 승인에 따라 proposals.md의 pending 제안 P-001–P-008을 모두 승인하고 반영했다.
- concepts/, topics/, methods/, ideas/에 디지털트윈, 스마트 제조 지도, PLM, RAMI 4.0, 시뮬레이션 기반 최적화, 불확실성 정량화, surrogate model, 인간-로봇 협업, 이산사건 시뮬레이션, 상호운용성, 의사결정 지원, 모델 검증·타당화, 디지털트윈 성숙도, 신뢰할 수 있는 디지털트윈 페이지를 생성했다.
- 여러 제안이 같은 페이지를 대상으로 한 경우 기존 내용을 덮어쓰지 않고 통합했다. 특히 P-005는 Digital Twin, P-007은 Simulation-based Optimization과 Integrated Digital Twin Optimization Loop에 연결해 반영했다.
- P-004의 통합 최적화 루프는 확정된 사실이 아니라 혜영님의 연구 맥락에 맞춘 medium 신뢰도의 연구 아이디어 후보로 표시했다.
- 모든 새 페이지를 index.md에 등록하고, 원본 raw/는 변경하지 않았다.

## [2026-08-02] revise | 핵심 용어 영어 원문 병기

- RAMI 4.0의 “세 개의 축 (Three Axes)”과 대상·계층, 수명주기·가치 흐름, 층의 영어 원문을 병기했다.
- 통합 디지털트윈 최적화 루프의 1~6단계에 State Collection, State Synchronization, Prediction & What-if Analysis, Optimization, Review & Execution, Monitoring & Updating을 병기했다.
- 이후 위키 페이지에서도 핵심 기술·연구 용어를 처음 등장할 때 한국어(영어 원문)로 병기하도록 AGENTS.md와 wiki/AGENTS.md 규칙을 추가했다.

## [2026-08-02] revise | 자료 유형별 폴더 분류

- Web Clipper 수집 경로와 문서 유형을 분리하도록 운영 규칙을 보강했다. Web Clipper 원본은 계속 raw/web/에 보관한다.
- OUP 문헌 리뷰, ScienceDirect 연구 논문 2개, Taylor & Francis 체계적 문헌 리뷰를 wiki/papers/로 이동하고 자료 유형을 paper로 기록했다.
- Nature Computational Science Editorial은 학술지에 실렸지만 연구 논문이 아닌 편집 글이므로 wiki/web/에 유지했다.
- 인덱스와 관련 내부 링크를 새 폴더 기준으로 갱신하고, Web Clipper 템플릿에 capture_type과 document_type 필드를 추가했다.

## [2026-08-02] review | 오늘 작업한 페이지 상태 변경

- 오늘 생성한 15개 지식 페이지와 오늘 보강한 Nature·Taylor & Francis 웹 요약 2개의 frontmatter 상태를 draft에서 reviewed로 변경했다.
- AGENTS.md, wiki/AGENTS.md, index.md, proposals.md, log.md는 운영·기록 파일이므로 상태 변경 대상에서 제외했다.

## [2026-08-02] ingest | 기존 로컬 Vault의 연구 기초 노트 6개

- 기존 `/Users/Hyeyeong/Vault/`를 읽기 전용으로 점검하고, 수업·실습 전체가 아니라 연구와 직접 연결되는 6개 축만 선별했다.
- `SimPy`, `Queueing Theory`, `Poisson Process`, `Markov Chain`, `Probability Distribution`, `Convex Optimization`의 독립적인 HyeWiki 초안 페이지를 생성했다.
- 로컬 Vault 원본과 첨부파일은 수정·이동·복사하지 않았다. 각 페이지에 원본 경로와 원본 수정시각을 기록하고, 연구용으로 바로 쓰기 전 외부 문헌·데이터 재검증이 필요함을 명시했다.
- 페이지는 수업 노트 기반이므로 `draft`·`medium`으로 시작했다. 기존 reviewed 페이지에 역방향 연결을 추가하는 변경은 P-009–P-013으로 제안했다.
- 외부 학습 Vault의 수동 편입 규칙을 `wiki/AGENTS.md`에 추가하고, 변경 추적용 `wiki/.state/vault-import-state.json`을 기록했다.

## [2026-08-02] revise | 개념·방법론 페이지의 개인화 섹션 정리

- 개념·방법론 초안에서 반복적인 `혜영님의 연구와의 관련성` 섹션을 제거했다.
- 연구 연결은 관련 개념·방법론·주제에 대한 내부 링크와 내용상 필요한 중립적 적용 맥락으로 유지한다.
- `Markov Chain`의 상태 분류 용어는 영어 중심으로 정리하고, `Poisson Process`의 `Merging` 표기를 불필요한 한영 병기 없이 수정했다.
