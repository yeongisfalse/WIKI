---
type: topic
title: "Human-Robot Collaboration in Manufacturing"
status: reviewed
confidence: high
confidence_reason: "FELICE 자동차 조립라인 case study를 중심으로 인간-로봇 협업 디지털트윈의 시스템 구성과 연구 질문을 정리했다. 결과는 특정 조립라인과 KPI에 한정된다."
tags:
  - human-robot-collaboration
  - manufacturing
  - digital-twin
  - ergonomics
  - assembly
sources:
  - "[[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]"
  - "[[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]"
---

# Human-Robot Collaboration in Manufacturing

## 빠른 이해

- 인간-로봇 협업 제조는 사람과 로봇이 같은 공정의 작업·자원·공간을 공유하면서 생산성·안전·ergonomics를 함께 고려하는 주제다.
- 디지털트윈은 실제 조립선 상태를 모델과 Digital Mirror에 반영하고, 작업 할당·배치·workflow 후보를 what-if로 비교하는 분석 환경을 제공한다.
- 생산시간 하나만 줄이는 해는 사람의 피로·자세·안전 제약을 악화시킬 수 있으므로, KPI의 충돌과 허용 가능한 trade-off를 명시해야 한다.

## 주제의 중심 질문

사람과 로봇이 함께 작업하는 제조 시스템에서 디지털트윈과 시뮬레이션을 이용해 작업 배치·작업 할당·안전·생산성을 어떻게 함께 개선할 것인가?

## 사례 아키텍처

| 구성요소 | 역할 |
| --- | --- |
| Digital Model | AnyLogic 기반 이산사건 시뮬레이션과 Real-Time Virtual Simulation으로 조립선의 작업·자원·이벤트를 표현 |
| Digital Mirror | 실제 조립선의 현재 이벤트와 상태를 3차원으로 반영 |
| Orchestrator | 사용자의 what-if 요청 또는 자동 시나리오 요청을 시뮬레이션에 전달 |
| 데이터 교환 | FIWARE/FIROS, NGSIv2 JSON 메시지, 사용자 정의 Java 라이브러리 |
| KPI | 조립시간, 생산성, 활용률, 작업자 ergonomics 등 |

## 연구 설계의 핵심

- 실제 자동차 front-door 조립라인 3개 workstation을 대상으로 한다.
- 사람·로봇·작업을 포함한 agent-based/discrete-event 모델이 실시간 상태와 8시간 앞의 fast-time what-if 실험을 지원한다.
- 작업 순서와 로봇이 맡을 수 있는 micro-operation 조합을 비교한다.
- 로봇 참여에 따른 조립시간 변화만으로 결론을 내리지 않고 생산성·활용률·ergonomics를 함께 본다.

## 연구 질문

- 작업자의 숙련도, 피로, 안전 제약을 어떻게 모델에 표현할 것인가?
- 작업 할당의 생산성 향상과 ergonomics 개선이 충돌할 때 어떤 기준으로 선택할 것인가?
- 실제 현장 데이터와 시뮬레이션 모델 사이의 동기화 지연이 의사결정에 미치는 영향은 무엇인가?
- 이산사건 모델과 실시간 3차원 Digital Mirror 사이의 상태·의미 불일치를 어떻게 검증할 것인가?

## 주제 범위와 비교 기준

이 주제에서 시스템 경계는 사람·로봇·작업·공정·공간·안전 규칙을 포함하는지에 따라 달라진다. 단순히 로봇이 작업을 수행한다는 사실보다, 누가 어떤 micro-operation을 어떤 순서와 조건에서 수행하고 그 결과가 다음 상태에 어떻게 영향을 주는지를 모델링해야 한다.

사례를 비교할 때는 작업 할당 방식, 자원 공유 규칙, 작업자 상태 표현, 실시간 데이터의 지연·결측 처리, KPI와 제약조건, 실제 실행으로 연결되는 승인 절차를 기록한다. 생산성·활용률·조립시간·ergonomics가 같은 단위와 시간 범위로 측정되지 않으면 숫자의 직접 비교를 피한다.

## 대표 쟁점과 연구 공백

- 작업자 피로·숙련도·자세·안전 위험을 시뮬레이션 상태와 관측 데이터로 어떻게 연결할 것인가?
- 생산성 향상과 인간 중심 지표가 충돌할 때 Pareto front, 제약조건, lexicographic rule 중 어떤 의사결정 기준을 사용할 것인가?
- Digital Model과 Digital Mirror가 서로 다른 시간 해상도와 의미 체계를 사용할 때 상태 일관성을 어떻게 검증할 것인가?
- 추천된 작업 배치를 실제 현장에 적용한 뒤 예측과 결과의 차이를 어떻게 재학습·재검증할 것인가?

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]
- [[concepts/Interoperability|상호운용성]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[topics/Digital Twin in Smart Manufacturing|스마트 제조 디지털트윈]]

## 근거 자료

- [[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]
