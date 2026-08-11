---
type: method
title: "Simulation-based Optimization"
status: reviewed
confidence: high
confidence_reason: "스마트 제조 문헌 연구와 두 simulation-based DT 사례에서 반복되는 시뮬레이션·what-if·최적화 연결을 방법론 관점으로 통합했다. 사례별 목적함수와 실험 조건은 일반화하지 않는다."
tags:
  - simulation-based-optimization
  - digital-twin
  - discrete-event-simulation
  - decision-support
sources:
  - "[[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]"
  - "[[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]"
  - "[[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]"
---

# Simulation-based Optimization

## 빠른 이해

- 시뮬레이션 기반 최적화(SBO)는 해석식으로 계산하기 어려운 시스템을 시뮬레이터로 평가하면서 결정변수의 좋은 조합을 탐색한다.
- 최적화기의 후보 생성, 시뮬레이터 실행, 성능·제약 집계, 난수·실험 설계, 탐색 종료가 하나의 반복 구조를 이룬다.
- 시뮬레이션 노이즈와 계산비용 때문에 최적화기의 성능만 비교할 수 없다. 반복 실행, common random numbers, surrogate, 조기 중단, 검증용 독립 시나리오가 함께 필요하다.

## 정의

시뮬레이션 기반 최적화는 복잡한 실제 시스템을 시뮬레이션 모델로 표현하고, 후보 의사결정과 매개변수를 반복해서 평가해 목적함수와 제약조건을 만족하는 대안을 찾는 방법이다. 해석식으로 계산하기 어려운 대기행렬, 작업 순서, 자원 상호작용, 불확실성을 모델 안에 포함할 수 있다는 점이 장점이다.

## 디지털트윈과의 운영 루프

1. 물리 시스템에서 상태·수요·결함·재공품 데이터를 수집한다.
2. 데이터로 시뮬레이션 모델의 초기 상태와 입력을 갱신한다.
3. 후보 정책 또는 설계안을 여러 시나리오로 실행한다.
4. 생산시간, 처리량, 활용률, 품질, 안전, ergonomics 등 지표를 비교한다.
5. 최적 또는 허용 가능한 계획을 사람이 검토하거나 실행 시스템에 전달한다.
6. 실제 결과를 다시 수집해 모델과 다음 의사결정을 갱신한다.

## MaaS 사례의 구체적 데이터 흐름

dynamic job-shop 사례에서는 다음 구성요소가 전략적·운영적 의사결정을 연결한다.

1. **IoT platform**이 센서와 현장 장치의 이벤트를 메시지 브로커로 수집한다.
2. **Advanced Plant Model(APM)**이 MES의 생산계획과 현장 자원·작업·재공품 상태를 실시간 표현한다.
3. **FlexSim** 이산사건 시뮬레이션이 현재 재공품 snapshot을 초기 상태로 불러와 후보 생산계획을 평가한다.
4. **OptQuest**가 작업 순서와 자원 배치를 탐색하고 sequence-dependent setup을 포함한 makespan을 줄이는 계획을 찾는다.
5. 승인된 생산계획을 JSON 메시지로 IoT platform을 거쳐 APM과 현장 실행 시스템에 전달한다.
6. 실행 중 수집된 상태·결함·지연 정보를 다음 재계산의 입력으로 되돌린다.

이 사례의 수치와 개선 결과는 특정 MaaS supplier, dynamic job-shop, 장비 구성과 실험 조건에 한정된다. 여기서 재사용할 수 있는 것은 구성요소 사이의 데이터·의사결정 흐름이지, 특정 도구 조합의 일반적 우월성이 아니다.

## 연구 사례

| 사례 | 결정변수·후보 | 주요 지표 또는 목적 |
| --- | --- | --- |
| 인간-로봇 협업 조립 | 작업 할당, macro·micro-operation workflow | 조립시간, 생산성, 활용률, 작업자 ergonomics |
| MaaS dynamic job-shop | 작업 순서, 자원 배치, mobile programmable cobot 수 | sequence-dependent setup을 포함한 makespan, 자원 활용률 |
| 스마트 제조 문헌 지도 | 레이아웃, 스케줄링, 자원 배분, 공정 파라미터 | 설계·제조 단계의 성능 개선과 제어 |

## 모델 설계 체크리스트

- 목적함수와 제약조건은 실제 의사결정 질문과 일치하는가?
- 초기 상태와 입력 데이터의 시점·품질·결측을 기록했는가?
- 확률변수와 모델 가정을 명시했는가?
- 시뮬레이션 결과의 반복 수, warm-up, 신뢰구간 또는 오차 기준을 기록했는가?
- 모델 구현 검증과 사용 맥락 타당화를 분리했는가?
- 계산시간이 의사결정 주기 안에 들어오는가? 필요하면 [[methods/Surrogate Modeling|surrogate model]]을 검토했는가?
- 실행 전에 안전·운영 제약과 사람의 승인 지점을 정의했는가?

## 한계와 주의

- 시뮬레이션이 실제 시스템을 잘못 표현하면 최적화 결과도 잘못된 방향으로 정교해질 수 있다.
- 특정 사례에서 보고된 개선률은 해당 시스템·입력·반복 조건에 한정된다.
- 목적함수가 여러 개이면 가중합, 파레토 해, 우선순위 규칙 등 의사결정자의 선호를 별도로 기록해야 한다.

## 실험 결과를 해석하는 순서

먼저 동일한 초기조건·입력·난수 정책에서 기준선과 후보 정책을 비교하고, 다음으로 여러 반복의 평균·분산·신뢰구간을 확인한다. 그 뒤 독립적인 검증 시나리오와 교란 조건에서 순위가 유지되는지 평가한다.

최적화기가 더 좋은 값을 찾았다는 사실과 정책이 실제 운영에 적합하다는 사실은 다르다. 실행 가능성, 데이터 지연, 안전·품질 제약, 재계획 빈도, 계산시간, 모델 오차를 함께 기록해야 한다. 최종 보고에는 선택된 정책뿐 아니라 탈락한 후보와 탈락 이유도 남기는 것이 재현성과 감사 가능성에 유리하다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]
- [[ideas/Integrated Digital Twin Optimization Loop|통합 디지털트윈 최적화 루프]]
- [[concepts/Decision Support System|의사결정 지원 시스템]]

## 근거 자료

- [[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]
- [[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]
- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]
