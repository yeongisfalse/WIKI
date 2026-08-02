# 연구 지식 지도 인덱스

이 파일은 위키의 콘텐츠 중심 진입점이다. 모든 위키 페이지를 한 줄 요약과 함께 등록한다. `proposals.md`와 `.state/`는 등록하지 않는다.

## 연구 주제

- [[topics/Digital Twin in Smart Manufacturing|스마트 제조 디지털트윈]] — 제품 수명주기·RAMI 4.0 계층·디지털트윈 기능을 교차해 연구 주제를 배치하는 지도.
- [[topics/Human-Robot Collaboration in Manufacturing|제조 인간-로봇 협업]] — 조립 시스템에서 작업 할당·생산성·ergonomics를 디지털트윈으로 함께 분석하는 주제.
- [[topics/Trusted Digital Twin|신뢰할 수 있는 디지털트윈]] — 표현·검증·타당화·불확실성·상호운용성·인간 책임을 신뢰성 축으로 정리한 지도.

## 핵심 개념

- [[concepts/Digital Twin|디지털트윈]] — 물리 시스템과 디지털 모델의 데이터 연결을 이용해 관찰·예측·최적화·의사결정을 지원하는 개념.
- [[concepts/Digital Twin Maturity|디지털트윈 성숙도]] — Representation·Replication·Reality·Relational capability와 검증 증거를 함께 보는 관점.
- [[concepts/Decision Support System|의사결정 지원 시스템]] — 데이터·모델·시나리오를 선택지와 실행계획으로 바꾸는 시스템.
- [[concepts/Interoperability|상호운용성]] — 이기종 장치와 모델이 데이터와 의미를 교환하고 함께 작동하는 능력.
- [[concepts/Model Verification and Validation|모델 검증과 타당화]] — 구현이 요구사항에 맞는지와 사용 맥락에서 실제를 대표하는지를 분리해 확인하는 방법.
- [[concepts/Product Lifecycle Management|제품 수명주기 관리]] — 제품 기획부터 설계·제조·사용·서비스·재활용까지의 정보 흐름을 관리하는 관점.
- [[concepts/RAMI 4.0|RAMI 4.0]] — 산업 4.0의 층·수명주기·계층을 세 축으로 배치하는 참조 아키텍처 모델.
- [[concepts/Uncertainty Quantification|불확실성 정량화]] — 데이터·모델·미래 변동이 예측과 의사결정에 미치는 영향을 범위와 확률로 표현하는 과정.

## 논문

- [[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]] — 스마트 제조 디지털트윈 문헌 91편을 제품 수명주기·RAMI 4.0·기능 축으로 분류한 문헌 연구.
- [[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]] — 이산사건 시뮬레이션과 Digital Mirror로 자동차 인간-로봇 협업 조립라인을 분석한 연구.
- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]] — IoT·Advanced Plant Model·FlexSim·OptQuest를 연결한 MaaS job-shop 디지털트윈 아키텍처 연구.
- [[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]] — 제조 디지털트윈 157편의 구현 검증·사용 맥락 타당화와 4R capability를 분석한 체계적 문헌 연구.

## 웹 자료

- [[web/The increasing potential and challenges of digital twins (2024)]] — 여러 분야의 DT 확장 가능성과 fit-for-purpose·검증·타당화·불확실성 정량화·human-in-the-loop 과제를 종합한 Nature Editorial.

## 방법론

- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]] — 도착·완료·고장 같은 사건 시점에 제조 시스템 상태를 갱신하는 시뮬레이션 방법.
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]] — 시뮬레이션으로 후보 의사결정과 불확실성을 반복 평가해 대안을 찾는 방법.
- [[methods/Surrogate Modeling|surrogate model]] — 계산 비용이 큰 모델을 빠르게 근사해 실시간 탐색과 최적화를 돕는 방법.
- [[methods/SimPy|SimPy]] — Python에서 프로세스·이벤트·공유 자원을 사용해 이산사건 시뮬레이션을 구현하는 도구.
- [[methods/Convex Optimization|볼록 최적화]] — 목적함수·제약의 볼록 구조, 미분·헤시안·쌍대성을 이용해 최적화 문제를 분석하는 방법론.
- [[methods/Newsvendor Model|Newsvendor Model]] — 불확실한 수요와 초과·부족 비용을 이용해 일기간 주문량과 `(S,s)` 정책을 결정하는 확률적 재고 모형.

## 확률·통계·확률과정 기초

- [[concepts/Probability Theory|확률론]] — 사건·조건부확률·베이즈 정리·확률변수·기댓값·분산을 묶은 공통 기반.
- [[concepts/Probability Distribution|확률분포]] — PMF·PDF·CDF와 결합·주변·조건부 분포를 통해 확률적 입력을 표현하는 기초 개념.
- [[concepts/Descriptive Statistics|기술통계]] — 측정척도·중심·산포·분위수·IQR·표준화를 통해 관측자료를 탐색하는 기초 개념.
- [[concepts/Statistical Inference|통계적 추론]] — 표본으로부터 모수·차이·가설을 추론하는 추정·신뢰구간·검정의 구조.
- [[concepts/Probability Inequalities|확률 부등식]] — 분포를 정확히 몰라도 평균·분산으로 확률의 상한·하한을 제한하는 도구.
- [[concepts/Stochastic Process|확률과정]] — 시간에 따른 확률변수들의 구조와 Poisson·Markov·Queueing 모델의 공통 틀.
- [[concepts/Poisson Process|포아송 과정]] — 시간에 따른 사건 도착을 계수하는 확률과정과 병합·thinning·비균일 확장을 정리한 개념.
- [[concepts/Queueing Theory|대기행렬 이론]] — 도착률·서비스율·부하·변동성이 대기시간·재공품·처리량에 미치는 영향을 분석하는 개념.
- [[concepts/Markov Chain|마르코프 체인]] — 현재 상태만으로 다음 상태를 표현하는 전이확률 기반 확률과정.

## 선형대수 기초

- [[concepts/Vector Spaces and Linear Transformations|벡터공간과 선형변환]] — 선형결합·span·독립·기저·차원, affine 해집합·feasible region과 kernel·range를 통합한 구조.
- [[concepts/Linear Systems and Matrix Rank|선형시스템과 행렬 rank]] — `Ax=b`, REF/RREF·rank·null space·행렬식 행 연산·가역성·최소제곱의 관계.
- [[concepts/Eigenvalues and Quadratic Forms|고유값과 이차형식]] — 고유방향·대각화·직교성·스펙트럼 정리와 Hessian·부호성·이차 최적화 조건의 연결.

## 연구 아이디어

- [[ideas/Integrated Digital Twin Optimization Loop|통합 디지털트윈 최적화 루프]] — 실시간 상태 동기화·시뮬레이션·최적화·실행·검증을 폐루프로 연결하는 연구 아이디어 후보.
