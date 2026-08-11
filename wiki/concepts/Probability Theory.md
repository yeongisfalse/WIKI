---
type: concept
title: "Probability Theory"
status: draft
confidence: medium
confidence_reason: "기존 확률론·확률변수 수업 노트 3개에서 사건, 조건부확률, 베이즈 정리, 확률변수, 기댓값·분산의 공통 골격을 통합했다. 원본 노트의 일부 표기와 수식은 외부 교재로 재확인해야 한다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/Probability Theory & Random Variables.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/확률.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/확률변수와 확률함수.md"
source_vault_modified_at:
  - "2026-03-23T14:40:37+09:00"
  - "2026-01-20T23:41:00+09:00"
  - "2026-03-18T17:52:06+09:00"
tags:
  - probability
  - random-variable
  - expectation
  - variance
  - statistics
---

# Probability Theory

## 빠른 이해

- 확률론은 불확실한 결과를 표본공간·사건·확률측도로 표현하고, 조건부확률과 확률변수로 관측과 예측을 연결한다.
- 독립과 조건부 독립을 구분해야 곱셈법칙·베이즈 정리·분포의 결합을 올바르게 사용할 수 있다.
- 기대값과 분산은 결과의 평균 수준과 변동을 요약하지만, 분포의 꼬리·비대칭·시간 의존성까지 설명하지는 않으므로 필요하면 확률과정과 위험 지표로 확장해야 한다.

## 확률공간과 사건

확률론(Probability Theory)은 불확실한 실험과 관측을 수학적으로 표현하는 이론이다. 확률공간(Probability Space)은 보통 표본공간 `S`, 사건들의 집합, 확률측도로 구성한다.

- **Sample Space `S`**: 가능한 결과의 전체 집합
- **Event `A`**: 표본공간의 부분집합으로 표현되는 관심 결과
- **Probability `P(A)`**: 사건이 발생할 가능성을 나타내는 값

확률은 다음 Kolmogorov 공리를 만족한다.

1. `P(A) ≥ 0`
2. `P(S) = 1`
3. 서로 배반인 사건들의 합집합 확률은 각 확률의 합이다.

이 공리에서 여사건, 포함관계, 합집합 확률과 같은 기본 성질이 유도된다.

## 배반과 독립

- **Mutually Exclusive**: `A ∩ B = ∅`인 관계. 두 사건이 동시에 발생할 수 없다.
- **Independent**: 한 사건의 발생이 다른 사건의 확률에 정보를 추가하지 않는 관계.

독립이면

$$
P(A\cap B)=P(A)P(B)
$$

이다. 양의 확률을 갖는 두 사건은 동시에 배반이면서 독립일 수 없다. 배반은 가능한 결과의 겹침에 관한 개념이고, 독립은 확률적 정보의 의존성에 관한 개념이므로 혼동하지 않는다.

## 조건부확률과 베이즈 정리

조건부확률(Conditional Probability)은 사건 `B`가 관측되었다는 조건에서 사건 `A`의 확률을 나타낸다.

$$
P(A\mid B)=\frac{P(A\cap B)}{P(B)},\qquad P(B)>0
$$

표본공간을 관측된 정보에 맞게 좁히는 연산으로 해석할 수 있다. 표본공간의 분할 `A₁, …, Aₙ`에 대해서는 전확률 법칙(Law of Total Probability)이 성립한다.

$$
P(B)=\sum_i P(A_i)P(B\mid A_i)
$$

베이즈 정리(Bayes' Theorem)는 관측된 결과를 이용해 원인 또는 가설의 확률을 갱신한다.

$$
P(A_k\mid B)=\frac{P(A_k)P(B\mid A_k)}{\sum_iP(A_i)P(B\mid A_i)}
$$

시뮬레이션과 디지털트윈에서는 센서 관측으로 상태·고장 원인·수요 가설을 갱신하는 구조를 설명하는 기초가 된다. 단, 사전확률과 우도 모델의 근거를 별도로 기록해야 한다.

## 확률변수와 분포

확률변수(Random Variable) `X`는 표본공간의 결과를 수치로 매핑하는 함수다. 확률변수의 가능한 값과 확률의 대응은 [[concepts/Probability Distribution|확률분포]]로 표현한다.

- 이산 확률변수: 셀 수 있는 값을 가지며 PMF로 표현
- 연속 확률변수: 구간의 값을 가지며 PDF와 CDF로 표현
- 여러 변수를 함께 다룰 때 결합·주변·조건부 분포를 사용

## 기댓값과 분산

기댓값(Expected Value)은 확률변수의 장기 평균 수준이다.

$$
E[X]=\sum_x xP(X=x)\quad\text{or}\quad E[X]=\int xf_X(x)dx
$$

기댓값은 선형성을 갖는다.

$$
E[aX+bY]=aE[X]+bE[Y]
$$

분산(Variance)은 평균 주변의 변동성을 나타낸다.

$$
Var(X)=E[(X-E[X])^2]=E[X^2]-E[X]^2
$$

두 변수의 함께 움직이는 정도는 공분산(Covariance)으로 표현한다.

$$
Cov(X,Y)=E[(X-E[X])(Y-E[Y])]
$$

일반적으로

$$
Var(X+Y)=Var(X)+Var(Y)+2Cov(X,Y)
$$

이며, 독립이면 공분산이 0이 되어 분산을 단순화할 수 있다. 독립과 무상관은 일반적으로 같은 개념이 아니다.

## 지식 지도에서의 위치

확률론은 [[concepts/Probability Distribution|확률분포]], [[concepts/Probability Inequalities|확률 부등식]], [[concepts/Stochastic Process|확률과정]], [[concepts/Statistical Inference|통계적 추론]]의 공통 기반이다. 분포 선택, 상태 전이, 추정과 검정은 모두 표본공간·조건부 확률·기댓값·변동성에 대한 가정을 포함한다.

## 주의와 확인 필요

- 확률변수의 기댓값·분산이 존재하는지와 적분·합이 수렴하는지를 확인해야 한다.
- 독립성은 편리한 가정이지만 실제 센서·수요·공정 데이터의 시간상관과 공통 원인을 제거하지 않는다.
- 이 페이지는 기존 학습 노트를 통합한 초안이며, 원본에 포함된 이미지와 일부 잘못된 표기는 재현하지 않았다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/Probability Theory & Random Variables.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/확률.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/확률변수와 확률함수.md`

## 연결

- [[concepts/Probability Distribution|확률분포]]
- [[concepts/Probability Inequalities|확률 부등식]]
- [[concepts/Stochastic Process|확률과정]]
- [[concepts/Statistical Inference|통계적 추론]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
