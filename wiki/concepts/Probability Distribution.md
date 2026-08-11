---
type: concept
title: "Probability Distribution"
status: draft
confidence: medium
confidence_reason: "기존 확률·통계 노트에서 PMF·PDF·CDF와 결합·주변·조건부 분포를 컴파일했다. 원본의 일부 시각 자료는 가져오지 않았고, 연구에 사용할 분포 선택은 데이터 기반 검토가 필요하다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/Probability Distribution.md"
source_vault_modified_at: "2026-03-23T14:37:29+09:00"
tags:
  - probability
  - statistics
  - uncertainty
  - simulation
---

# Probability Distribution

## 빠른 이해

- 확률분포는 확률변수의 가능한 값과 그 가능성을 연결하는 규칙이며, 이산형은 PMF, 연속형은 PDF와 CDF로 표현한다.
- 분포를 선택한다는 것은 평균 하나를 정하는 것이 아니라 변동·꼬리·왜도·상관·경계와 같은 입력의 구조를 선택하는 일이다.
- 시뮬레이션에서는 경험자료와 가정된 분포를 구분하고, 적합도·잔차·민감도·외삽 범위를 확인해야 결과의 불확실성을 해석할 수 있다.

## 정의

확률분포(Probability Distribution)는 확률변수가 가질 수 있는 값과 각 값 또는 구간에 대응하는 가능성을 수학적으로 표현한 것이다. 시뮬레이션에서는 실제 시스템의 도착·처리·고장·수요 변동을 입력으로 바꾸는 기본 언어다.

## PMF, PDF, CDF

| 대상 | 함수 | 확률의 의미 |
| --- | --- | --- |
| 이산 확률변수 | 확률질량함수(Probability Mass Function, PMF) | `P(X=x)` 자체 |
| 연속 확률변수 | 확률밀도함수(Probability Density Function, PDF) | 구간 아래 면적 |
| 이산·연속 공통 | 누적분포함수(Cumulative Distribution Function, CDF) | `F(x)=P(X≤x)` |

연속형에서는 한 점의 확률 `P(X=x)`가 0일 수 있고, 구간확률은 밀도를 적분해 얻는다. CDF는 단조 증가하고 0과 1 사이에 있으며, 연속형에서는 조건이 맞을 때 미분으로 PDF를 얻을 수 있다.

## 여러 변수의 분포

- **결합분포(Joint Distribution)**: 여러 확률변수가 동시에 가질 값을 표현한다.
- **주변분포(Marginal Distribution)**: 다른 변수를 합산 또는 적분해 관심 변수 하나의 분포만 남긴다.
- **조건부 분포(Conditional Distribution)**: 다른 변수의 값 또는 상태가 주어졌을 때의 분포다.
- **독립(Independence)**: 결합분포가 주변분포의 곱으로 분해되는 관계다. 독립을 가정하면 모델이 단순해지지만, 실제 공정의 공통 원인과 시간상관을 놓칠 수 있다.

## 시뮬레이션 입력으로 사용할 때

분포를 선택하기 전에 다음을 기록한다.

1. 무엇을 관측한 변수인지와 단위를 정의한다.
2. 데이터의 기간·조건·표본 추출 방법을 기록한다.
3. 이산·연속 여부와 관측된 절단·검열·결측을 점검한다.
4. 후보 분포의 적합도만이 아니라 평균·분산·꼬리·시간상관을 비교한다.
5. 선택한 분포가 [[concepts/Uncertainty Quantification|불확실성 정량화]]와 의사결정 결과에 미치는 민감도를 확인한다.

분포를 잘못 선택하면 시뮬레이션 출력이 그럴듯해도 대기시간·고장위험·최적 정책을 체계적으로 왜곡할 수 있다.

## 주의와 확인 필요

- PDF의 함수값은 일반적으로 확률 자체가 아니라 밀도이며 1보다 클 수도 있다.
- 독립성은 주변분포와 조건부 분포가 같다는 한 가지 관찰만으로 확정하지 않는다.
- 이 페이지는 기존 학습 노트의 개념 정리 초안이며, 실제 연구에 사용할 분포는 원자료와 통계적 검정으로 다시 확인해야 한다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/Probability Distribution.md`

## 연결

- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[concepts/Poisson Process|포아송 과정]]
- [[concepts/Queueing Theory|대기행렬 이론]]
- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]
