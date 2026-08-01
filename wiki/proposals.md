# 위키 변경 제안함

AI가 기존 위키 페이지에 연결·갱신을 제안하는 단일 검토함이다. `reviewed`·`stable` 페이지는 이 파일에서 승인하기 전까지 직접 수정하지 않는다.

## 사용 규칙

- 제안 상태: `pending`, `approved`, `rejected`, `deferred`
- `high`와 `medium` 자료에서 나온 제안만 기록한다.
- 각 제안에는 원본, 대상 페이지, 제안 내용, 근거, 신뢰도를 포함한다.
- `승인된 제안 반영해줘`라는 명시적 요청이 있을 때 `approved` 항목만 반영한다.
- 반영 또는 거부가 끝난 항목은 필요할 때 `wiki/log.md`로 요약하고 이 파일에서 정리한다.

<!-- 새 제안은 아래에 추가한다. -->

## [2026-08-01] ingest | Past, present, and future research of digital twin for smart manufacturing

### P-001 | Digital Twin 개념 페이지 생성

- 상태: `pending`
- 대상: `wiki/concepts/Digital Twin.md`
- 제안: 물리 공간·사이버 공간·데이터/정보 연결을 DT의 최소 구성으로 정리하고, 단순 가상 시뮬레이션과 구분한다.
- 근거: 원문 2.1절의 DT 정의와 세 요소 설명.
- 출처: `wiki/web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing.md`
- 신뢰도: `high`

### P-002 | 스마트 제조 DT 주제 지도 생성

- 상태: `pending`
- 대상: `wiki/topics/Digital Twin in Smart Manufacturing.md`
- 제안: PLM 단계 × RAMI 4.0 hierarchy × DT 기능(prototyping, pilot testing, monitoring, improvement, control)의 3축 지도를 만들고 관련 문헌을 연결한다.
- 근거: 91편 문헌의 분류 틀과 결론.
- 출처: `wiki/web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing.md`
- 신뢰도: `high`

### P-003 | PLM·RAMI 4.0 연결 개념 보강

- 상태: `pending`
- 대상: `wiki/concepts/Product Lifecycle Management.md`, `wiki/concepts/RAMI 4.0.md`
- 제안: 각각의 정의와 DT 적용 위치를 만들고, 주제 지도에서 PLM의 lifecycle/value stream과 RAMI 4.0의 hierarchy level이 어떻게 교차하는지 연결한다.
- 근거: 원문 2.2절 및 3절의 적용 축 설명.
- 출처: `wiki/web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing.md`
- 신뢰도: `high`

### P-004 | 시뮬레이션 기반 최적화 연결 및 연구 아이디어 검토

- 상태: `pending`
- 대상: `wiki/methods/Simulation-based Optimization.md`, `wiki/ideas/Integrated Digital Twin Optimization Loop.md`
- 제안: 레이아웃·스케줄링·자원 배분·공정 파라미터 사례를 시뮬레이션 기반 최적화 관점에서 비교하고, “실시간 데이터 → DT 시뮬레이션 → 최적화/의사결정 → 물리 시스템 되먹임” 루프를 별도 연구 아이디어 후보로 검토한다.
- 근거: 원문 4장 사례와 5장 통합 아키텍처 제안. 위 루프를 일반화하는 표현은 혜영님의 연구 맥락에 맞춘 해석이므로 관련 근거를 추가 확인해야 한다.
- 출처: `wiki/web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing.md`
- 신뢰도: `medium` (원문 근거는 높지만, 연구 아이디어로의 확장은 해석임)

## [2026-08-01] ingest | The increasing potential and challenges of digital twins

### P-005 | DT 성숙도·계산비용·신뢰성 축 보강

- 상태: `pending`
- 대상: `wiki/concepts/Digital Twin.md`, `wiki/concepts/Uncertainty Quantification.md`, `wiki/methods/Surrogate Modeling.md`
- 제안: fit-for-purpose 설계, 모델 복잡도와 비용·정확도 trade-off, surrogate model, 검증·타당화·불확실성 정량화·표준·human-in-the-loop를 기존 DT 개념과 연결한다.
- 근거: Nature Editorial이 Focus와 여러 Perspective·Comment에서 종합한 공통 과제.
- 출처: `wiki/web/2026-08-01_nature.com_The increasing potential and challenges of digital twins - Nature Computational Science.md`
- 신뢰도: `high` (출처 신뢰도는 높지만, Editorial 종합 내용의 세부 주장은 원 연구에서 재확인)

## [2026-08-01] ingest | Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems

### P-006 | HRC 조립 DT 사례와 DES·상호운용성 연결

- 상태: `pending`
- 대상: `wiki/topics/Human-Robot Collaboration in Manufacturing.md`, `wiki/methods/Discrete-Event Simulation.md`, `wiki/concepts/Interoperability.md`
- 제안: Digital Model(DES·RTVS)–Digital Mirror(IVRE)–orchestrator 구조, FIWARE/FIROS 데이터 교환, task allocation·ergonomics KPI를 사례 지도에 추가한다.
- 근거: FELICE 자동차 조립라인 case study와 workstation workflow 비교.
- 출처: `wiki/web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems.md`
- 신뢰도: `high`

## [2026-08-01] ingest | Transitioning trends into action: A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making

### P-007 | 통합 DT 최적화 루프와 의사결정 아키텍처 보강

- 상태: `pending`
- 대상: `wiki/methods/Simulation-based Optimization.md`, `wiki/concepts/Decision Support System.md`, `wiki/ideas/Integrated Digital Twin Optimization Loop.md`
- 제안: IoT platform–APM–MES–FlexSim–OptQuest–현장 실행의 데이터 흐름을 정리하고, 전략적 설비 결정과 운영적 schedule 재계산을 하나의 DT 최적화 루프로 연결한다.
- 근거: dynamic job-shop MaaS 산업 실험, WIP 기반 시뮬레이션, makespan 최적화.
- 출처: `wiki/web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making.md`
- 신뢰도: `high`

## [2026-08-01] ingest | Verification and validation of digital twins: a systematic literature review for manufacturing applications

### P-008 | 신뢰할 수 있는 DT의 검증·타당화·4R 주제 지도 생성

- 상태: `pending`
- 대상: `wiki/concepts/Model Verification and Validation.md`, `wiki/concepts/Digital Twin Maturity.md`, `wiki/topics/Trusted Digital Twin.md`
- 제안: 구현 검증과 사용 맥락 타당화의 목적을 분리하고, 4R(Representation·Replication·Reality·Relational) capability와 요구사항·context of use·trust metric을 연결한다.
- 근거: 157편 SLR의 4R 분류와 검증·타당화 현황(양쪽 모두 보고 24%, Relational 0%).
- 출처: `wiki/web/2026-08-01_tandfonline.com_Verification and validation of digital twins a systematic literature review for manufacturing applications.md`
- 신뢰도: `high`
