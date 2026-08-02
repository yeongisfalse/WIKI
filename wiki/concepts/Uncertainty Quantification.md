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
  - "[[web/2026-08-01_nature.com_The increasing potential and challenges of digital twins - Nature Computational Science]]"
  - "[[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]"
  - "[[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]]"
---

# Uncertainty Quantification

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

## 혜영님의 연구와의 관련성

디지털트윈 최적화 결과를 실제 시스템에 전달하려면 “최적해가 무엇인가?”와 함께 “이 해가 입력 변동과 모델 오차에 얼마나 견디는가?”를 답해야 한다. 따라서 원본 데이터의 품질, 모델 검증·타당화, 예측 범위를 같은 메타데이터에 연결하는 것이 중요하다.

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

- [[web/2026-08-01_nature.com_The increasing potential and challenges of digital twins - Nature Computational Science]]
- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]
- [[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]]
