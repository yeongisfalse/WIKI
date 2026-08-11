---
type: concept
title: "Statistical Inference"
status: draft
confidence: medium
confidence_reason: "기존 추정·가설검정·두 모집단 추론 노트에서 추정량, 신뢰구간, 검정, 오류·검정력, 두 집단 비교의 공통 구조를 컴파일했다. 원본의 일부 표본크기 조건과 검정식은 연구 목적·분포 가정에 따라 재검토해야 한다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/추정.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/가설검정.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/두 모집단의 추론과 검정.md"
source_vault_modified_at:
  - "2026-01-20T14:41:00+09:00"
  - "2026-01-20T14:41:00+09:00"
  - "2026-01-20T14:41:00+09:00"
tags:
  - statistical-inference
  - estimation
  - hypothesis-testing
  - model-validation
  - statistics
---

# Statistical Inference

## 빠른 이해

- 통계적 추론은 표본에서 모집단의 모수나 차이에 대해 불확실성을 포함한 주장을 만드는 과정이다.
- 점추정은 하나의 값을, 구간추정은 가능한 값의 범위와 반복표집 관점을, 가설검정은 자료가 특정 귀무가설과 얼마나 양립하는지를 다룬다.
- p-value, 신뢰구간, 효과크기, 검정력은 서로 다른 정보를 제공한다. 통계적 유의성만으로 실질적 중요성이나 인과성을 판단할 수 없다.

## 정의와 구성요소

통계적 추론(Statistical Inference)은 표본으로부터 모집단의 모수·관계·차이에 대한 불확실한 결론을 도출하는 과정이다.

- **Population**: 관심 있는 전체 대상
- **Parameter**: 모집단의 평균·분산·비율처럼 알고 싶은 값
- **Sample**: 모집단에서 관측한 자료
- **Statistic**: 표본으로 계산한 값
- **Estimator**: 모수를 추정하기 위해 사용하는 통계량

통계적 추론은 “표본에서 계산된 수치”와 “모집단에 대한 주장”을 구분하는 데서 시작한다.

## 추정량의 성질

- **Unbiasedness**: `E[θ̂]=θ`. 반복 표본추출에서 평균적으로 모수에 맞는 성질
- **Consistency**: 표본 크기가 커질수록 `θ̂`가 `θ`에 수렴하는 성질
- **Efficiency**: 같은 조건의 추정량 중 분산이 작은 성질
- **Sufficiency**: 표본이 모수에 관한 정보를 충분통계량에 보존하는 성질

이 성질은 서로 자동으로 보장되지 않는다. 실제 선택에서는 편향·분산·표본크기·모델 가정과 목적함수를 함께 비교한다.

## Point Estimation과 Interval Estimation

**Point Estimation**은 모수를 하나의 추정값으로 제시한다. 예를 들어 표본평균은 모평균의 점추정량이 될 수 있다.

**Interval Estimation**은 추정의 불확실성을 구간으로 제시한다. 신뢰구간(Confidence Interval)은 반복해서 같은 절차로 표본을 수집할 때 그 절차가 장기적으로 모수를 포함하는 비율을 말한다. 데이터를 관측한 뒤 고정된 모수가 특정 구간 안에 들어갈 확률이라고 해석하지 않는다.

일반적인 형태는 다음과 같다.

$$
\text{estimate}\ \pm\ \text{critical value}\times\text{standard error}
$$

표본 크기, 신뢰수준, 분산·분포 가정이 구간 폭에 영향을 준다.

## Standard Error

표준오차(Standard Error)는 통계량의 표본분포 표준편차로, 추정량이 표본에 따라 얼마나 변하는지 나타낸다. 표본평균의 경우 독립·동일분포와 유한 분산을 가정하면

$$
SE(\bar X)=\frac{\sigma}{\sqrt n}
$$

이며 `σ`를 모를 때는 `s`로 대체한다. 표본 크기가 커지면 표준오차는 감소하지만, 체계적 편향이나 잘못된 모델 가정이 자동으로 사라지는 것은 아니다.

## Hypothesis Testing

가설검정(Hypothesis Testing)은 귀무가설 `H₀`과 대립가설 `H₁`을 세우고 표본이 `H₀`과 얼마나 양립하는지 평가한다.

1. 연구 질문과 `H₀`, `H₁`을 정의한다.
2. 유의수준 `α`와 검정 방향을 사전에 정한다.
3. 자료·가정에 맞는 검정통계량과 표본분포를 선택한다.
4. 검정통계량, 신뢰구간, p-value와 효과크기를 함께 해석한다.
5. `H₀`을 기각하거나, 기각할 충분한 증거가 없다고 보고한다.

p-value는 `H₀`이 참이라고 가정했을 때 관측된 결과 이상으로 극단적인 결과가 나올 확률이다. p-value는 `H₀`이 참일 확률이나 효과의 크기가 아니다. `p≤α`라고 해서 실질적 중요성이나 인과관계가 자동으로 입증되는 것도 아니다.

## 오류와 검정력

| 실제 상태 | `H₀` 기각 | `H₀` 기각하지 못함 |
| --- | --- | --- |
| `H₀` 참 | Type I Error `α` | 올바른 결정 |
| `H₁` 참 | 올바른 결정, Power `1-β` | Type II Error `β` |

표본 크기, 효과크기, 변동성, 유의수준이 검정력에 영향을 준다. 표본을 크게 하면 작은 차이도 유의해질 수 있으므로 통계적 유의성과 실질적 중요성을 분리한다.

## 두 집단 비교

두 모집단의 평균·비율·분산을 비교할 때는 먼저 자료의 독립성, 대응 여부, 분산 구조와 측정 단위를 확인한다.

- **Independent Samples**: 두 집단의 관측이 서로 독립
- **Paired Samples**: 같은 대상의 전후 측정 또는 자연스럽게 짝지어진 관측
- 평균 차이, 비율 차이, 분산비에 따라 통계량과 표본분포가 달라짐

독립 표본과 대응 표본을 혼동하거나, 분산이 같다는 가정을 확인하지 않고 pooled 검정을 사용하면 표준오차와 p-value가 왜곡될 수 있다. 표본분포와 가정이 맞지 않으면 Welch 방법이나 비모수·재표본 방법을 검토한다.

## 시뮬레이션·모델 검증에서의 사용

통계적 추론은 관측 데이터로 시뮬레이션 입력분포와 파라미터를 추정하거나, 모델 출력과 실제 시스템의 차이가 우연한 변동 범위에 있는지 평가할 때 사용한다. 이때 통계적 검정 하나만으로 모델 타당화가 끝나는 것은 아니며, [[concepts/Model Verification and Validation|모델 검증과 타당화]]의 사용 맥락·오차·전문가 근거와 함께 해석해야 한다.

## 주의와 확인 필요

- 신뢰구간, p-value, 검정력은 표본추출·독립성·분포·분산·검정 사전계획의 가정에 의존한다.
- “귀무가설을 채택한다”보다 “기각할 충분한 증거가 없다”는 표현이 해석상 안전하다.
- 다중비교, 선택적 보고, 데이터 누수, 시간상관을 무시하면 유의성이 과대평가될 수 있다.
- 이 페이지는 수업 노트를 통합한 초안이며 특정 연구 데이터에 대한 검정 절차를 결정하는 문서가 아니다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/추정.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/가설검정.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/두 모집단의 추론과 검정.md`

## 연결

- [[concepts/Probability Theory|확률론]]
- [[concepts/Probability Distribution|확률분포]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
