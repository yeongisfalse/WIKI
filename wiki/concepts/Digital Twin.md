---
type: concept
title: "Digital Twin"
status: reviewed
confidence: high
confidence_reason: "문헌 연구, Nature Editorial, simulation-based DT 사례와 검증·타당화 문헌을 통합한 개념 페이지다. 디지털트윈의 정확한 범위와 성숙도 기준은 적용 분야와 사용 목적에 따라 달라질 수 있다."
tags:
  - digital-twin
  - cyber-physical-system
  - simulation
  - decision-support
sources:
  - "[[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]"
  - "[[web/The increasing potential and challenges of digital twins (2024)]]"
  - "[[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]"
  - "[[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]"
---

# Digital Twin

## 빠른 이해

- 디지털트윈은 물리 대상의 상태를 디지털 모델로 표현하고, 양방향 또는 목적에 맞는 데이터 연결을 통해 관찰·예측·what-if 분석·의사결정을 지원한다.
- 단순 CAD, 정적 데이터베이스, 일회성 시뮬레이션은 데이터 동기화·사용 목적·운영 피드백이 없으면 디지털트윈의 전체 개념을 충족하지 않는다.
- 시스템 경계, 동기화 주기, 모델의 역할, 사용자의 승인 지점, 검증·타당화 증거를 명시해야 “무엇을 위한 디지털트윈인가”를 판단할 수 있다.

## 한 문장 정의

디지털트윈은 물리 시스템의 상태와 행동을 디지털 공간에서 표현하고, 물리 시스템과 디지털 모델 사이의 데이터 연결을 이용해 관찰·예측·what-if 분석·의사결정을 지원하는 시스템이다.

## 최소 구성과 경계

1. **물리 객체 또는 시스템**: 제품, 기계, 공정, 공장, 물류와 같은 실제 대상
2. **디지털 객체 또는 모델**: 실제 대상의 상태·구조·행동을 표현하는 모델
3. **데이터·정보 연결**: 물리 상태를 디지털 모델에 전달하고, 분석 또는 결정 결과를 실제 운영으로 되돌리는 연결

독립적으로 실행되는 가상 시뮬레이션은 물리 시스템과 운영 데이터가 연결되지 않는다면 디지털트윈과 동일하지 않다. 다만 시뮬레이션은 디지털트윈의 예측·what-if·최적화 기능을 구성하는 중요한 방법이 될 수 있다.

## 운영 루프

물리 시스템 상태 → 센서·운영 데이터 수집 → 디지털 모델 동기화 → 시뮬레이션·예측·최적화 → 의사결정 또는 실행계획 → 물리 시스템에 적용 → 결과 관찰과 모델 갱신

이 루프가 항상 완전히 자동화될 필요는 없다. 데이터 품질, 불확실성, 안전성, 책임 범위에 따라 사람이 결과를 검토하는 human-in-the-loop 구조가 적절할 수 있다.

## 사용 목적에 따른 기능

| 기능         | 질문                          | 제조 연구 예시                               |
| ---------- | --------------------------- | -------------------------------------- |
| 표현·모니터링    | 지금 시스템은 어떤 상태인가?            | 설비, 작업자, 공정, 재공품 상태의 실시간 표현            |
| 예측         | 앞으로 어떻게 될 것인가?              | 고장, 병목, 생산시간, 품질 변화 예측                 |
| what-if 분석 | 다른 선택을 하면 어떻게 되는가?          | 레이아웃, 작업 배치, 자원 수, 작업 순서 비교            |
| 최적화·의사결정   | 어떤 선택이 목적에 가장 적합한가?         | makespan, 생산성, 활용률, ergonomics를 고려한 계획 |
| 제어·되먹임     | 결정 결과를 실제 시스템에 어떻게 반영할 것인가? | 생산계획, 작업 할당, 공정 파라미터의 갱신               |

## 설계 원칙

- **Fit-for-purpose**: 물리 자산과 완전히 똑같은 복제품을 만들기보다, 필요한 의사결정과 성능 목표에 맞는 수준으로 설계한다.
- **계산 비용과 정확도의 절충**: 실시간 제약이 있으면 복잡한 시뮬레이션을 surrogate model 또는 적절한 단순화 모델과 조합할 수 있다.
- **검증과 타당화의 분리**: 모델이 요구사항대로 구현되었는지와 사용 맥락에서 실제를 충분히 대표하는지를 별도로 확인한다.
- **불확실성의 명시**: 입력 데이터, 모델 가정, 예측 결과의 불확실성을 숨기지 않고 의사결정에 함께 전달한다.
- **상호운용성**: 센서·설비·시뮬레이션·실행 시스템이 데이터를 교환하고 의미를 공유할 수 있어야 한다.

## 적용 맥락과 설계 질문

디지털트윈을 설계할 때는 다음 순서로 시스템 경계를 고정한다.

1. 어떤 물리 대상과 의사결정을 다루는지 정의한다.
2. 상태·이벤트·매개변수 중 무엇을 어떤 주기로 수집하는지 적는다.
3. 디지털 모델이 표현·예측·시나리오 평가·최적화 중 어떤 역할을 맡는지 구분한다.
4. 결과가 관찰 화면, 계획, 제어 중 어디로 전달되는지와 사람의 승인 지점을 정한다.
5. 모델·데이터·인터페이스가 변경될 때 필요한 재검증과 중지 조건을 기록한다.

이 순서를 생략하면 “실시간”, “지능형”, “자율” 같은 표현이 실제 capability와 증거보다 앞서게 된다. 반대로 사용 목적에 필요한 범위만 구현하면 고충실도 모델을 모든 기능에 강제하지 않고도 fit-for-purpose 디지털트윈을 설계할 수 있다.

## 연결

- [[concepts/Digital Twin Maturity|디지털트윈 성숙도]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[concepts/Interoperability|상호운용성]]
- [[ideas/Integrated Digital Twin Optimization Loop|통합 디지털트윈 최적화 루프]]

## 근거 자료

- [[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]
- [[web/The increasing potential and challenges of digital twins (2024)]]
- [[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]
- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]
