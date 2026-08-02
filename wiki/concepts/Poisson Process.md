---
type: concept
title: "Poisson Process"
status: draft
confidence: medium
confidence_reason: "기존 경영과학 수업 노트에서 포아송 과정의 정의·증분·도착간격·병합·thinning·비균일 확장을 컴파일했다. 원본 노트의 수식 조건과 표기 관례는 외부 교재로 재확인할 필요가 있다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Poisson Process.md"
source_vault_modified_at: "2026-05-21T19:21:03+09:00"
tags:
  - poisson-process
  - stochastic-process
  - discrete-event-simulation
  - uncertainty
---

# Poisson Process

## 정의

포아송 과정(Poisson Process)은 시간에 따라 무작위로 발생하는 사건의 누적 개수를 세는 계수과정(Counting Process)이다. `N(t)`를 시각 0부터 `t`까지 발생한 사건 수라고 하면, `N(t)`는 0에서 시작해 시간이 지날수록 감소하지 않는다.

## 균질 포아송 과정

발생률이 시간에 따라 일정한 `λ`인 균질 포아송 과정(Homogeneous Poisson Process)은 다음 성질을 갖는다.

- 서로 겹치지 않는 시간 구간의 증분은 독립이다.
- 길이가 같은 구간의 증분 분포는 시작 시점과 무관하다(정상 증분).
- 길이 `t`인 구간의 사건 수는 `Poisson(λt)`를 따른다.
- 첫 도착까지의 시간과 연속 도착 간격은 평균 `1/λ`인 지수분포(Exponential Distribution)를 따른다.

$$
P(N(t+s)-N(s)=n)=e^{-\lambda t}\frac{(\lambda t)^n}{n!}
$$

이 모델은 서로 독립적인 고객 도착, 고장 발생, 요청 도착을 단순화하는 출발점이 될 수 있다.

## 병합과 thinning

- **Merging**: 독립적인 포아송 과정 두 개를 합치면 발생률이 각 발생률의 합인 포아송 과정이 된다.
- **Thinning**: 각 도착을 독립적으로 확률 `p`로 유형 A에 배정하면 A 도착은 `pλ`의 포아송 과정이 된다. 나머지 유형은 `(1-p)λ`의 포아송 과정이 되며, 표준적인 thinning 가정 아래 두 과정은 독립이다.

이 성질은 전체 주문 도착을 제품 유형별로 나누거나, 센서 이벤트를 정상·고장 유형으로 분리하는 모델의 기초가 된다.

## 비균일 포아송 과정

발생률이 시각에 따라 `λ(t)`로 바뀌는 비균일 포아송 과정(Non-homogeneous Poisson Process, NHPP)에서는 길이만으로 평균 사건 수를 정할 수 없다. 구간 `[s, s+t]`의 평균은 누적 발생률이다.

$$
E[N(s+t)-N(s)] = \int_s^{s+t}\lambda(u)\,du
$$

따라서 동일한 길이의 시간 구간이라도 피크 시간대와 비피크 시간대의 사건 수 분포가 다를 수 있다.

## 시뮬레이션과 디지털트윈에서의 역할

포아송 과정은 도착·고장·요청 이벤트를 생성하는 확률적 입력 모델이 될 수 있다. 그러나 실제 시스템이 독립 증분, 일정 발생률, 지수분포 간격을 만족하는지는 데이터로 확인해야 한다. [[methods/SimPy|SimPy]]에서는 도착 간격을 생성하는 프로세스와 사건을 연결할 수 있고, [[concepts/Queueing Theory|대기행렬 이론]]에서는 그 입력이 대기시간·처리량에 미치는 영향을 분석한다.

## 주의와 확인 필요

- 포아송 과정 가정은 편리한 기준 모델이지 실제 도착의 기본값이 아니다. 시간대별 수요, 군집 도착, 자기상관, 용량 제한을 점검해야 한다.
- NHPP를 구현할 때는 `λ(t)`의 단위와 적분 구간을 명확히 해야 한다.
- 이 페이지는 로컬 수업 노트를 컴파일한 초안이며 원문헌·데이터 기반 가정 검증은 수행하지 않았다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Poisson Process.md`

## 연결

- [[concepts/Queueing Theory|대기행렬 이론]]
- [[methods/SimPy|SimPy]]
- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
