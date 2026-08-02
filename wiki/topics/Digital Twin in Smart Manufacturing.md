---
type: topic
title: "Digital Twin in Smart Manufacturing"
status: draft
confidence: high
confidence_reason: "스마트 제조 디지털트윈 문헌 연구의 분류 축을 중심으로, 후속 사례 연구와 연결한 주제 지도다. 원문 분석 범위는 Scopus·영어·engineering·2003–2020 문헌으로 제한된다."
tags:
  - digital-twin
  - smart-manufacturing
  - manufacturing-systems
  - research-map
sources:
  - "[[web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing]]"
  - "[[web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems]]"
  - "[[web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making]]"
---

# Digital Twin in Smart Manufacturing

## 주제의 중심 질문

스마트 제조에서 디지털트윈을 어느 제품 수명주기 단계와 제조 계층에 적용하고, 어떤 기능과 의사결정으로 연결할 것인가?

## 세 축 지도

### 1. 제품 수명주기 관리 축

| 단계 | 디지털트윈의 질문 |
| --- | --- |
| 개념 생성·설계 | 요구사항과 설계안이 어떤 결과를 낼 것인가? |
| 제조 | 현재 생산 상태와 병목은 무엇이며 어떻게 개선할 것인가? |
| 운송·판매 | 제품과 물류 흐름을 어떻게 추적하고 조정할 것인가? |
| 사용·서비스 | 실제 사용 상태와 성능 저하를 어떻게 예측할 것인가? |
| 재활용·폐기 | 제품 데이터와 자원을 다음 주기로 어떻게 연결할 것인가? |

### 2. 제조 계층 축

RAMI 4.0의 계층을 제조 맥락에서 단순화하면 다음과 같이 읽을 수 있다.

| 계층 | 제조 대상의 예 |
| --- | --- |
| Product | 생산할 제품과 부품 |
| Machine / Field device | 설비, 센서, 로봇, 이동 장치 |
| Process / Station / Work unit | 공정, 작업대, 작업 단위 |
| Factory / Enterprise | 공장과 사업 운영 |
| Logistics / Connected world | 내부·외부 물류와 협력 네트워크 |

정확한 RAMI 4.0의 계층 명칭과 표준 축은 [[concepts/RAMI 4.0|RAMI 4.0]]에서 따로 정리한다.

### 3. 디지털트윈 기능 축

| 기능 | 설계 단계 | 제조·운영 단계 |
| --- | --- | --- |
| Prototyping | 제품·공정 설계안의 가상 시험 | — |
| Pilot testing | 파일럿 생산과 변경안의 시험 | — |
| Monitoring | 설계 데이터와 상태 추적 | 설비·공정·재공품의 현재 상태 추적 |
| Improvement | 설계와 공정의 성능 개선 | 병목, 품질, 자원 활용 개선 |
| Control | 설계 기준과 운영 규칙의 반영 | 작업·공정·생산계획 조정 |

## 사례 연결

| 사례 | 데이터·모델 | 의사결정 |
| --- | --- | --- |
| 인간-로봇 협업 조립 | 실시간 조립선 데이터, 이산사건 시뮬레이션, Digital Mirror | 작업 배치·작업 할당·workflow 비교 |
| MaaS dynamic job-shop | IoT platform, Advanced Plant Model, FlexSim, OptQuest | 설비 투자와 생산순서·자원 배치 결정 |
| 검증·타당화 문헌 연구 | 4R capability, 요구사항, 사용 맥락 | 신뢰할 수 있는 디지털트윈의 증거 설계 |

## 연구 공백과 질문

- 여러 계층과 여러 기능을 한 시스템에서 연결할 때 데이터 의미와 책임 경계는 어떻게 정의할 것인가?
- 설계·제조·사용 단계에서 생성된 데이터의 정보 단절과 중복을 어떻게 줄일 것인가?
- 시뮬레이션 기반 최적화 결과를 실제 운영에 되먹임할 때 불확실성과 지연을 어떻게 다룰 것인가?
- 생산성뿐 아니라 품질, 안전, 작업자 ergonomics, 지속가능성을 함께 최적화할 수 있는가?
- 디지털트윈이 실제로 사용 목적을 충족했다는 검증·타당화 증거를 어떤 공통 형식으로 남길 것인가?

## 혜영님의 연구 지도 사용법

새 연구 아이디어를 이 지도에 놓을 때 다음 네 가지를 먼저 표시한다.

1. 적용 대상: 제품·기계·공정·공장·물류 중 어디인가?
2. 수명주기 단계: 설계·제조·사용·서비스 중 어디인가?
3. 기능: 모니터링·예측·what-if·최적화·제어 중 무엇인가?
4. 증거: 데이터 연결, 모델 성능, 검증·타당화, 실제 운영 결과를 어떻게 입증할 것인가?

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[concepts/Product Lifecycle Management|제품 수명주기 관리]]
- [[concepts/RAMI 4.0|RAMI 4.0]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[topics/Human-Robot Collaboration in Manufacturing|제조 인간-로봇 협업]]
- [[topics/Trusted Digital Twin|신뢰할 수 있는 디지털트윈]]

## 근거 자료

- [[web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing]]
- [[web/2026-08-01_sciencedirect.com_Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems]]
- [[web/2026-08-01_sciencedirect.com_Transitioning trends into action A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making]]
