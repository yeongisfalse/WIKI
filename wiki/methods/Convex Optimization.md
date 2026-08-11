---
type: method
title: "Convex Optimization"
status: draft
confidence: medium
confidence_reason: "기존 AI 모델 최적화 수업 노트에서 목적함수·feasible set·gradient·Hessian·볼록성·라그랑지안 쌍대성의 연구용 골격을 컴파일했다. 제약 최적화의 정리와 쌍대성의 강한 조건은 원 교재로 재확인해야 한다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/03_AI/04_Optimization/Math Foundation (1).md"
source_vault_modified_at: "2026-04-19T22:30:40+09:00"
tags:
  - convex-optimization
  - optimization
  - linear-algebra
  - mathematical-foundation
---

# Convex Optimization

## 빠른 이해

- 볼록 최적화는 목적함수와 feasible set이 볼록한 문제를 다루며, 국소 최적해가 전역 최적해가 된다는 강한 구조적 장점이 있다.
- gradient·Hessian은 곡률과 이동 방향을, KKT 조건과 duality는 제약조건이 최적해에 미치는 영향과 하한을 설명한다.
- 실제 문제에서 볼록성은 자동으로 보장되지 않는다. 변수 변환, 비선형 제약, 정수 변수, 시뮬레이터 내부의 불연속성이 있으면 다른 방법이나 근사 검토가 필요하다.

## 문제의 기본 구조

최적화(Optimization)는 결정변수 `x` 중 목적함수(Objective Function)를 최소화 또는 최대화하면서 제약조건을 만족하는 해를 찾는 문제다.

$$
\min_{x\in\Omega} f(x)
$$

- `x`: 결정변수
- `f(x)`: 목적함수
- `Ω`: 제약조건을 만족하는 feasible set

디지털트윈 연구에서는 작업순서·자원배치·설비 수·정책 파라미터가 결정변수가 될 수 있고, 처리시간·비용·품질·안전·ergonomics가 목적 또는 제약이 될 수 있다.

## 선형대수와 최소제곱

선형 시스템 `Ax=b`는 모델의 상태·관측·제약을 표현하는 기본 형태다. 정확한 해가 없거나 과결정 시스템이면 최소제곱(Least Squares)을 사용해 잔차 제곱합을 줄인다.

$$
\min_x \|b-Ax\|_2^2
$$

정규방정식(Normal Equation)은

$$
A^TAx=A^Tb
$$

의 형태로 나타난다. 실제 계산에서는 `AᵀA`를 직접 구성할 때 수치조건이 나빠질 수 있으므로, 연구 구현에서는 QR 분해나 SVD 등 수치적으로 안정적인 방법을 검토해야 한다.

## 미분과 곡률

- 기울기(Gradient) `∇f(x)`는 함수값이 가장 빠르게 증가하는 방향을 나타낸다.
- 헤시안(Hessian) `∇²f(x)`은 국소 곡률을 표현한다.
- 2차 Taylor 근사는 현재 점 주변에서 함수의 변화와 곡률을 설명한다.

제약이 없는 내부점에서 미분 가능한 함수가 국소 최솟값을 가지면 `∇f(x*)=0`이 필요조건이다. 두 번 미분 가능하면 헤시안이 양의 준정부호(Positive Semidefinite, PSD)라는 조건이 추가적인 2차 필요조건이 된다. 충분조건과 제약조건이 있는 경우에는 함수의 정칙성·경계·활성 제약을 별도로 확인해야 한다.

## 볼록성

집합 `Ω`가 두 점을 잇는 모든 선분을 포함하면 볼록집합(Convex Set)이다. 함수 `f`가

$$
f(\theta x+(1-\theta)y)\leq \theta f(x)+(1-\theta)f(y),\quad 0\leq\theta\leq1
$$

을 만족하면 볼록함수(Convex Function)다.

미분 가능한 볼록함수에서는 `∇f(x*)=0`인 점이 전역 최솟값이다. 따라서 국소 최적해와 전역 최적해의 차이가 작아지고, 해석·알고리즘 설계가 상대적으로 쉬워진다. 반대로 시뮬레이션 기반 목적함수는 잡음·불연속·비볼록성을 가질 수 있어, 이 이론을 그대로 적용하기 전에 목적함수의 구조를 확인해야 한다.

## 라그랑지안과 쌍대성

제약식 `g_i(x)≤0`, `h_j(x)=0`을 가진 문제에서는 라그랑지안(Lagrangian)을 사용해 목적함수와 제약을 승수와 함께 표현한다.

$$
L(x,u,v)=f(x)+\sum_i u_i g_i(x)+\sum_j v_j h_j(x),\qquad u_i\geq0
$$

`x`에 대한 하한을 취하면 듀얼 함수(Dual Function)를 얻고, 이를 최대화하는 듀얼 문제를 구성할 수 있다. 듀얼 문제의 해는 원문제 최적값에 대한 하한을 제공한다(약한 쌍대성). 원문제와 듀얼 문제의 최적값이 일치하는 강한 쌍대성은 볼록성·feasibility·Slater 조건과 같은 추가 가정이 필요하다.

## 시뮬레이션 기반 최적화와의 구분

볼록 최적화는 목적함수와 제약의 수학적 구조를 이용한다. 반면 [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]는 시뮬레이션을 실행해야 목적함수를 평가할 수 있고, 평가 잡음·확률 입력·계산비용을 다룬다. 둘은 배타적이지 않다.

- 시뮬레이션이 매끄럽고 볼록한 대리 목적함수를 제공하면 경사 기반 방법을 사용할 수 있다.
- 목적함수가 불연속·블랙박스·잡음성이면 메타휴리스틱, 순차적 실험, surrogate model 등을 검토할 수 있다.
- 어느 경우에도 실제 시스템의 제약, 모델 검증·타당화, 불확실성을 최적화 알고리즘과 분리하지 않는다.

## 주의와 확인 필요

- 원본 수업 노트는 선형대수·미분·볼록 최적화·쌍대성을 한 페이지에 묶은 학습 자료다. 이 페이지는 연구 연결에 필요한 골격만 추출했다.
- 최적성 조건은 제약 여부와 정칙성에 따라 달라진다. `∇f=0`을 모든 최적화 문제의 해법으로 해석하면 안 된다.
- 원본 노트에는 KKT 조건과 수치 최적화 알고리즘의 상세 검토가 없으므로, 해당 내용을 연구에 사용할 때는 별도 페이지로 보강해야 한다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/03_AI/04_Optimization/Math Foundation (1).md`

## 연결

- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[methods/Surrogate Modeling|surrogate model]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]
