---
type: web
title: "Transitioning trends into action: A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making"
authors:
  - "Romão Santos"
  - "Henrique Piqueiro"
  - "Rui Dias"
  - "Cláudia D. Rocha"
journal: "Computers & Industrial Engineering"
published: "2024"
volume: 198
article_number: "110616"
doi: "10.1016/j.cie.2024.110616"
source: "https://www.sciencedirect.com/science/article/pii/S0360835224007381"
site: "Elsevier / ScienceDirect"
raw_file: "[[raw/web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making]]"
captured_at: "2026-08-01T23:31:46+09:00"
status: draft
confidence: high
confidence_reason: "Computers & Industrial Engineering의 peer-reviewed 연구이며, DOI·저자·권호·article number와 FlexSim 기반 산업 실험 본문을 확인했다. 사례는 특정 MaaS 공급자와 dynamic job-shop에 한정된다."
tags:
  - digital-twin
  - simulation-based-optimization
  - decision-support
  - manufacturing-as-a-service
  - job-shop-scheduling
---

# Transitioning trends into action: A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making

## 핵심 내용

이 연구는 제조 운영에서 전략적·운영적 의사결정을 지원하는 simulation-based DT 아키텍처를 제안하고, Manufacturing-as-a-Service(MaaS) 공급자의 dynamic job-shop 사례에 적용한다. 실시간 생산 상태를 DT에 적재하고, 시뮬레이션으로 대안을 평가한 뒤, 최적화된 생산계획을 실제 시스템에 되돌려 보내는 구조다.

## 아키텍처 구성

- **IoT platform**: Message Broker, Protocol Adapter, Thing/Service Registry, Data Store와 API Gateway로 이기종 장치의 실시간 이벤트를 중계한다.
- **Advanced Plant Model(APM)**: 작업자·로봇·설비·workstation·물류 자원을 포함한 공장 상태의 동적 표현이며 MES와 연동한다.
- **Simulation model**: FlexSim 2023의 3D discrete-event simulation으로 WIP snapshot과 시나리오를 불러온다.
- **Optimization**: OptQuest가 생산 순서와 자원 배치를 탐색하며, 주요 목적은 sequence-dependent setup이 있는 job-shop의 makespan 최소화다.
- **현장 기술**: AGV/AMR, mobile programmable cobot(MPC), robotic manipulator, 3D printing과 Task Manager를 연결한다.

## 연구 설계 및 사례

- 전략 단계에서는 MPC 수와 생산계획을 여러 replication으로 비교하고, 운영 단계에서는 실시간 WIP·결함 정보를 바탕으로 schedule을 재계산한다.
- 산업 실험은 다양한 제품을 조립하는 MaaS supplier의 dynamic job-shop이다.
- 논문은 2대와 3대 MPC를 비교한 결과에서 MPC 수 증가에 따른 makespan 감소와 약 30%의 예상 이득을 보고한다.
- 50개 생산 주문의 scheduling에서는 OptQuest를 1,000 iterations·10,000초 wall time 조건으로 실행했고, 시뮬레이션–APM–현장 통신과 KPI(예: makespan, robot/operator utilization)를 확인했다.

## 출처와 맥락

- 저자: Romão Santos, Henrique Piqueiro, Rui Dias, Cláudia D. Rocha
- 저널: *Computers & Industrial Engineering*, 198, 110616 (2024)
- 이 연구는 DT를 단순 모니터링 모델이 아니라 **실시간 상태 → 시뮬레이션 → 최적화 → 실행계획**의 운영 의사결정 인프라로 구현한다.

## 신뢰도와 근거

- 평가: `high`
- 근거: Elsevier 서지정보와 DOI, 논문의 시스템 구성·FlexSim/OptQuest 설정·산업 실험 절차를 확인했다.
- 범위 주의: makespan 개선은 특정 제품·자원·시나리오의 실험 결과이며, 다른 공정이나 최적화 목적에 일반화하려면 추가 실험이 필요하다.

## 혜영님의 연구와의 관련성

- 혜영님이 원하는 “DT 지식–시뮬레이션–최적화–현장 되먹임” 구조를 구체적인 모듈과 데이터 흐름으로 보여준다.
- 전략적 설비 도입과 운영적 schedule 재계산을 같은 simulation model에 넣어, 시간 규모가 다른 최적화 문제를 한 아키텍처에서 연결하는 사례다.
- 연구 아이디어로는 `[[ideas/Integrated Digital Twin Optimization Loop]]`의 아키텍처 후보와 비교하고, WIP·불확실성·결함을 최적화 문제의 상태 입력으로 명시할 수 있다.

## 한계와 확인 필요

- 데이터 품질·가용성, 보안·개인정보, DT 유지보수·업데이트가 주요 제한으로 남는다.
- 사례는 MaaS supplier의 하나의 dynamic job-shop에 기반하며, 최적화 알고리즘 자체의 일반 우월성을 검증한 연구는 아니다.
- 약 30% 이득은 논문이 보고한 특정 실험 조건의 결과이며, 목표·자원·복제 수가 바뀌면 달라질 수 있다.

## 연결 후보

- [[concepts/Digital Twin]] — Digital Model·Digital Shadow·DT 구분과 동기화
- [[methods/Simulation-based Optimization]] — FlexSim·OptQuest·makespan 최소화
- [[methods/Discrete-Event Simulation]] — WIP 기반 시나리오 평가
- [[concepts/Decision Support System]] — 전략·운영 의사결정의 통합
- [[concepts/Interoperability]] — IoT platform, MQTT/OPC-UA/ROS, API·메시지 브로커
- [[ideas/Integrated Digital Twin Optimization Loop]] — 실시간 최적화 아키텍처 후보

## 원문 및 출처

- [ScienceDirect 공식 논문 페이지](https://www.sciencedirect.com/science/article/pii/S0360835224007381)
- [DOI: 10.1016/j.cie.2024.110616](https://doi.org/10.1016/j.cie.2024.110616)
- 원문 캡처: [[raw/web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making]]
