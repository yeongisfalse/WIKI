---
type: concept
title: "Model Verification and Validation"
status: reviewed
confidence: high
confidence_reason: "제조 디지털트윈 157편 systematic literature review의 정의·보고 현황·증거 유형을 중심으로 정리하고, Nature Editorial과 최적화 사례의 사용 맥락을 연결했다."
tags:
  - verification
  - validation
  - model-credibility
  - digital-twin
  - simulation
sources:
  - "[[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]]"
  - "[[web/The increasing potential and challenges of digital twins (2024)]]"
  - "[[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]"
---

# Model Verification and Validation

## 빠른 이해

- verification은 모델이 설계·코드·요구사항대로 구현되었는지를 묻고, validation은 그 모델이 정해진 사용 목적과 맥락에서 실제 시스템을 충분히 대표하는지를 묻는다.
- 두 검사는 서로 대체할 수 없다. 잘 구현된 모델도 현실을 잘못 추상화할 수 있고, 현실과 비슷해 보이는 모델도 코드 오류를 포함할 수 있다.
- 검증·타당화는 한 번의 정확도 수치가 아니라 요구사항 추적성, 단위·보존법칙 점검, 관측자료 비교, 민감도·불확실성 분석, 운영 후 재검토의 증거 묶음이다.

## 핵심 구분

### 구현 검증(verification)

구현 검증은 디지털트윈이 명세된 요구사항을 충족하고, 구현된 모델이 개념 모델과 설계 의도를 올바르게 반영하는지 확인하는 과정이다. 질문은 “모델을 올바르게 만들었는가?”에 가깝다.

### 사용 맥락 타당화(validation)

사용 맥락 타당화는 정해진 context of use에서 디지털트윈이 물리 시스템을 충분히 대표하고, 의도된 운영 목적을 달성하는지 증거를 제시하는 과정이다. 질문은 “목적에 맞는 모델을 만들었는가?”에 가깝다.

두 과정은 서로 대체할 수 없다. 구현이 요구사항대로 되었더라도 실제 사용 목적에 부적합할 수 있고, 실제 출력이 비슷해 보여도 구현 내부의 오류가 남아 있을 수 있다.

## 증거 예시

| 대상 | 확인 질문 | 가능한 증거 |
| --- | --- | --- |
| 구현 검증 | 상태·규칙·계산이 명세와 일치하는가? | 요구사항 추적, 단위·통합 시험, 보존법칙·논리 점검, 코드·모델 리뷰 |
| 사용 맥락 타당화 | 실제 시스템을 해당 목적에 충분히 대표하는가? | 물리·가상 출력 비교, KPI·오차 지표, 실제 사례 비교, 전문가 검토 |
| 운영 재검토 | 데이터·목적·시스템이 바뀌어도 계속 적합한가? | 기간별 재평가, drift 점검, 실행 결과와 예측 결과 비교 |

## 제조 디지털트윈 문헌의 관찰

해당 systematic literature review는 최종 157편을 분석했으며, 두 과정을 모두 수행했다고 보고한 연구는 24%, 구현 검증만 보고한 연구는 31%, 사용 맥락 타당화만 보고한 연구는 35%였다. 두 과정을 모두 보고한 연구 중 일부는 두 용어를 동의어처럼 사용했다. 이 수치는 선정된 문헌과 저자들의 분류 기준에 따른 결과이지 분야 전체의 절대 비율은 아니다.

## 디지털트윈 연구 체크리스트

1. 사용 목적과 context of use를 먼저 썼는가?
2. 모델의 요구사항·가정·경계를 추적할 수 있는가?
3. 입력 데이터와 상태 동기화의 품질을 확인했는가?
4. 구현 검증과 사용 맥락 타당화의 증거를 별도로 제시했는가?
5. 오차와 불확실성이 의사결정에 미치는 영향을 평가했는가?
6. 시스템이 변경될 때 재검토할 조건과 책임자를 정했는가?

## 검증·타당화 결과를 읽는 순서

먼저 모델의 사용 목적과 허용 가능한 오차를 확인하고, 다음으로 각 주장에 대응하는 시험·비교·검토 증거를 찾는다. “오차가 작다”는 표현은 비교 대상, 기간, 지표, 데이터 분할, 반복 조건이 없으면 해석할 수 없다.

실행 단계에서는 사전 검증 결과와 운영 후 결과를 분리한다. 운영 데이터가 모델의 학습·보정에 사용되었다면 독립적인 평가 구간을 유지해야 하며, 모델 구조나 목적이 바뀌었을 때 기존 타당화 결과가 여전히 유효한지 재검토한다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[concepts/Digital Twin Maturity|디지털트윈 성숙도]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[topics/Trusted Digital Twin|신뢰할 수 있는 디지털트윈]]

## 근거 자료

- [[papers/Verification and validation of digital twins - A systematic literature review for manufacturing applications (2025)]]
- [[web/The increasing potential and challenges of digital twins (2024)]]
- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]
