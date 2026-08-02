---
type: concept
title: "Vector Spaces and Linear Transformations"
status: draft
confidence: medium
confidence_reason: "기존 벡터공간·선형결합·span·선형독립·기저·차원·선형변환 노트를 통합했다. 추상공간의 예시와 좌표변환은 원문헌 또는 교재로 추가 확인할 수 있다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Vector Space.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Linear combination & Span.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Linear Independence.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Basis & Dimension.md"
  - "/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Linear Transformation.md"
source_vault_modified_at:
  - "2026-02-27T16:17:50+09:00"
  - "2026-02-20T19:04:14+09:00"
  - "2026-02-02T23:22:55+09:00"
  - "2026-03-03T16:17:37+09:00"
  - "2026-03-26T14:26:11+09:00"
tags:
  - linear-algebra
  - vector-space
  - basis
  - linear-transformation
  - dimension
---

# Vector Spaces and Linear Transformations

## Vector Space

벡터공간(Vector Space)은 벡터의 덧셈과 스칼라 곱이 정의되어 있고, 그 연산이 닫힘성·결합법칙·분배법칙·영벡터·역원 등의 공리를 만족하는 집합이다. 벡터는 숫자 배열뿐 아니라 함수·다항식·행렬처럼 선형결합을 정의할 수 있는 대상을 포함할 수 있다.

## Linear Combination과 Span

벡터 `v₁,…,vₖ`의 선형결합(Linear Combination)은

$$
c_1v_1+\cdots+c_kv_k
$$

형태의 벡터다. 이 모든 선형결합의 집합을 span이라고 하며, 주어진 벡터들이 생성할 수 있는 공간을 나타낸다.

선형시스템 `Ax=b`에서 `A`의 열벡터들의 span이 바로 `Col(A)`이고, `Ax`는 그 열벡터들의 계수 `x`를 사용한 선형결합이다.

## 선형독립·기저·차원

벡터 집합 `{v₁,…,vₖ}`가

$$
c_1v_1+\cdots+c_kv_k=0
$$

을 만족하는 해가 모든 `c_i=0`뿐이면 선형독립(Linear Independence)이다. 선형독립인 생성 집합을 기저(Basis)라고 하며, 기저는 공간의 모든 벡터를 유일한 좌표로 표현하게 한다.

기저 벡터의 개수는 유한차원 공간에서 항상 같으며, 그 수를 차원(Dimension)이라고 한다. 차원은 공간이 갖는 독립적인 자유 방향의 개수로 해석할 수 있다.

## Subspace와 Null Space

부분공간(Subspace)은 상위 벡터공간의 부분집합이면서 영벡터 포함·덧셈 닫힘·스칼라 곱 닫힘을 만족하는 공간이다. 원점을 지나지 않는 직선이나 평면은 일반적으로 부분공간이 아니다.

행렬 `A`에 대한 `Nul(A)`는 `Ax=0`을 만족하는 입력들의 부분공간이다. [[concepts/Linear Systems and Matrix Rank|선형시스템과 행렬 rank]]에서 정리한 것처럼 nullity는 `Nul(A)`의 차원이고 rank와 함께 입력 차원을 분해한다.

## Linear Transformation

선형변환(Linear Transformation) `L:V→W`는

$$
L(u+v)=L(u)+L(v),\qquad L(cu)=cL(u)
$$

를 만족하는 함수다.

- **Kernel `Ker(L)`**: `L(v)=0`이 되는 입력들의 공간
- **Range 또는 Image**: 실제로 도달하는 출력들의 공간
- **One-to-one**: `Ker(L)={0}`인 경우
- **Onto**: `Range(L)=W`인 경우

선형변환의 차원 정리(Rank–Nullity Theorem)는

$$
\dim Ker(L)+\dim Range(L)=\dim V
$$

이다. 이 정리는 변환이 보존하는 정보의 차원과 0으로 사라지는 자유방향을 함께 설명한다.

## 기저와 행렬 표현

입력공간의 기저 `S={v₁,…,vₙ}`와 출력공간의 기저 `T`가 주어지면, 각 `L(v_i)`를 `T`의 좌표로 표현해 열벡터로 쌓은 행렬 `A`가 선형변환을 표현한다.

$$
[L(x)]_T=A[x]_S
$$

기저변환(Transition Matrix)은 같은 벡터를 다른 좌표계로 표현하는 것이고, 선형변환의 행렬표현은 벡터를 실제로 다른 출력으로 보내는 규칙이다. 둘을 구분해야 `P^{-1}AP`와 같은 좌표변환·닮음변환을 올바르게 해석할 수 있다.

## 연구에서의 의미

벡터공간은 상태·관측·특징·정책을 좌표화하는 언어이고, 선형변환은 상태전이·투영·특징변환·제약을 표현하는 구조다. 기저를 선택하면 같은 모델을 계산하기 쉬운 좌표계로 바꿀 수 있지만, 좌표 표현과 실제 대상의 변화를 혼동하지 않는다.

## 주의와 확인 필요

- `span`은 특정 벡터들이 생성하는 공간이고, 원래 벡터들의 집합 자체와 다를 수 있다.
- 선형독립은 벡터의 개수만으로 판단할 수 없고 선형결합 방정식으로 확인한다.
- `Range(L)`와 `Col(A)`의 동일시는 특정 기저에서의 행렬 표현을 전제로 한다.
- 이 페이지는 기존 수업 노트를 통합한 초안이며 함수공간·무한차원 공간의 세부사항은 다루지 않는다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Vector Space.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Linear combination & Span.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Linear Independence.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Basis & Dimension.md`
- `/Users/Hyeyeong/Vault/01_Mathematics/02_Linear Algebra/Linear Transformation.md`

## 연결

- [[concepts/Linear Systems and Matrix Rank|선형시스템과 행렬 rank]]
- [[concepts/Eigenvalues and Quadratic Forms|고유값과 이차형식]]
- [[methods/Convex Optimization|볼록 최적화]]
- [[concepts/Stochastic Process|확률과정]]
