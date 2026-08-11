---
type: concept
title: "Uncertainty Quantification"
status: reviewed
confidence: high
confidence_reason: "Nature Editorial이 디지털트윈의 핵심 과제로 제시한 불확실성 정량화와, simulation-based DT 사례의 변동·결함·실시간 데이터 문제를 연결해 정리했다."
tags:
  - uncertainty-quantification
  - digital-twin
  - simulation
  - decision-making
sources:
  - "[[web/The increasing potential and challenges of digital twins (2024)]]"
  - "[[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]"
  - "[[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]]"
---

# Uncertainty Quantification

## 빠른 이해

- 불확실성 정량화(UQ)는 입력·매개변수·모델 구조·측정·미래 변동의 불확실성이 출력과 의사결정에 미치는 영향을 범위·분포·위험도로 표현한다.
- 평균 예측만 제시하는 것과 불확실성을 정량화하는 것은 다르다. 후자는 어떤 조건에서 결과가 달라지고 제약을 위반할 가능성이 있는지 보여준다.
- UQ는 분포 선택, 전파, 민감도 분석, 검증·타당화, 의사결정 기준을 하나의 흐름으로 연결해야 의미가 있다.

## 정의

불확실성 정량화는 입력 데이터, 모델 매개변수, 구조적 가정, 측정과 예측 오차에 포함된 불확실성이 모델 출력과 의사결정에 얼마나 영향을 주는지 수치 또는 범위로 표현하는 과정이다.

## 디지털트윈에서 불확실성이 생기는 곳

| 원천 | 제조 디지털트윈 예 |
| --- | --- |
| 측정 불확실성 | 센서 오차, 결측, 통신 지연 |
| 입력 변동 | 수요, 처리시간, 고장, 재공품, 작업자 행동 |
| 매개변수 불확실성 | 공정시간 분포, 설비 능력, 작업자별 수행 차이 |
| 모델 구조 불확실성 | 실제 공정의 상호작용을 단순화하거나 누락한 경우 |
| 미래·시나리오 불확실성 | 갑작스러운 결함, 주문 변경, 자원 중단 |

## 기본 절차

1. 어떤 의사결정에 영향을 주는 불확실성인지 식별한다.
2. 데이터 또는 전문가 판단으로 분포·범위·시나리오를 설정한다.
3. 시뮬레이션·예측 모델을 반복 실행해 출력 분포를 계산한다.
4. 목적함수, 제약 위반 확률, 예측 오차, 신뢰구간을 의사결정자에게 전달한다.
5. 민감도가 높은 입력과 모델 가정을 우선적으로 측정·검증한다.

## 최적화와의 연결

불확실성을 무시한 최적화는 평균 조건에서 좋아 보이지만 변동이 큰 현장에서 불안정할 수 있다. 연구에서는 기대 성능만이 아니라 최악 조건, 위험도, 제약 위반 확률, 계획의 재현성과 같은 기준을 함께 비교할 수 있다.

## 의사결정 결과로 변환하기

UQ의 결과는 분포나 구간으로 끝나지 않고 실행 규칙과 연결되어야 한다. 예를 들어 예측 구간이 넓으면 보수적 정책을 선택하거나, 제약 위반 확률이 임계값을 넘으면 고충실도 모델·추가 측정·사람 검토로 되돌리는 조건을 둘 수 있다.

서로 다른 불확실성을 한 숫자로 합치기 전에 원인을 분리한다. 데이터 측정오차, 매개변수 변동, 모델 구조 오차, 미래 사건은 완화 방법과 책임 주체가 다르다. 따라서 결과 표에는 출력 범위뿐 아니라 어떤 입력과 가정이 범위를 지배했는지 함께 기록한다.

## 주의점

- 불확실성 범위는 데이터와 가정에 의존하므로 숫자 자체보다 근거와 민감도를 함께 기록한다.
- 불확실성을 정량화했다고 해서 모델이 자동으로 타당해지는 것은 아니다.
- 사용 목적에 필요한 수준보다 과도하게 복잡한 확률 모델을 만들면 실시간 의사결정을 방해할 수 있다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[methods/Surrogate Modeling|surrogate model]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]
- [[ideas/Integrated Digital Twin Optimization Loop|통합 디지털트윈 최적화 루프]]

## 근거 자료

- [[web/The increasing potential and challenges of digital twins (2024)]]
- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]
- [[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]]
