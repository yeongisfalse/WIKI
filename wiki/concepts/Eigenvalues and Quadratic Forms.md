---
type: concept
title: "Eigenvalues and Quadratic Forms"
status: draft
confidence: medium
confidence_reason: "기존 고유값·고유벡터·대각화·닮음·직교성·이차형식 노트에서 스펙트럼 구조와 부호성의 공통 내용을 통합했다. 수치 고유값 계산과 PCA·공분산의 응용은 별도 검증이 필요하다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Eigenvector & Eigenvalue.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Diagonalization.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Quadratic Form.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Orthogonal Vectors & Matrix.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Similarity.md"
source_vault_modified_at:
  - "2026-03-26T12:51:03+09:00"
  - "2026-03-26T18:54:45+09:00"
  - "2026-03-27T00:35:51+09:00"
  - "2026-03-26T19:57:47+09:00"
  - "2026-03-26T13:16:34+09:00"
tags:
  - linear-algebra
  - eigenvalue
  - diagonalization
  - quadratic-form
  - positive-definite
---

# Eigenvalues and Quadratic Forms

## 고유값과 고유벡터

정방행렬 또는 선형연산자 `A`의 고유값(Eigenvalue) `λ`와 고유벡터(Eigenvector) `v≠0`는

$$
Av=\lambda v
$$

를 만족한다. 고유벡터가 span하는 방향은 변환 뒤에도 같은 1차원 부분공간에 남고, 고유값은 그 방향의 크기와 방향을 바꾸는 배율이다. `λ<0`이면 직선 위에서 방향이 뒤집히고, `λ=0`이면 해당 방향이 영벡터로 collapse된다.

고유값은 특성방정식

$$
\det(A-\lambda I)=0
$$

으로 찾고, 각 `λ`에 대해 `(A-λI)v=0`을 풀어 고유공간을 구한다. `λ=0`의 고유공간은 `Nul(A)`와 같다.

## Similarity와 Diagonalization

닮음변환(Similarity)은 가역행렬 `P`에 대해

$$
B=P^{-1}AP
$$

로 표현되는 관계다. 닮은 행렬은 같은 선형연산자를 다른 기저에서 표현한 것으로 볼 수 있으며, 고유값·행렬식·특성다항식과 같은 구조적 성질을 공유한다.

`A`가 `n`개의 선형독립인 고유벡터를 가지면 대각화(Diagonalization)가 가능하다.

$$
A=PDP^{-1}
$$

여기서 `P`의 열은 고유벡터이고 `D`의 대각원소는 고유값이다. 대각화는 행렬의 거듭제곱·선형동역학·반복 계산을 단순화하지만, 모든 행렬이 대각화 가능한 것은 아니다. 고유벡터가 공간의 기저를 만들 만큼 충분한지 확인해야 한다.

## Inner Product와 Orthogonality

내적(Inner Product)은 두 벡터의 유사한 방향과 크기를 측정한다.

$$
u^Tv=\|u\|\|v\|\cos\theta
$$

`uᵀv=0`이면 두 벡터는 직교(Orthogonal)하고, 직교하면서 각 벡터의 norm이 1이면 정규직교(Orthonormal)다. 직교행렬 `Q`는

$$
Q^TQ=QQ^T=I
$$

를 만족하며 길이·각도·내적을 보존하고 `Q^{-1}=Q^T`이다.

실수 대칭행렬은 스펙트럼 정리(Spectral Theorem)에 따라 직교 대각화할 수 있다.

$$
A=Q\Lambda Q^T
$$

## Quadratic Form과 Definiteness

이차형식(Quadratic Form)은 대칭행렬 `A`를 사용해

$$
q(x)=x^TAx
$$

로 표현되는 함수다. 대칭이 아닌 `A`도 이 식에서는 대칭 부분만 기여하므로, 부호성을 분석할 때 대칭행렬을 사용한다.

대칭행렬의 고유값 부호에 따라 다음을 분류한다.

| 분류 | 조건 | 기하·최적화 해석 |
| --- | --- | --- |
| Positive Definite | 모든 `λᵢ>0` | 모든 비영벡터 방향에서 양수, 엄격한 곡률 |
| Positive Semidefinite | 모든 `λᵢ≥0` | 평평한 방향을 허용하는 비음수 곡률 |
| Negative Definite | 모든 `λᵢ<0` | 음의 곡률 |
| Negative Semidefinite | 모든 `λᵢ≤0` | 평평한 방향을 허용하는 비양수 곡률 |
| Indefinite | 양·음 고유값이 함께 존재 | 방향에 따라 부호가 바뀌는 안장 구조 |

`x=Qy`로 좌표를 바꾸면

$$
x^TAx=y^T\Lambda y=\sum_i\lambda_i y_i^2
$$

가 되어 교차항 없이 고유방향별 곡률을 볼 수 있다.

### Positive Definiteness와 이차 최적화

대칭행렬 `H`를 사용하는 무제약 이차함수

$$
f(x)=\frac12x^THx+g^Tx+c,
\qquad x\in\mathbb{R}^n
$$

에서 `H`가 양의 정부호이면 `f`는 엄격히 볼록(strictly convex)이고 유일한 전역최솟값을 갖는다. 그 점은

$$
x^*=-H^{-1}g
$$

이며, `H`가 음의 정부호이면 같은 형태의 함수가 유일한 전역최댓값을 갖는다. 순수한 이차형식 `q(x)=x^THx`에서는 각각 `x=0`이 유일한 전역최솟값·최댓값이다.

이 결론은 목적함수의 형태와 정의역에 의존한다. 양의 준정부호는 볼록성(convexity)을 보장하지만 평평한 방향 때문에 최적해가 유일하지 않을 수 있다. `H`가 양의 정부호이고 feasible region이 비어 있지 않은 닫힌 볼록집합이면, 이 이차함수는 그 집합에서 최솟값을 가지며 엄격한 볼록성 때문에 최솟값은 유일하다. 정의역이 닫혀 있지 않거나 feasible region이 비볼록이면 최적해의 존재·유일성을 별도로 확인해야 한다. 반대로 Hessian이 한 점에서만 양의 정부호라는 사실은 일반적으로 전역최적해를 보장하지 않는다.

## 최적화와 데이터 분석에서의 사용

두 번 미분 가능한 목적함수의 헤시안(Hessian) `H`는 국소 곡률을 표현한다. gradient가 0인 정지점에서 `H`의 부호성을 보면 local minimum·maximum·saddle point를 판별하는 기준을 만들 수 있다. 볼록 최적화에서 양의 준정부호 Hessian은 중요한 구조적 조건이지만, 제약·경계·수치오차를 별도로 검토해야 한다.

공분산행렬은 데이터의 퍼짐·상관 구조를 나타내며 고유벡터는 변동이 큰 방향을, 고유값은 그 방향의 분산 크기를 나타낼 수 있다. 따라서 PCA와 타원형 데이터 분포의 해석에 연결되지만, 공분산행렬의 고유분해와 `Σ^{-1}`을 사용하는 Mahalanobis 거리의 역할은 구분한다.

## 주의와 확인 필요

- 고유벡터가 충분하지 않으면 대각화가 불가능하며, 중복 고유값만으로 대각화 가능성을 판단할 수 없다.
- `A=QΛQᵀ`는 실수 대칭행렬에 대한 결과다. 일반 행렬에는 같은 형태를 무조건 적용하지 않는다.
- 고유값이 모두 양수라는 조건과 Positive Definite의 동치는 실수 대칭행렬에 대한 주장이다. 일반 비대칭행렬은 대칭 부분과 이차형식을 기준으로 판단한다.
- Positive Definite는 위에서 명시한 무제약 이차함수의 경우 유일한 전역 최솟값을 보장한다. 다른 최적화 문제에서는 목적함수·정의역·제약조건을 함께 확인한다.
- 이 페이지는 기존 선형대수 수업 노트를 통합한 초안이며, 수치 고유값 알고리즘·조건수·PCA 구현은 별도 검토가 필요하다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Eigenvector & Eigenvalue.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Diagonalization.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Quadratic Form.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Orthogonal Vectors & Matrix.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Similarity.md`

## 연결

- [[concepts/Linear Systems and Matrix Rank|선형시스템과 행렬 rank]]
- [[concepts/Vector Spaces and Linear Transformations|벡터공간과 선형변환]]
- [[methods/Convex Optimization|볼록 최적화]]
- [[concepts/Probability Theory|확률론]]
