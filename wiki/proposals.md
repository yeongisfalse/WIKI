# 위키 변경 제안함

AI가 기존 위키 페이지에 연결·갱신을 제안하고, 혜영님의 명시적 승인을 거쳐 반영하는 검토함이다.

## 사용 규칙

- 새 제안은 pending 상태로 기록한다.
- 혜영님이 명시적으로 승인한 제안만 위키에 반영한다.
- 기존 reviewed·stable 페이지는 승인 전 직접 수정하지 않는다.
- 반영이 끝난 제안은 아래 처리 완료 기록과 wiki/log.md에 남긴다.
- low 신뢰도 자료는 연결 제안을 만들지 않고 요약만 만든다.

## 처리 완료

### P-001 | Digital Twin 개념 페이지 생성

- 상태: approved
- 반영 대상: wiki/concepts/Digital Twin.md
- 반영 내용: 물리 객체·디지털 객체·데이터 연결을 최소 구성으로 정리하고, 독립 가상 시뮬레이션과 구분했다.
- 근거: 스마트 제조 디지털트윈 문헌 연구의 정의와 구성 요소.

### P-002 | 스마트 제조 DT 주제 지도 생성

- 상태: approved
- 반영 대상: wiki/topics/Digital Twin in Smart Manufacturing.md
- 반영 내용: 제품 수명주기 관리 × RAMI 4.0 계층 × 디지털트윈 기능의 세 축과 후속 사례를 연결했다.
- 근거: 91편 문헌의 적용 축과 기능 분류.

### P-003 | PLM·RAMI 4.0 연결 개념 보강

- 상태: approved
- 반영 대상: wiki/concepts/Product Lifecycle Management.md, wiki/concepts/RAMI 4.0.md
- 반영 내용: 수명주기 단계, RAMI 4.0의 세 축과 제조 계층, 디지털트윈 적용 좌표를 정리했다.
- 근거: 원문 2.2절과 RAMI 4.0 적용 축 설명.

### P-004 | 시뮬레이션 기반 최적화 연결 및 연구 아이디어

- 상태: approved
- 반영 대상: wiki/methods/Simulation-based Optimization.md, wiki/ideas/Integrated Digital Twin Optimization Loop.md
- 반영 내용: 시뮬레이션 기반 최적화 루프와 실시간 데이터 → 시뮬레이션 → 최적화 → 실행계획 → 결과 갱신 구조를 연구 아이디어 후보로 정리했다.
- 근거: 스마트 제조 문헌 연구와 MaaS simulation-based DT 사례.
- 주의: 연구 아이디어로의 확장은 혜영님의 연구 맥락에 맞춘 해석이며 confidence는 medium으로 표시했다.

### P-005 | DT 성숙도·계산비용·신뢰성 축 보강

- 상태: approved
- 반영 대상: wiki/concepts/Digital Twin.md, wiki/concepts/Uncertainty Quantification.md, wiki/methods/Surrogate Modeling.md
- 반영 내용: fit-for-purpose, 계산 비용·정확도 절충, surrogate model, 불확실성, 검증·타당화, human-in-the-loop를 연결했다.
- 근거: Nature Editorial이 여러 Perspective·Comment에서 종합한 공통 과제.

### P-006 | HRC 조립 DT 사례와 DES·상호운용성 연결

- 상태: approved
- 반영 대상: wiki/topics/Human-Robot Collaboration in Manufacturing.md, wiki/methods/Discrete-Event Simulation.md, wiki/concepts/Interoperability.md
- 반영 내용: Digital Model·Digital Mirror·orchestrator, FIWARE/FIROS·NGSIv2, task allocation·ergonomics KPI를 정리했다.
- 근거: FELICE 자동차 조립라인 case study.

### P-007 | 통합 DT 최적화 루프와 의사결정 아키텍처 보강

- 상태: approved
- 반영 대상: wiki/methods/Simulation-based Optimization.md, wiki/concepts/Decision Support System.md, wiki/ideas/Integrated Digital Twin Optimization Loop.md
- 반영 내용: IoT platform·Advanced Plant Model·MES·FlexSim·OptQuest·현장 실행의 데이터 흐름과 전략·운영 의사결정을 연결했다.
- 근거: dynamic job-shop MaaS 산업 실험.

### P-008 | 신뢰할 수 있는 DT의 검증·타당화·4R 지도 생성

- 상태: approved
- 반영 대상: wiki/concepts/Model Verification and Validation.md, wiki/concepts/Digital Twin Maturity.md, wiki/topics/Trusted Digital Twin.md
- 반영 내용: 구현 검증과 사용 맥락 타당화를 분리하고, 4R capability, 요구사항, context of use, 불확실성, 상호운용성, 인간 책임을 연결했다.
- 근거: 157편 systematic literature review와 Nature Editorial.

## 현재 상태

- pending 제안: P-009–P-013
- 마지막 일괄 승인·반영일: 2026-08-02

## 대기 중 제안

### P-009 | 대기행렬 이론과 DES·최적화 연결

- 상태: pending
- 반영 대상: `wiki/methods/Discrete-Event Simulation.md`, `wiki/methods/Simulation-based Optimization.md`, `wiki/topics/Human-Robot Collaboration in Manufacturing.md`
- 제안 내용: `Queueing Theory`의 `ρ`, `L`, `W`, throughput, 변동성·병목 관점을 제조 DES와 후보 의사결정 KPI의 연결로 추가한다.
- 근거: `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Queuing Theory.md`에서 컴파일한 초안.
- 주의: 수식 적용 조건과 특정 사례의 일반화 범위를 재검토한 뒤 반영한다.

### P-010 | 포아송 과정·마르코프 체인과 확률 입력 연결

- 상태: pending
- 반영 대상: `wiki/methods/Discrete-Event Simulation.md`, `wiki/concepts/Uncertainty Quantification.md`
- 제안 내용: 사건 도착·설비 상태 전이의 확률모델 후보로 `Poisson Process`와 `Markov Chain`을 연결하고, 독립성·정상성·전이확률 가정 확인 항목을 추가한다.
- 근거: `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Poisson Process.md`, `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Discrete Time Markov Chain(DTMC).md`에서 컴파일한 초안.
- 주의: 실제 제조 데이터가 포아송·마르코프 가정을 만족한다고 단정하지 않는다.

### P-011 | SimPy와 이산사건 시뮬레이션 구현 연결

- 상태: pending
- 반영 대상: `wiki/methods/Discrete-Event Simulation.md`
- 제안 내용: `SimPy`를 DES 개념을 소규모 실행 모델로 검증하는 구현 도구로 연결하고, Resource·Container·Process·Event 대응표를 추가한다.
- 근거: 기존 로컬 Vault의 SimPy 입문·전기차 충전·주유소 실습 노트에서 컴파일한 초안.
- 주의: SimPy 버전과 API는 공식 문서로 재확인하고, 실습 코드를 연구 모델의 타당화 증거로 해석하지 않는다.

### P-012 | 볼록 최적화와 시뮬레이션 기반 최적화의 구조 비교

- 상태: pending
- 반영 대상: `wiki/methods/Simulation-based Optimization.md`, `wiki/methods/Surrogate Modeling.md`
- 제안 내용: 해석 가능한 볼록 구조와 확률·블랙박스·계산비용을 갖는 시뮬레이션 목적함수의 차이를 명시하고, 알고리즘 선택 전 문제 구조 확인 항목을 추가한다.
- 근거: `/Users/Hyeyeong/Vault/03_AI/04_Optimization/Math Foundation (1).md`에서 컴파일한 초안.
- 주의: `gradient`, KKT, 강한 쌍대성, 수치 안정성은 별도 검증·보강이 필요하다.

### P-013 | 확률분포와 불확실성 정량화 연결

- 상태: pending
- 반영 대상: `wiki/concepts/Uncertainty Quantification.md`, `wiki/methods/Discrete-Event Simulation.md`
- 제안 내용: PMF·PDF·CDF, 결합·조건부 분포, 독립성 가정을 시뮬레이션 입력과 불확실성 원천을 정의하는 기초로 연결한다.
- 근거: `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/Probability Distribution.md`에서 컴파일한 초안.
- 주의: 분포 선택은 원자료·적합도·꼬리·시간상관과 함께 검토해야 한다.
