---
type: concept
title: "Linear Systems and Matrix Rank"
status: draft
confidence: medium
confidence_reason: "기존 선형시스템·연립방정식 풀이·행공간·열공간·영공간·행렬식·가역행렬 노트의 공통 구조를 통합했다. 수치해석 관점의 안정성과 대규모 계산은 별도 검토가 필요하다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Linear Systems.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Solving Linear Systems.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Row Space & Column Space.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Subspace & Null space.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Non-Singular Matrix.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Determinants.md"
source_vault_modified_at:
  - "2026-02-02T23:15:39+09:00"
  - "2026-02-02T23:22:55+09:00"
  - "2026-03-03T12:59:55+09:00"
  - "2026-02-27T16:21:38+09:00"
  - "2026-03-05T13:12:44+09:00"
  - "2026-02-20T20:14:35+09:00"
tags:
  - linear-algebra
  - linear-system
  - matrix-rank
  - null-space
  - optimization
---

# Linear Systems and Matrix Rank

## 선형시스템

선형시스템(Linear System)은 같은 변수에 대한 선형방정식들의 모음이다. 행렬과 벡터를 사용하면

$$
Ax=b
$$

로 표현할 수 있다.

- `A`: 계수행렬
- `x`: 결정변수 또는 상태벡터
- `b`: 관측값·요구량·우변 벡터
- `[A\mid b]`: 확장행렬(Augmented Matrix)

동차 시스템(Homogeneous System)은 `b=0`인 경우다. 항상 `x=0`이라는 trivial solution을 가지며, 비자명해가 존재하는지는 `A`의 열 사이 선형종속성과 rank에 달려 있다.

## 기본 행 연산과 RREF

기본 행 연산(Elementary Row Operations)은 해집합을 보존하면서 시스템을 변환한다.

1. 두 행을 교환한다.
2. 한 행에 0이 아닌 스칼라를 곱한다.
3. 한 행에 다른 행의 스칼라배를 더한다.

이 연산으로 행렬을 Row Echelon Form 또는 Reduced Row Echelon Form으로 바꾸면 pivot과 free variable이 드러난다. 행 동치(Row Equivalence)인 두 시스템은 같은 해집합을 갖는다.

## 해의 존재와 개수

`A`의 열 개수를 `n`이라고 할 때 다음 기준을 사용한다.

- **No solution**: `rank(A) < rank([A\mid b])`
- **Unique solution**: `rank(A)=rank([A\mid b])=n`
- **Infinitely many solutions**: `rank(A)=rank([A\mid b])<n`

`m<n`이라고 해서 모든 비동차 시스템이 항상 무수히 많은 해를 갖는 것은 아니다. 해가 존재한다면 자유변수가 생겨 무수히 많은 해를 갖지만, `b`가 `Col(A)` 밖에 있으면 해가 없다. 이 구분은 원본 노트의 underdetermined 설명을 더 정확하게 정리한 것이다.

## Fundamental Subspaces와 Rank

`A`가 `m×n` 행렬일 때

- **Column Space `Col(A)`**: 열벡터들의 span. `Ax=b`가 풀릴 필요충분조건은 `b∈Col(A)`다.
- **Row Space `Row(A)`**: 행벡터들의 span.
- **Null Space `Nul(A)`**: `Ax=0`의 모든 해. `Rⁿ`의 부분공간이다.
- **Rank**: `Col(A)` 또는 `Row(A)`의 차원. 두 차원은 항상 같다.
- **Nullity**: `Nul(A)`의 차원.

Rank–Nullity Theorem은

$$
rank(A)+nullity(A)=n
$$

을 말한다. rank는 입력 차원 중 출력에 영향을 주는 독립 방향의 수이고, null space는 변환에서 사라지거나 제약식이 구분하지 못하는 자유 방향이다.

## 가역성과 행렬식

정방행렬 `A`에 대해 다음 조건은 서로 동치다.

- `A`가 invertible 또는 nonsingular이다.
- `det(A)≠0`이다.
- `rank(A)=n`이다.
- `Nul(A)={0}`이다.
- `Ax=0`은 trivial solution만 갖는다.
- 모든 `b`에 대해 `Ax=b`가 유일해를 갖는다.

행렬식(Determinant)은 선형변환이 부피를 얼마나 배율 조정하는지와 관련된 스칼라다. `det(A)=0`이면 어떤 방향이 collapse되어 차원과 정보가 손실되고 역변환을 만들 수 없다.

## 최적화·데이터 모델에서의 의미

선형시스템은 자원 제약, 상태방정식, 관측식, 회귀·최소제곱 문제의 기본 표현이다. `Nul(A)`의 방향은 제약 `Ax=b`를 유지하면서 해를 움직일 수 있는 자유도이고, rank 결핍은 변수 중복·식별 불가능성·다중공선성과 연결될 수 있다.

정확한 해가 없을 때는 최소제곱 문제

$$
\min_x\|Ax-b\|_2^2
$$

를 고려한다. 정규방정식은 `AᵀAx=Aᵀb`이지만, 실제 계산에서 `AᵀA`를 직접 만드는 것이 수치적으로 불리할 수 있으므로 QR 분해·SVD와 조건수(condition number)를 함께 검토한다.

## 주의와 확인 필요

- `rank(A)=rank([A|b])<n`은 무수히 많은 해를 뜻하고, rank가 다르면 해가 없다는 점을 구분한다.
- `A^{-1}b`는 정방·가역 시스템의 표현이며, 모든 선형시스템을 역행렬로 푸는 계산법을 의미하지 않는다.
- 행 연산은 행공간과 해집합을 보존하지만 원래 행렬의 열공간 벡터 자체는 바꾼다. 열공간의 기저는 RREF의 pivot 열 위치를 참고해 원본 `A`에서 가져온다.
- 이 페이지는 수업 노트를 통합한 초안이며 대규모 희소 시스템·수치 안정성은 별도 방법론으로 보강해야 한다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Linear Systems.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Solving Linear Systems.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Row Space & Column Space.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Subspace & Null space.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Non-Singular Matrix.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Determinants.md`

## 연결

- [[concepts/Vector Spaces and Linear Transformations|벡터공간과 선형변환]]
- [[concepts/Eigenvalues and Quadratic Forms|고유값과 이차형식]]
- [[methods/Convex Optimization|볼록 최적화]]
- [[concepts/Statistical Inference|통계적 추론]]
