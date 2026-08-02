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
  - "[[web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making]]"
  - "[[web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems]]"
  - "[[web/2026-08-01_nature.com_The increasing potential and challenges of digital twins - Nature Computational Science]]"
---

# Decision Support System

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

## 혜영님의 연구와의 관련성

최적화 연구에서 의사결정 지원 시스템을 명시하면 알고리즘 출력이 실제 연구자의 판단과 현장 운영으로 넘어가는 경계를 분석할 수 있다. 특히 여러 KPI를 동시에 고려할 때, 파레토 해와 설명 가능한 추천을 어떻게 제시할지가 중요한 연구 질문이 된다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[concepts/Interoperability|상호운용성]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[ideas/Integrated Digital Twin Optimization Loop|통합 디지털트윈 최적화 루프]]

## 근거 자료

- [[web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making]]
- [[web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems]]
- [[web/2026-08-01_nature.com_The increasing potential and challenges of digital twins - Nature Computational Science]]
