---
type: concept
title: "Interoperability"
status: reviewed
confidence: high
confidence_reason: "HRC 사례의 FIWARE/FIROS·NGSIv2 연동과 MaaS 사례의 IoT platform·메시지 브로커·API 구조를 상호운용성 관점으로 통합했다."
tags:
  - interoperability
  - digital-twin
  - industrial-iot
  - data-exchange
sources:
  - "[[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]"
  - "[[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]"
  - "[[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]"
---

# Interoperability

## 빠른 이해

- 상호운용성은 데이터를 주고받는 연결성만이 아니라, 송수신자가 데이터의 구조·단위·시간 의미·상태 의미를 동일하게 해석하는 능력이다.
- 디지털트윈에서는 장치·프로토콜·메시지 스키마·의미 모델·권한·운영 절차가 함께 맞아야 센서에서 모델, 모델에서 실행계획까지의 흐름이 유지된다.
- 연결이 끊기지 않았다는 사실만으로 충분하지 않다. 지연·결측·중복·버전 차이·재전송·의미 불일치가 결과와 의사결정에 미치는 영향을 점검해야 한다.

## 정의

상호운용성은 서로 다른 장치·시스템·모델·조직이 데이터를 교환할 뿐 아니라, 그 데이터의 의미와 사용 규칙을 이해하고 함께 작업할 수 있는 능력이다. 디지털트윈에서는 센서·설비·시뮬레이션·최적화·실행 시스템 사이의 연결을 가능하게 한다.

## 층별로 확인할 것

| 층 | 질문 | 예시 |
| --- | --- | --- |
| 기술·통신 | 연결과 메시지 전달이 가능한가? | Message Broker, Protocol Adapter, REST API |
| 문법·형식 | 데이터 구조와 직렬화 방식이 합의되어 있는가? | JSON, NGSIv2 |
| 의미·모델 | 같은 필드와 상태를 같은 의미로 해석하는가? | 설비 ID, 작업 상태, 시간, 단위, KPI 정의 |
| 과정·조직 | 누가 언제 어떤 데이터를 만들고 사용할 권한이 있는가? | MES·APM·시뮬레이션·현장 실행의 책임 경계 |

## 사례의 연결 구조

HRC 사례는 FIWARE/FIROS와 NGSIv2 JSON 메시지를 이용해 조립선의 디지털 모델·Digital Mirror·외부 시스템 사이의 publish/subscribe 통신을 구성했다. MaaS 사례는 IoT platform의 Message Broker, Protocol Adapter, Thing·Service Registry, Data Store와 API Gateway를 통해 이기종 장치·서비스·Advanced Plant Model·시뮬레이션을 연결했다.

## 디지털트윈 연구에서의 체크리스트

- 물리 대상과 디지털 모델을 연결하는 식별자가 일관적인가?
- 상태와 이벤트의 시간·단위·버전·출처가 보존되는가?
- 데이터가 한 방향으로만 흐르는가, 계획·행동이 실제 시스템으로 되돌아가는가?
- 프로토콜이 달라질 때 변환 계층이 의미 손실 없이 동작하는가?
- 외부 시스템과 서비스의 권한, 보안, 장애, 재전송 정책이 정의되어 있는가?
- 시뮬레이션 출력과 실행 시스템이 동일한 KPI와 상태 의미를 공유하는가?

## 장애와 변경을 해석하는 방법

상호운용성은 정상 경로만 설계해서는 충분하지 않다. 메시지 지연·중복·순서 뒤바뀜·부분 손실·스키마 버전 변경이 발생했을 때 시스템이 어떤 상태를 유지하고, 재전송하거나 무시하며, 사용자에게 경고하는지를 정의해야 한다.

특히 최적화 결과를 실행계획으로 변환할 때는 데이터 계약이 중요하다. 입력의 단위·시간 기준·식별자·허용 범위를 확인하고, 실행 시스템이 이해하지 못하는 필드나 오래된 상태를 차단해야 한다. 통신 성공 로그만으로 의미 보존을 증명할 수 없으므로 변환 전후의 값과 의미를 검증하는 테스트가 필요하다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[concepts/Product Lifecycle Management|제품 수명주기 관리]]
- [[topics/Human-Robot Collaboration in Manufacturing|제조 인간-로봇 협업]]
- [[concepts/Decision Support System|의사결정 지원 시스템]]
- [[ideas/Integrated Digital Twin Optimization Loop|통합 디지털트윈 최적화 루프]]

## 근거 자료

- [[papers/Simulation-based Digital Twin for enhancing human-robot collaboration in assembly systems (2024)]]
- [[papers/Transitioning trends into action - A simulation-based Digital Twin architecture for enhanced strategic and operational decision-making (2024)]]
- [[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]
