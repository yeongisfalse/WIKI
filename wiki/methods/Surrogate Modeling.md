---
type: method
title: "Surrogate Modeling"
status: reviewed
confidence: high
confidence_reason: "Nature Editorial이 소개한 Perspective의 surrogate model 정의와 실시간 디지털트윈·최적화의 계산 제약을 방법론 페이지로 정리했다. 특정 surrogate 알고리즘의 우월성을 주장하지 않는다."
tags:
  - surrogate-model
  - simulation
  - digital-twin
  - optimization
sources:
  - "[[web/The increasing potential and challenges of digital twins (2024)]]"
  - "[[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]"
---

# Surrogate Modeling

## 빠른 이해

- surrogate model은 비싼 원래 시뮬레이터의 입력–출력 관계를 근사해 탐색·예측·최적화의 평가시간을 줄인다.
- surrogate의 유효성은 평균 오차 하나가 아니라 관심 영역, 제약 경계, 꼬리 위험, 외삽 여부, 원모델과의 재검증 결과로 판단한다.
- 정확도와 속도의 절충은 사용 목적에 따라 달라진다. 후보를 빠르게 거르는 용도와 최종 실행을 승인하는 용도는 다른 증거 기준을 가져야 한다.

## 정의

Surrogate model은 계산 비용이 큰 시뮬레이션 또는 물리 모델의 입력–출력 관계를 근사하면서 더 빠르게 평가할 수 있는 대체 모델이다. 완전히 동일한 모델이 아니라, 사용 목적에 필요한 정확도와 계산시간을 맞추기 위한 절충이다.

## 디지털트윈에서의 역할

- 실시간 의사결정 주기 안에서 많은 후보를 빠르게 평가한다.
- 최적화 탐색 중 값비싼 시뮬레이션 호출 횟수를 줄인다.
- 설계·운영 시나리오를 넓게 탐색한 뒤 중요한 후보만 원래 시뮬레이션으로 재확인한다.

## 기본 흐름

1. 기준 시뮬레이션에서 입력·출력 실험 데이터를 만든다.
2. surrogate model을 학습하거나 적합한다.
3. 별도 검증 데이터로 근사 오차와 적용 범위를 평가한다.
4. 최적화 또는 what-if 탐색에 사용한다.
5. 선택된 후보를 고충실도 모델 또는 실제 시스템으로 다시 확인한다.
6. 새로운 관측값을 추가해 모델을 갱신한다.

## 반드시 기록할 것

| 항목 | 질문 |
| --- | --- |
| 적용 범위 | 어떤 입력 영역과 운영 조건에서만 신뢰할 수 있는가? |
| 오차 | 평균 오차뿐 아니라 최대 오차와 중요한 KPI의 오차는 얼마인가? |
| 불확실성 | 데이터가 부족한 영역에서 예측 신뢰도를 어떻게 표시하는가? |
| 갱신 | 실제 운영 데이터가 들어올 때 언제, 어떤 기준으로 재학습하는가? |
| 안전장치 | surrogate의 결과를 어떤 조건에서 원래 모델 또는 사람 검토로 되돌리는가? |

## 주의점

- 학습 범위를 벗어난 외삽은 특히 위험하다.
- 평균 예측이 정확해도 안전·품질·제약 경계에서 오차가 클 수 있다.
- 고충실도 모델과 실제 시스템의 차이를 surrogate의 성능으로 잘못 해석하지 않는다.

## 선택과 검증 기준

surrogate를 선택할 때는 정확도·계산시간·업데이트 비용·불확실성 표시 능력을 사용 목적과 함께 비교한다. 전역 탐색용 모델은 넓은 영역의 평균 성능이 중요할 수 있지만, 제약 경계나 안전 임계값 근처에서는 국소 최대 오차와 보수적 예측이 더 중요하다.

검증은 학습 데이터와 분리된 입력에서 수행하고, 원모델과 실제 시스템을 혼동하지 않는다. 후보가 선택된 뒤에는 원모델의 고충실도 재평가와 실제 관측 비교를 거쳐야 하며, 새로운 운영 데이터가 기존 학습 영역을 벗어나면 자동 외삽 대신 재학습·fallback·사람 검토 규칙을 적용한다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]

## 근거 자료

- [[web/The increasing potential and challenges of digital twins (2024)]]
- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]
