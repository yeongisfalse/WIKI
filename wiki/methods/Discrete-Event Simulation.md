---
type: method
title: "Discrete-Event Simulation"
status: reviewed
confidence: high
confidence_reason: "HRC 조립선과 MaaS job-shop 사례에서 설명한 이산사건 시뮬레이션의 모델 요소와 디지털트윈 활용을 통합했다."
tags:
  - discrete-event-simulation
  - simulation
  - manufacturing
  - digital-twin
sources:
  - "[[web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems]]"
  - "[[web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making]]"
---

# Discrete-Event Simulation

## 정의

이산사건 시뮬레이션(Discrete-Event Simulation, DES)은 시스템 상태가 연속적으로 매 순간 바뀐다고 가정하기보다, 도착·출발·고장·작업 완료·상태 변경과 같은 사건이 발생하는 시점에 상태를 갱신하는 시뮬레이션 방법이다.

## 제조 시스템의 모델 요소

- **Entity**: 주문, 제품, 부품, 작업물
- **Resource**: 설비, 로봇, 작업자, 작업대, 운송 장치
- **Process flow**: 작업 순서와 라우팅 규칙
- **Queue**: 자원을 기다리는 대기행렬과 재공품
- **Event**: 도착, 시작·완료, 고장·복구, 결함, 우선순위 변경
- **KPI**: makespan, 처리량, 대기시간, 활용률, 작업자 부담

## 디지털트윈에서의 사용

실제 상태의 snapshot을 시뮬레이션 초기 상태로 불러오면, 현재 운영에서 앞으로 벌어질 일을 fast-time으로 예측하거나 여러 what-if 시나리오를 비교할 수 있다. HRC 사례는 조립선의 사람·로봇·작업을 모델링했고, MaaS 사례는 재공품과 생산순서를 반영해 전략·운영 계획을 비교했다.

## 설계와 실행 체크리스트

1. 사건 목록과 상태 변수의 정의가 실제 시스템의 시간 해상도에 맞는가?
2. 처리시간, 도착, 고장, 결함의 변동과 상관관계를 기록했는가?
3. 초기 재공품과 진행 중 작업을 실제 snapshot과 일치시켰는가?
4. 반복 실행, warm-up, 난수 시드와 결과 집계 방식을 명시했는가?
5. 모델 구현 검증과 사용 맥락 타당화를 별도로 수행했는가?
6. 실시간 의사결정에 필요한 계산시간과 데이터 지연을 측정했는가?

## 장점과 한계

**장점**

- 대기, 병목, 자원 경쟁, 작업 순서와 같은 운영 상호작용을 표현하기 쉽다.
- 물리 시스템을 멈추지 않고 설계·운영 대안을 반복 비교할 수 있다.
- 디지털트윈의 what-if 분석과 시뮬레이션 기반 최적화에 적합하다.

**한계**

- 사람의 판단, 안전 행동, 예외 처리와 같은 요소는 단순 규칙으로 축약될 수 있다.
- 사건과 분포를 잘못 정의하면 결과가 그럴듯해도 실제와 달라진다.
- 매우 복잡한 모델은 실시간 운영 주기보다 오래 걸릴 수 있어 surrogate model 또는 모델 축소가 필요할 수 있다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[topics/Human-Robot Collaboration in Manufacturing|제조 인간-로봇 협업]]
- [[concepts/Uncertainty Quantification|불확실성 정량화]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]

## 근거 자료

- [[web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems]]
- [[web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making]]
