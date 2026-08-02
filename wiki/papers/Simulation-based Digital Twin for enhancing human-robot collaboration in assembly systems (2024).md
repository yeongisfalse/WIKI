---
type: paper
content_type: research_article
title: "Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems"
authors:
  - "Antonio Cimino"
  - "Francesco Longo"
  - "Letizia Nicoletti"
  - "Vittorio Solina"
journal: "Journal of Manufacturing Systems"
published: "2024"
volume: 77
pages: "903–918"
doi: "10.1016/j.jmsy.2024.10.024"
source: "https://www.sciencedirect.com/science/article/pii/S0278612524002504"
site: "Elsevier / ScienceDirect"
raw_file: "[[raw/web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems]]"
captured_at: "2026-08-01T23:31:17+09:00"
status: draft
confidence: high
confidence_reason: "Journal of Manufacturing Systems의 peer-reviewed 연구이며, Elsevier 공식 페이지·DOI·저자·권호·페이지와 자동차 조립라인 case study 본문을 확인했다. 결과는 특정 FELICE 실증 맥락에 한정된다."
tags:
  - digital-twin
  - human-robot-collaboration
  - discrete-event-simulation
  - interoperability
  - assembly-systems
---

# Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems

## 핵심 내용

이 연구는 인간-로봇 협업(HRC) 조립 시스템을 개선하기 위한 simulation-based DT를 설계하고 자동차 조립라인 case study로 시험·검증한다. DT가 실시간 데이터를 받아 조립선의 여러 작업 배치와 인간·로봇 task allocation을 빠르게 비교하고, 생산성·작업자 ergonomics KPI를 기준으로 의사결정을 지원하도록 구성했다.

## 시스템 구성

- **Digital Model**: AnyLogic 기반의 discrete-event simulation(DES)과 Real-Time Virtual Simulation(RTVS)
- **Digital Mirror**: 실제 조립선의 현재 이벤트를 3D로 반영하는 Interactive Virtual Reality Environment(IVRE)
- **Orchestrator 연동**: 사용자가 수동으로 실행하거나, orchestrator가 자동으로 what-if 시나리오를 요청할 수 있다.
- **데이터 교환**: FIWARE/FIROS와 NGSIv2 JSON 메시지, 사용자 정의 Java 라이브러리로 DES와 외부 시스템 사이의 publish/subscribe 통신을 구현했다.

## 연구 설계 및 사례

- EU Horizon 2020 FELICE 프로젝트의 자동차 front-door 조립라인(3개 workstation)을 대상으로 한다.
- DES는 사람·로봇·작업을 포함한 agent-based/discrete-event 모델이며, 실시간 데이터와 8시간 앞의 fast-time what-if 실험을 지원한다.
- workstation 10의 사례에서는 macro-operation 순서 2가지와 로봇이 맡을 수 있는 5개 micro-operation을 조합해 64개 workflow를 비교했다.
- 원문 표의 세 반복 실험에서 모든 5개 지원 작업에 로봇이 참여한 경우 assembly time이 수동 기준보다 약 4.4–4.6% 감소했다. 최종 workflow 선택은 productivity·utilization·ergonomics 등 다른 KPI와 함께 판단해야 한다.

## 출처와 맥락

- 저자: Antonio Cimino, Francesco Longo, Letizia Nicoletti, Vittorio Solina
- 저널: *Journal of Manufacturing Systems*, 77, 903–918 (2024)
- 연구의 주된 기여는 새 최적화 알고리즘보다 **시뮬레이션 기반 DT의 실증·모듈화·상호운용성**에 있다.

## 신뢰도와 근거

- 평가: `high`
- 근거: Elsevier 공식 서지정보와 DOI, 본문에 기술된 FELICE 자동차 조립라인 case study 및 반복 실험을 확인했다.
- 범위 주의: 결과는 특정 조립라인·모델·KPI에 대한 것이며, 다른 HRC 환경에 그대로 일반화할 수 없다.

## 혜영님의 연구와의 관련성

- 최적화 전에 DES로 task allocation과 layout/workflow 후보를 빠르게 평가하는 **simulation–decision loop** 사례다.
- DT의 구성요소를 Digital Model, Digital Mirror, orchestrator로 분리해 연구 주제의 시스템 경계를 설계하는 데 참고할 수 있다.
- 생산성만이 아니라 ergonomics를 KPI로 함께 둔 점은 다목적 최적화와 인간 중심 제조 연구로 확장할 수 있는 연결점이다.

## 한계와 확인 필요

- 실제 사례는 자동차 조립라인과 FELICE 플랫폼에 집중되어 있다.
- 본문은 DES 모듈의 구현과 what-if 평가에 초점을 두며, 전체 orchestrator의 의사결정 로직은 범위 밖이다.
- 4.4–4.6% assembly-time 감소는 특정 workflow·세 번의 반복 결과이며, 통계적 일반화로 해석하지 않는다.

## 연결 후보

- [[concepts/Digital Twin]] — Digital Model·Digital Mirror·실시간 동기화
- [[methods/Discrete-Event Simulation]] — fast-time what-if 분석
- [[concepts/Interoperability]] — FIWARE/FIROS, NGSIv2, 외부 시스템 연동
- [[topics/Human-Robot Collaboration in Manufacturing]] — HRC task allocation과 ergonomics KPI
- [[methods/Simulation-based Optimization]] — KPI 기반 workflow 선택과 최적화 연결

## 원문 및 출처

- [ScienceDirect 공식 논문 페이지](https://www.sciencedirect.com/science/article/pii/S0278612524002504)
- [DOI: 10.1016/j.jmsy.2024.10.024](https://doi.org/10.1016/j.jmsy.2024.10.024)
- 원문 캡처: [[raw/web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems]]
