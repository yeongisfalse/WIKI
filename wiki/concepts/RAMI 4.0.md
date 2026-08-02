---
type: concept
title: "RAMI 4.0"
status: reviewed
confidence: high
confidence_reason: "OUP 문헌 연구가 인용한 RAMI 4.0의 세 축과 제조 계층을 기준으로 정리했다. 표준의 실제 적용에서는 산업 도메인과 사용 목적에 맞춘 해석이 필요하다."
tags:
  - rami-4-0
  - industry-4-0
  - smart-manufacturing
  - digital-twin
sources:
  - "[[papers/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing]]"
---

# RAMI 4.0

## 정의

RAMI 4.0(Reference Architecture Model Industrie 4.0)은 산업 4.0 환경의 구성요소와 관계를 세 개의 축(Three Axes)으로 배치해 설명하는 3차원 참조 아키텍처 모델이다. 디지털트윈이 어떤 대상·수명주기·기능 계층에 걸쳐 있는지 공통 언어로 표시하는 데 사용할 수 있다.

## 세 개의 축 (Three Axes)

| 축 | 무엇을 설명하는가 | 주요 구성 |
| --- | --- | --- |
| Layers | 대상의 속성과 기능을 어떤 층으로 나눌 것인가 | Asset, Integration, Communication, Information, Functional, Business |
| Lifecycle and Value Stream | 제품·설비의 유형과 개별 인스턴스가 수명주기에서 어디에 있는가 | IEC 62890 기반 type·instance 관점 |
| Hierarchy Levels | 기능과 책임이 제조 시스템의 어느 계층에 있는가 | Product, Field device, Control device, Station, Work unit, Enterprise, Connected world |

## 제조 맥락에서 읽는 계층

연구 문헌에서는 복잡한 표준 계층을 제조 대상에 맞춰 제품, 기계·설비, 공정, 공장, 물류와 같은 표현으로 단순화하기도 한다. 이 단순화는 연구 지도의 표시 방법이며, 표준의 원래 명칭을 대체하지 않는다.

## 디지털트윈 연구에 쓰는 방법

새 연구 또는 논문을 읽을 때 다음 좌표를 기록한다.

1. **대상·계층 (Hierarchy Levels)**: 제품·센서·기계·작업대·공정·공장·기업·물류 중 어디인가?
2. **수명주기·가치 흐름 (Lifecycle and Value Stream)**: 설계·제조·사용·서비스 중 어느 단계인가?
3. **층 (Layers)**: 데이터 수집과 연결, 정보 모델, 기능, 사업 의사결정 중 어느 층을 다루는가?

이 좌표는 [[topics/Digital Twin in Smart Manufacturing|스마트 제조 디지털트윈]]의 주제 지도를 구성하는 기준이 된다.

## 주의점

- RAMI 4.0은 구현 방법이나 특정 소프트웨어 아키텍처를 그 자체로 제공하지 않는다.
- 하나의 연구가 모든 축을 같은 해상도로 다룰 필요는 없다.
- “공장 수준 디지털트윈”이라는 표현만으로 데이터 연결, 의사결정 기능, 성숙도를 판단하지 말고 각 축의 위치와 증거를 따로 확인한다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[concepts/Product Lifecycle Management|제품 수명주기 관리]]
- [[topics/Digital Twin in Smart Manufacturing|스마트 제조 디지털트윈]]
- [[concepts/Interoperability|상호운용성]]

## 근거 자료

- [[papers/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing]]
