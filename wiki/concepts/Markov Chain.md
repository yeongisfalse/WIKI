---
type: concept
title: "Markov Chain"
status: draft
confidence: medium
confidence_reason: "기존 이산 시간 마르코프 체인 수업 노트에서 Markov property·전이행렬·정상분포·상태분류를 컴파일했다. 일부 상태분류 정리와 무한 상태공간 결과는 외부 교재로 재확인해야 한다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Discrete Time Markov Chain(DTMC).md"
source_vault_modified_at: "2026-05-11T19:21:50+09:00"
tags:
  - markov-chain
  - stochastic-process
  - state-transition
  - manufacturing
---

# Markov Chain

## 빠른 이해

- 마르코프 체인은 현재 상태가 미래 전이를 결정하는 데 충분하다는 가정 아래, 상태와 전이확률로 시간 변화를 표현한다.
- 전이행렬의 각 행은 현재 상태에서 가능한 다음 상태의 확률분포이며, 행렬의 거듭제곱은 여러 단계 뒤의 전이확률을 계산한다.
- 정상분포가 존재하거나 초기 상태의 영향이 사라지는지는 irreducibility·aperiodicity·recurrent 구조에 달려 있으므로 단순히 전이행렬을 반복한다고 가정하면 안 된다.

## 정의

마르코프 체인(Markov Chain)은 다음 상태가 전체 과거가 아니라 현재 상태에 조건부로 의존하는 확률 과정이다. 이 성질을 마르코프 성질(Markov Property)이라고 한다.

$$
P(X_{n+1}=j\mid X_0,\ldots,X_n)=P(X_{n+1}=j\mid X_n)
$$

여기서 상태공간(State Space)은 시스템이 가질 수 있는 상태의 집합이다. 상태를 어떻게 정의하느냐에 따라 같은 현상도 서로 다른 마르코프 모델이 된다.

## 전이확률행렬

유한 상태공간에서는 한 단계 전이확률을 행렬 `P`로 표현한다.

$$
p_{ij}=P(X_{n+1}=j\mid X_n=i),\qquad p_{ij}\ge 0,\qquad \sum_j p_{ij}=1
$$

초기분포를 행벡터 `a₀`로 두면 `n` 단계 뒤의 분포는 `a₀Pⁿ`이다. 이 표현은 설비 상태, 작업 진행상태, 재고상태, 품질등급처럼 이산적인 상태 전이를 모델링하는 데 사용할 수 있다.

## 정상분포와 극한분포의 구분

- **정상분포(Stationary Distribution, `π`)**: `πP=π`를 만족하는 분포. 이 분포에서 시작하면 한 단계가 지나도 분포가 변하지 않는다.
- **극한분포(Limiting Distribution)**: `n`이 무한히 커질 때 `Pⁿ` 또는 `a₀Pⁿ`가 수렴해 얻는 분포.

정상분포가 존재한다고 해서 극한분포가 항상 존재하거나 둘이 반드시 같아지는 것은 아니다. 예를 들어 주기적인 체인은 정상분포를 가지면서도 상태가 순환해 `Pⁿ`이 수렴하지 않을 수 있다. 유한 상태·기약(irreducible)·비주기(aperiodic)와 같은 조건은 유일한 정상분포와 초기상태와 무관한 극한 거동을 논의할 때 확인해야 한다.

## 상태와 클래스

- **Accessibility**: 어떤 유한 단계 안에 `i`에서 `j`로 갈 확률이 양수인 경우
- **Communication**: 서로 양방향으로 접근 가능한 경우
- **Irreducible**: 모든 상태가 하나의 통신 클래스에 속하는 경우
- **Periodicity**: 상태로 되돌아오는 가능한 단계들의 최대공약수로 정의되는 성질
- **Absorbing State**: 한 번 들어가면 계속 그 상태에 머무는 상태
- **Recurrent·Transient**: 장기적으로 자기 상태로 돌아올 가능성에 따른 분류

상태 분류는 단순한 용어 목록이 아니라, 장기 안정상태·고장 흡수·복구 가능성·초기상태의 영향이 어떻게 달라지는지를 판단하는 도구다.

## 주의와 확인 필요

- 마르코프 성질은 데이터가 자동으로 보장하는 사실이 아니라 모델링 가정이다.
- 정상분포·극한분포의 존재와 유일성은 상태공간과 전이행렬의 구조에 의존한다.
- 이 페이지는 로컬 수업 노트를 기반으로 한 초안이며, 특히 무한 상태공간과 재귀성 결과는 별도 검증이 필요하다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Discrete Time Markov Chain(DTMC).md`

## 연결

- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]
- [[concepts/Queueing Theory|대기행렬 이론]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
