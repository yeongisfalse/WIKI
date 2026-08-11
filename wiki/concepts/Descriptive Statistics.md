---
type: concept
title: "Descriptive Statistics"
status: draft
confidence: medium
confidence_reason: "기존 기술통계 노트에서 자료척도, 중심·산포, 분위수·IQR, 변동계수·z-score, 왜도의 연구용 기초를 추출했다. 지표의 적합성은 데이터 생성과 측정척도에 따라 달라진다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/Descriptive Statistics.md"
source_vault_modified_at: "2026-03-23T14:38:29+09:00"
tags:
  - descriptive-statistics
  - data-quality
  - statistics
  - uncertainty
---

# Descriptive Statistics

## 빠른 이해

- 기술통계는 이미 관측된 자료를 중심·산포·분포 형태로 요약하는 단계이며, 모집단에 대한 인과적 결론을 자동으로 만들어 주지 않는다.
- 평균·중앙값·분산·분위수·IQR·z-score는 서로 다른 질문에 답한다. 이상치와 측정척도에 따라 어떤 지표를 사용할지가 달라진다.
- 시뮬레이션 입력을 만들 때는 요약값만 저장하지 말고 표본 수, 결측, 시간 순서, 측정 단위, 분포 형태를 함께 기록해야 한다.

## 역할

기술통계(Descriptive Statistics)는 관측된 자료의 구조·중심·변동·분포 형태를 요약하는 방법이다. 모집단에 대한 일반화나 인과관계를 자동으로 제공하지 않으며, 데이터 탐색과 모델 입력 설계의 첫 단계로 사용한다.

## 자료의 종류와 측정척도

- **Nominal**: 범주 이름만 의미가 있으며 순서·차이를 계산할 수 없다.
- **Ordinal**: 순서가 있지만 범주 간 간격이 동일하다고 보장되지 않는다.
- **Interval**: 차이는 해석할 수 있지만 절대적 0이 없다.
- **Ratio**: 의미 있는 절대적 0이 있어 비율 비교가 가능하다.
- **Discrete / Continuous**: 값의 공간이 셀 수 있는지 또는 연속적인지에 따른 구분이다.

평균·비율·차이와 같은 연산은 측정척도와 데이터 생성방식에 맞게 선택해야 한다.

## 중심과 산포

- **Mean**: 전체 합을 관측 수로 나눈 값. 이상치와 긴 꼬리에 민감하다.
- **Median**: 순서대로 정렬했을 때 가운데 값. 비대칭 분포나 이상치가 있을 때 대표값으로 유용할 수 있다.
- **Variance / Standard Deviation**: 평균 주변의 변동을 측정한다. 표본분산은 보통 `n-1`로 나누어 불편 추정량을 사용한다.
- **Coefficient of Variation**: `SD / Mean`. 양의 비율척도에서 서로 다른 평균 수준의 상대적 변동을 비교할 때 사용한다.

한 지표만으로 자료를 대표하지 말고 평균·중앙값·분산·표본크기·극단값을 함께 확인한다.

## Quantile과 IQR

분위수(Quantile)는 누적분포가 특정 비율에 도달하는 위치다. `Q₁`, `Q₂`, `Q₃`는 각각 25%, 50%, 75% 위치를 나타내며

$$
IQR=Q_3-Q_1
$$

은 중앙 50%의 범위를 나타낸다. Box Plot의 전형적인 이상치 규칙은 `Q₁-1.5IQR`보다 작거나 `Q₃+1.5IQR`보다 큰 관측값을 표시하지만, 이것이 곧 데이터 오류나 제거 대상이라는 뜻은 아니다.

## 표준화와 분포 형태

z-score는 관측값을 평균 0·표준편차 1의 척도로 변환한다.

$$
z=\frac{x-\mu}{\sigma}\quad\text{or}\quad z=\frac{x-\bar x}{s}
$$

왜도(Skewness)는 분포의 비대칭성을 나타낸다. 오른쪽 꼬리가 긴 양의 왜도에서는 평균이 중앙값보다 커지는 경향이 있지만, 표본크기와 이상치의 영향을 고려해야 한다.

## 확률·시뮬레이션 입력과의 연결

기술통계는 [[concepts/Probability Distribution|확률분포]] 후보를 탐색하고, 도착·처리·고장 데이터의 중심과 변동을 비교하는 데 사용한다. 그러나 평균과 히스토그램만으로 확률분포를 확정할 수는 없다. 시간상관·계절성·검열·결측·측정오차를 확인한 뒤 [[concepts/Statistical Inference|통계적 추론]]과 모델 검증으로 확장한다.

## 주의와 확인 필요

- CV는 평균이 0에 가깝거나 음수일 수 있는 변수에 부적절할 수 있다.
- z-score 표준화는 이상치와 비정규성의 영향을 받으며, 학습·검증 데이터의 정보 누수를 피해야 한다.
- 이상치 규칙은 탐색 도구이지 자동 삭제 규칙이 아니다.
- 이 페이지는 기존 기술통계 학습 노트를 정제한 초안이다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/01_Mathematics/01_Statistics/Descriptive Statistics.md`

## 연결

- [[concepts/Probability Theory|확률론]]
- [[concepts/Probability Distribution|확률분포]]
- [[concepts/Statistical Inference|통계적 추론]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
