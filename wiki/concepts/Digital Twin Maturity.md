---
type: concept
title: "Digital Twin Maturity"
status: reviewed
confidence: high
confidence_reason: "제조 디지털트윈 systematic literature review의 4R capability를 중심으로 만든 실무용 성숙도 관점이다. 4R은 해당 연구의 분류 틀이며 보편적·유일한 표준 성숙도 모델로 단정하지 않는다."
tags:
  - digital-twin
  - maturity
  - 4r-framework
  - verification
  - validation
sources:
  - "[[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]]"
  - "[[web/The increasing potential and challenges of digital twins (2024)]]"
---

# Digital Twin Maturity

## 4R capability 관점

4R은 디지털트윈이 어떤 기능 수준을 갖추었는지 분류하는 분석 틀이다. 반드시 모든 시스템이 선형으로 네 단계를 통과해야 한다는 표준은 아니다.

| capability | 구체적 의미 | 연구에서 확인할 증거 |
| --- | --- | --- |
| **Representation** | 물리 시스템을 디지털 공간에 표현하기 위한 기반. 실시간 데이터 수집, 저장·분석, 가상 표현을 포함한다. | 대상 식별자, 데이터 흐름, 상태 표현 |
| **Replication** | 실제 데이터를 이용해 물리 시스템의 출력이나 상태를 재현하는 디지털 복제물. | 물리·디지털 출력 비교, 오차 지표 |
| **Reality** | 복제에 더해 물리 시스템의 동작을 예측하고 what-if 시나리오를 비교하는 수준. | 미래 상태 예측, 시나리오 실험, 고급 시뮬레이션 |
| **Relational** | 디지털트윈이 고차원 문제 해결과 자율적 조정을 수행하는 수준. | 자율 의사결정, self-calibration, 양방향 데이터·행동 연결 |

## 성숙도를 평가할 때의 원칙

- 기능 수준보다 먼저 사용 목적과 필요한 capability를 정한다.
- Representation이 높아도 검증·타당화 증거가 부족하면 신뢰할 수 있는 운영 시스템이라고 단정하지 않는다.
- Reality 수준의 예측을 사용하려면 입력 변동과 모델 불확실성을 함께 평가한다.
- Relational 수준을 목표로 할 때는 자동 실행 권한, 안전 제약, 사람의 승인과 중지 조건을 명시한다.
- 데이터 품질, 상호운용성, 보안, 유지보수 능력도 성숙도의 별도 축으로 기록한다.

## 문헌 연구의 관찰

해당 systematic literature review는 선정된 157편에서 Representation 약 15%, Replication 26%, Reality 10%를 보고했고, Relational 수준은 보고하지 않았다. 이 비율은 선택된 문헌과 저자들의 분류에 대한 결과이며 모든 디지털트윈의 분포를 뜻하지 않는다.

## 혜영님의 연구에서 사용할 평가표

| 질문 | 기록할 내용 |
| --- | --- |
| 무엇을 표현하는가? | 제품·기계·공정·공장·물류와 경계 |
| 무엇과 동기화되는가? | 데이터 종류, 주기, 지연, 결측 |
| 무엇을 예측·비교하는가? | KPI, 시나리오, 시간 범위 |
| 어떤 행동을 추천·실행하는가? | 최적화 결과, 제약, 승인 지점 |
| 어떤 증거가 있는가? | 구현 검증, 사용 맥락 타당화, 운영 결과 |
| 무엇이 불확실한가? | 입력, 매개변수, 모델, 미래 상황 |

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[concepts/Interoperability|상호운용성]]
- [[topics/Trusted Digital Twin|신뢰할 수 있는 디지털트윈]]

## 근거 자료

- [[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]]
- [[web/The increasing potential and challenges of digital twins (2024)]]
