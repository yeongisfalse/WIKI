---
type: concept
title: "Probability Inequalities"
status: draft
confidence: medium
confidence_reason: "기존 확률 부등식 노트에서 Markov·Chebyshev 부등식과 분포 비의존적 확률 상한의 의미를 정리했다. 실제 연구에서 사용할 때는 변수의 비음성·유한 분산 조건을 다시 확인해야 한다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/확률 부등식.md"
source_vault_modified_at: "2026-03-12T20:25:50+09:00"
tags:
  - probability-inequality
  - uncertainty
  - risk
  - statistics
---

# Probability Inequalities

## 역할

확률 부등식(Probability Inequalities)은 확률변수의 정확한 분포를 알지 못하더라도 평균·분산과 같은 제한된 정보로 사건의 확률을 상한 또는 하한으로 제한하는 도구다. 분포를 임의로 가정한 예측값보다 보수적이지만, 넓은 조건에서 성립하는 보장을 제공한다.

## Markov's Inequality

비음수 확률변수 `X≥0`와 `a>0`에 대해

$$
P(X\ge a)\le\frac{E[X]}{a}
$$

이다. 평균이 유한하면 특정 임계값 이상으로 커질 확률의 상한을 얻을 수 있다. 실제로는 이 상한이 느슨할 수 있으므로 정확한 분포를 알고 있을 때의 계산값과 구분한다.

## Chebyshev's Inequality

평균 `μ`와 유한한 분산 `σ²`을 갖는 임의의 확률변수에 대해 `k>0`이면

$$
P(|X-\mu|\ge k\sigma)\le\frac{1}{k^2}
$$

또는

$$
P(|X-\mu|< k\sigma)\ge1-\frac{1}{k^2}
$$

이다. 정규분포를 가정하지 않아도 평균 주변에 있을 확률의 하한을 얻는다는 점이 핵심이다.

Chebyshev 부등식은 Markov 부등식을 `(X-μ)²`에 적용해 유도할 수 있다.

## 연구에서의 해석

- 데이터가 부족해 분포를 신뢰하기 어려울 때 위험도·오류 확률의 보수적 범위를 만들 수 있다.
- 시뮬레이션 출력의 꼬리 위험을 논의할 때, 모수적 분포 가정에 의존하지 않는 기준선을 제공한다.
- 평균과 분산만으로 얻은 보장은 일반적으로 분포를 활용한 정밀한 확률보다 느슨하다.

따라서 부등식은 [[concepts/Uncertainty Quantification|불확실성 정량화]]의 대체물이 아니라, 분포 가정이 약할 때 사용하는 보조 기준이다. 최적화 제약으로 사용할 때는 보장의 보수성과 의사결정 비용을 함께 평가해야 한다.

## 주의와 확인 필요

- Markov 부등식에는 `X≥0` 조건이 필요하다.
- Chebyshev 부등식에는 유한한 평균과 분산이 필요하다.
- 부등식이 주는 상한·하한을 실제 확률의 추정치나 신뢰구간과 혼동하지 않는다.
- 이 페이지는 기존 수업 노트를 컴파일한 초안이다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/확률 부등식.md`

## 연결

- [[concepts/Probability Theory|확률론]]
- [[concepts/Probability Distribution|확률분포]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
