---
type: concept
title: "Stochastic Process"
status: draft
confidence: medium
confidence_reason: "기존 Poisson Process, DTMC, Queueing Theory 노트를 바탕으로 확률과정의 공통 구조와 연구용 분류를 통합했다. 각 모델의 수학적 조건은 개별 페이지와 원문헌에서 다시 확인해야 한다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Poisson Process.md"
  - "/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Discrete Time Markov Chain(DTMC).md"
  - "/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Queuing Theory.md"
source_vault_modified_at:
  - "2026-05-21T19:21:03+09:00"
  - "2026-05-11T19:21:50+09:00"
  - "2026-05-10T21:00:42+09:00"
tags:
  - stochastic-process
  - state-transition
  - event-arrival
  - simulation
---

# Stochastic Process

## 빠른 이해

- 확률과정은 시간 또는 순서에 따라 변하는 확률변수들의 모음이며, 상태·시간의 이산/연속성, 독립성, stationary 여부로 모델을 분류한다.
- Poisson Process는 사건 도착, Markov Chain은 상태 전이, Queueing Process는 도착·서비스·대기를 표현하는 대표 모델이다.
- 모델 선택은 데이터가 무엇을 관측하는지, 상태가 무엇인지, 시간 의존성이 어떻게 나타나는지, 분석 목적이 예측인지 시뮬레이션인지에 따라 결정한다.

## 정의

확률과정(Stochastic Process)은 시간 또는 다른 인덱스 `t`에 따라 변하는 확률변수들의 모음이다.

$$
\{X_t:t\in T\}
$$

`X_t`는 시각 `t`의 상태 또는 관측값이고, 가능한 값의 집합은 상태공간(State Space)이다. 따라서 확률과정은 “한 번의 확률 실험”이 아니라 시간에 따른 불확실한 변화와 의존구조를 표현한다.

## 분류 축

| 분류 축 | 주요 경우 | 예시 |
| --- | --- | --- |
| 시간 인덱스 | Discrete Time / Continuous Time | DTMC / Poisson Process |
| 상태공간 | Discrete State / Continuous State | 설비 상태 / 온도·재고량 |
| 변화 방식 | Event count / State transition / Continuous evolution | 도착 수 / 고장·복구 / 물리량 변화 |
| 의존구조 | Independent Increments / Markov Property / General Dependence | Poisson / DTMC / 실측 데이터 모델 |

이 분류는 서로 배타적인 이름표가 아니다. 예를 들어 포아송 과정은 연속시간·이산상태의 계수과정이며, 현재까지의 도착 수와 미래 증분 사이에 독립증분 성질을 갖는다.

## 핵심 모델

### Poisson Process

포아송 과정은 시간 구간별 사건 도착 수를 모델링한다. 균질 포아송 과정은 일정 발생률 `λ`와 독립·정상 증분을 가정하고, 비균일 포아송 과정은 `λ(t)`로 시간별 발생률을 표현한다.

→ [[concepts/Poisson Process|Poisson Process]]

### Markov Chain

마르코프 체인은 다음 상태가 전체 과거가 아니라 현재 상태에만 조건부로 의존한다고 가정한다. 유한 상태에서는 전이확률행렬 `P`와 정상분포 `π`로 장기 거동을 분석한다.

→ [[concepts/Markov Chain|Markov Chain]]

### Queueing Process

대기행렬 시스템은 도착, 서비스, 대기, 이탈과 자원 상태가 함께 변하는 확률과정이다. 도착률·서비스율·변동성·자원 수에 따라 queue length, waiting time, throughput이 달라진다. 특정 조건에서 대기행렬을 Markov process로 표현할 수 있지만, 모든 대기행렬이 자동으로 Markov인 것은 아니다.

→ [[concepts/Queueing Theory|Queueing Theory]]

## 모델을 선택할 때의 질문

1. 시간과 상태를 어떤 해상도로 이산화할 것인가?
2. 관심 대상은 상태값인가, 사건 발생 수인가, 전이인가?
3. 미래가 현재 상태만으로 충분히 설명되는가?
4. 도착·전이의 독립성, 정상성, 분포 가정이 데이터와 맞는가?
5. 상태공간을 세분화하면 설명력은 증가하지만 추정·계산 부담이 커지지 않는가?
6. 초기분포, 경계조건, absorbing state, 종료조건을 어떻게 정의할 것인가?

## 시뮬레이션에서의 역할

[[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]은 확률과정의 한 실현 경로(sample path)를 생성해 대기시간·처리량·고장·복구와 같은 결과를 추정할 수 있다. 여러 난수 시드와 반복 실행을 사용해야 단일 실행 경로를 장기 성능으로 오해하지 않는다.

확률과정 모델은 [[concepts/Uncertainty Quantification|불확실성 정량화]]의 입력 구조이기도 하다. 파라미터의 불확실성, 모델 구조의 불확실성, 관측 노이즈를 구분해 기록한다.

## 주의와 확인 필요

- “확률과정”은 하나의 분포나 알고리즘이 아니라 여러 확률변수의 시간적 구조를 가리키는 상위 개념이다.
- 평균 발생률만 맞는다고 포아송 과정이 되는 것은 아니며, 자기상관·군집·계절성·상태 의존성을 점검해야 한다.
- 마르코프 가정은 상태를 충분히 정의했다는 전제와 함께 검토해야 한다. 현재 상태에 과거의 중요한 정보가 빠져 있으면 마르코프성이 깨질 수 있다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Poisson Process.md`
- `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Discrete Time Markov Chain(DTMC).md`
- `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Queuing Theory.md`

## 연결

- [[concepts/Probability Theory|확률론]]
- [[concepts/Probability Distribution|확률분포]]
- [[concepts/Poisson Process|Poisson Process]]
- [[concepts/Markov Chain|Markov Chain]]
- [[concepts/Queueing Theory|Queueing Theory]]
- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]
