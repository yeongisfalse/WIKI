---
type: method
title: "Newsvendor Model"
status: draft
confidence: medium
confidence_reason: "기존 Newsvendor 수업 노트에서 underage·overage cost, critical ratio, 수요분포 기반 order-up-to 수준과 fixed cost가 있는 threshold 정책을 정리했다. 원본 예제의 수치·비용 정의는 재계산하지 않았고, 일반식의 가정 확인이 필요하다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Newsvendor Model.md"
source_vault_modified_at: "2026-05-11T19:22:02+09:00"
tags:
  - newsvendor
  - stochastic-optimization
  - inventory
  - operations-research
---

# Newsvendor Model

## 빠른 이해

- Newsvendor는 한 번의 주문 또는 생산 결정으로 불확실한 수요를 대응하며, 과잉재고 비용과 부족 비용의 균형으로 최적 수준을 정한다.
- 임계비율(critical ratio)은 underage cost와 overage cost의 상대적 크기를 수요분포의 분위수로 변환한다.
- 고정 주문비용이나 다기간·리드타임·용량 제약이 들어가면 단순 분위수 해가 바뀌며, `(S,s)` 정책이나 시뮬레이션 기반 평가가 필요할 수 있다.

## 정의

뉴스벤더 모형(Newsvendor Model)은 한 기간의 불확실한 수요에 대해 주문량 또는 생산량을 결정하는 확률적 재고 최적화 모형이다. 부패성 제품, 짧은 수명주기의 부품, 사전 생산이 필요한 자재처럼 남은 재고와 부족분의 비용이 서로 다른 상황에 사용한다.

- `D`: random demand
- `x`: order quantity 또는 available stock
- **Overage Cost `C_o`**: 수요보다 많이 확보했을 때의 단위 비용
- **Underage Cost `C_u`**: 수요보다 적게 확보했을 때의 단위 비용

## 기본 목적함수

단순한 one-period 모형에서는 기대 초과·부족 비용을 최소화한다.

$$
x^*=\arg\min_x\left\{C_oE[(x-D)^+]+C_uE[(D-x)^+]\right\}
$$

실제 문제에서는 구매비, 판매수익, 잔존가치, 폐기비, shortage disruption cost를 `C_o`, `C_u`에 일관되게 포함해야 한다. 비용 정의가 달라지면 같은 이름의 critical ratio라도 값이 달라진다.

## Critical Ratio

수요의 CDF를 `F_D`라고 하고 연속분포·고정 주문비 없음·기타 기본 가정을 두면 최적 order-up-to 수준 `S`는

$$
F_D(S)=\frac{C_u}{C_o+C_u}
$$

를 만족한다. 이를 critical ratio라고 한다.

- `C_u`가 클수록 품절을 피하기 위해 더 높은 수요 분위수를 선택한다.
- `C_o`가 클수록 과잉재고를 피하기 위해 더 낮은 수준을 선택한다.
- 이 결과는 수요 CDF와 비용 구조가 올바르게 정의되었다는 조건에서만 성립한다.

이산 수요에서는 CDF가 계단형이므로 equality보다 `F_D(S)≥C_u/(C_o+C_u)`를 만족하는 가장 작은 수준을 선택하는 방식으로 표현한다.

## Fixed Cost와 `(S,s)` 정책

주문을 할 때마다 배송·setup과 같은 고정비가 발생하면 현재 재고가 `S`보다 조금 낮다고 해서 항상 `S`까지 보충하는 것이 최적인 것은 아니다. 주문비와 shortage·overage 비용을 비교해 주문 여부의 threshold `s`를 만들 수 있다.

`(S,s)` 정책의 기본 구조는 다음과 같다.

- 현재 재고가 `s`보다 낮으면 `S`까지 주문한다.
- 현재 재고가 `s` 이상이면 주문하지 않는다.

고정비가 있는 경우 `S`와 `s`의 계산은 수요분포·리드타임·재고상태·비용 구조에 의존하므로, 단순 critical ratio만으로 결정하지 않는다.

## 시뮬레이션 기반 최적화와의 연결

Newsvendor는 수요분포와 비용 구조가 단순한 해석모형이다. 실제 제조·공급망에서는 다기간 재고, 리드타임, 용량, 서비스 수준, 수요 상관, 생산 스케줄이 추가되어 해석식이 복잡해질 수 있다. 이때 [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]로 정책 후보를 평가하고, [[concepts/Probability Distribution|확률분포]]와 [[concepts/Uncertainty Quantification|불확실성 정량화]]로 수요 가정의 민감도를 검토할 수 있다.

## 주의와 확인 필요

- `C_o`와 `C_u`는 문제의 판매·구매·폐기·품절 비용을 어떻게 정의했는지에 따라 달라진다.
- 단일 기간·즉시 보충·수요 분포가 알려졌다는 기본 가정은 실제 생산 시스템과 다를 수 있다.
- critical ratio는 fill rate와 관련 있지만, 일반적인 운영 성과지표로서의 fill rate와 항상 같은 의미는 아니다.
- 이 페이지는 기존 수업 노트에서 원리만 추출한 초안이며 원본 예제의 숫자 결과는 검증하지 않았다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/04_Industrial Engineering/Stochastic Process/Newsvendor Model.md`

## 연결

- [[concepts/Probability Theory|확률론]]
- [[concepts/Probability Distribution|확률분포]]
- [[concepts/Stochastic Process|확률과정]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[concepts/Decision Support System|의사결정 지원 시스템]]
