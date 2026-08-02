---
type: concept
title: "Queueing Theory"
status: draft
confidence: medium
confidence_reason: "기존 경영과학 수업 노트에서 대기행렬의 표기·안정성·Little's Law·Kingman 근사·제조 병목 연결을 컴파일했다. 공식 교재나 원 논문을 통한 수식 조건의 재검토가 필요하다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Queuing Theory.md"
source_vault_modified_at: "2026-05-10T21:00:42+09:00"
tags:
  - queueing-theory
  - stochastic-process
  - manufacturing
  - discrete-event-simulation
---

# Queueing Theory

## 정의

대기행렬 이론(Queueing Theory)은 고객·작업물·요청이 시스템에 도착하고, 제한된 서버·설비·작업자를 기다리며, 서비스를 받은 뒤 이탈하는 과정을 확률적으로 분석하는 방법이다. 제조에서는 대기시간, 재공품(Work-in-Process, WIP), 처리량(throughput), 자원 이용률과 병목을 함께 분석하는 데 사용한다.

## 기본 변수와 Kendall 표기

- 도착률 `λ`: 단위 시간당 도착하는 평균 개수
- 서비스율 `μ`: 서버 하나가 단위 시간당 처리할 수 있는 평균 개수
- 도착 간격·서비스시간: 각 고객 또는 작업물 사이의 시간과 처리 소요시간
- 서버 수와 대기공간: 병렬 자원 수와 허용되는 대기행렬의 크기

Kendall 표기에서 `M`은 지수분포 또는 Markovian 가정, `D`는 결정적 시간, `G`는 일반 분포를 뜻한다. 예를 들어 `M/M/1/∞`는 지수분포 도착 간격, 지수분포 서비스시간, 서버 1개, 무한 대기공간을 가정한다.

## 부하와 안정성

교통강도 또는 부하율(Traffic Intensity, `ρ`)은 수요와 처리능력의 비율이다. 단일 서버의 기본 형태는 다음과 같다.

$$
\rho = \frac{\lambda}{\mu}
$$

일반적으로 `ρ < 1`이어야 장기적으로 대기행렬이 안정될 수 있다. `ρ`가 1에 가까워질수록 작은 도착률 증가나 서비스시간 변동도 대기시간을 크게 늘릴 수 있다. 단, 안정성 조건은 대기공간, 서버 수, 도착·서비스 과정의 가정에 따라 달라지므로 모델마다 다시 확인해야 한다.

## 변동성과 Kingman 근사

일반적인 단일 서버 대기행렬에서 교통강도가 높지만 1보다 작을 때 평균 대기시간을 근사하는 대표적인 형태는 다음과 같다.

$$
E[W_q] \approx E[S]\frac{\rho}{1-\rho}\frac{c_a^2+c_s^2}{2}
$$

- `E[S]`: 평균 서비스시간
- `c_a`: 도착 간격의 변동계수
- `c_s`: 서비스시간의 변동계수

이 식은 평균만이 아니라 도착과 서비스의 변동성도 대기시간에 영향을 준다는 점을 보여준다. 특히 `ρ/(1-ρ)` 항 때문에 부하율이 1에 가까워질 때 대기시간이 급격히 증가한다. 이는 조건을 갖춘 일반 대기행렬에 대한 근사식이지, 모든 시스템의 정확한 해가 아니다.

## Little's Law

안정적인 시스템에서 장기 평균을 일관되게 정의할 수 있다면 Little's Law는 시스템 안의 평균 개수와 유입률·평균 체류시간을 연결한다.

$$
L = \lambda W
$$

- `L`: 시스템 안에 있는 평균 개수
- `λ`: 시스템을 통과하는 평균률
- `W`: 시스템 안에서 보내는 평균 시간

대기행렬만 분리하면 `L_q = λW_q`로 쓸 수 있다. 이 법칙은 특정 확률분포에만 의존하지 않지만, 도착률과 평균이 같은 범위·같은 집단을 가리키는지 확인해야 한다.

## 제조 시스템에서의 해석

- **처리량(Throughput)**: 단위 시간당 시스템을 빠져나가는 양
- 병렬 서버에서는 총 처리능력이 합쳐지고, 직렬 공정에서는 가장 느린 단계가 처리량의 상한이 된다.
- 따라서 병목은 단순히 대기열이 가장 긴 곳이 아니라, 수요와 처리능력·변동성·공정 연결을 함께 고려해 식별해야 한다.
- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]은 복잡한 자원 경쟁과 대기 규칙을 직접 표현하고, 대기행렬 이론은 결과를 해석할 기준식과 안정성 직관을 제공한다.

## 혜영님의 연구와의 관련성

디지털트윈 기반 생산 최적화에서 `ρ`, `W_q`, `L_q`, throughput은 후보 스케줄·자원배치·작업할당을 비교하는 기본 KPI가 될 수 있다. 다만 평균 KPI 하나만 최적화하면 높은 변동성과 극단적 지연을 놓칠 수 있으므로 [[concepts/Uncertainty Quantification|불확실성 정량화]]와 함께 사용해야 한다.

## 주의와 확인 필요

- 이 페이지의 수식과 용어는 로컬 수업 노트를 기반으로 한 초안이다.
- Kingman 식의 적용 조건, 다중 서버·유한 대기공간·우선순위·비정상 도착 과정에 대한 확장은 원문헌 또는 교재로 재검토해야 한다.
- 예제의 수치와 제조 병목 해석은 특정 가정 아래의 교육용 설명이며 실제 공정에 바로 일반화하지 않는다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Queuing Theory.md`

## 연결

- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]
- [[methods/SimPy|SimPy]]
- [[concepts/Poisson Process|포아송 과정]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
