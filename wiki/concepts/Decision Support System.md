---
type: concept
title: "Decision Support System"
status: reviewed
confidence: high
confidence_reason: "MaaS simulation-based DT 사례의 전략·운영 의사결정 흐름과 HRC 사례의 실시간 what-if 지원을 일반적인 의사결정 지원 시스템 개념으로 정리했다."
tags:
  - decision-support
  - digital-twin
  - simulation
  - optimization
sources:
  - "[[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]"
  - "[[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]"
  - "[[web/The increasing potential and challenges of digital twins (2024)]]"
---

# Decision Support System

## 빠른 이해

- **대상**: 데이터와 모델의 결과를 선택지와 실행 가능한 의사결정으로 바꾸는 시스템이다.
- **핵심 흐름**: 관측·예측 → 시나리오 생성 → 대안 평가 → 설명 가능한 추천 → 사람 또는 자동화 주체의 승인·실행 → 결과 기록이다.
- **경계**: 의사결정 지원은 추천을 제공하는 기능이며, 승인·책임·실행까지 자동화한다는 뜻은 아니다. 모델의 정확도뿐 아니라 추천이 사용 맥락에서 이해되고 추적되는지가 중요하다.

## 정의

의사결정 지원 시스템은 데이터, 모델, 시나리오 분석, 규칙 또는 최적화 결과를 사용해 사람이거나 자동화된 운영 주체가 선택지를 비교하고 행동을 결정하도록 돕는 시스템이다. 추천을 제공할 수 있지만, 모든 의사결정을 자동으로 수행해야 하는 것은 아니다.

## 디지털트윈과의 관계

디지털트윈은 현재 상태를 표현하고 미래 시나리오를 계산하는 기반이 되고, 의사결정 지원 시스템은 그 결과를 사용 목적과 제약조건에 맞는 선택지·권고·실행계획으로 바꾼다.

## 두 시간 규모의 의사결정

| 시간 규모 | 질문 | MaaS 사례의 예 |
| --- | --- | --- |
| 전략적 | 어떤 설비·기술·자원 구성이 장기 성능에 적합한가? | mobile programmable cobot 수와 생산계획 비교 |
| 운영적 | 현재 상태와 주문을 기준으로 다음 계획을 어떻게 조정할 것인가? | 재공품 snapshot과 결함 정보를 반영한 작업순서 재계산 |

## 기본 흐름

1. 현재 상태와 요구사항을 수집한다.
2. 시뮬레이션·예측·최적화로 후보를 생성한다.
3. KPI, 비용, 위험, 불확실성, 제약 위반을 비교한다.
4. 추천 이유와 근거를 사용자에게 보여준다.
5. 사람 승인 또는 자동화 정책에 따라 실행계획을 전달한다.
6. 결과를 관찰해 다음 판단의 근거로 축적한다.

## 설계 질문

- 추천의 대상이 작업순서·자원배치·공정조건 중 무엇인가?
- 최적화 목적과 운영 제약을 사용자가 이해하고 수정할 수 있는가?
- 계획이 모델의 불확실성과 예상 오차를 함께 표시하는가?
- 자동 실행 전에 사람이 개입하거나 중지할 수 있는가?
- 추천과 실제 결과 사이의 차이가 추적 가능하게 기록되는가?

## 적용 맥락과 분석 관점

의사결정 지원 시스템의 품질은 추천값 하나가 아니라 전체 의사결정 사슬로 평가한다. 입력 상태가 최신인지, 후보 생성 과정이 재현 가능한지, 목적함수와 제약조건이 사용자에게 설명 가능한지, 추천이 실행 가능한 형식으로 전달되는지를 각각 분리해 기록한다.

복수 KPI가 충돌하면 단일 점수로 합치는 과정에서 선호와 단위가 숨겨질 수 있다. 가중합을 사용한다면 가중치의 근거와 민감도를, Pareto 해를 제시한다면 지배관계·선택 기준·승인 주체를 함께 적는다. 추천 후에는 예측값과 실제 결과의 차이를 저장해 다음 모델 갱신과 재검토의 근거로 사용한다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[concepts/Interoperability|상호운용성]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[ideas/Integrated Digital Twin Optimization Loop|통합 디지털트윈 최적화 루프]]

## 근거 자료

- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]
- [[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]
- [[web/The increasing potential and challenges of digital twins (2024)]]
