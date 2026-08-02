---
type: concept
title: "Product Lifecycle Management"
status: reviewed
confidence: high
confidence_reason: "스마트 제조 디지털트윈 문헌 연구가 제시한 제품 기획부터 재활용·폐기까지의 수명주기와 데이터 문제를 위키용으로 정리했다."
tags:
  - product-lifecycle-management
  - digital-twin
  - smart-manufacturing
sources:
  - "[[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]"
---

# Product Lifecycle Management

## 정의

제품 수명주기 관리(Product Lifecycle Management, PLM)는 제품의 기획부터 설계·제조·운송·판매·사용·서비스·재활용 또는 폐기까지 전 과정의 정보와 활동을 통합적으로 관리하는 관점이다.

## 수명주기 단계

| 단계 | 핵심 활동 | 디지털트윈과의 연결 |
| --- | --- | --- |
| 개념 생성 | 고객 요구와 시장 정보를 바탕으로 제품 개념과 주요 기능 정의 | 요구사항과 설계 후보의 가상 비교 |
| 설계 | 제품 사양, 개념 설계, 상세 설계 확정 | 설계 검토, 가상 시험, prototype·pilot testing |
| 제조 | 설계 사양에 따라 부품을 가공·조립 | 공정 모니터링, 개선, 생산계획·제어 |
| 운송 | 생산 완료 후 판매 지점으로 이동 | 물류 상태와 재고 흐름 추적 |
| 판매 | 고객 또는 기업에 제품 제공 | 판매 정보와 제품 이력 연결 |
| 사용 | 고객이 제품을 실제로 운용 | 사용 상태·성능·고장 데이터 수집 |
| 사후 서비스 | 고장·정비·수리 지원 | 예지보전과 서비스 의사결정 |
| 재활용·폐기 | 제품을 재사용·재활용하거나 폐기 | 자원·부품의 다음 수명주기 정보 연결 |

## 왜 디지털트윈이 필요한가

제품 수명주기 데이터는 단계와 조직별 목적이 달라 정보 단절, 중복, 실제 현장과 가상 모델 사이의 비교 어려움을 만들 수 있다. 디지털트윈은 물리 시스템의 운영 데이터를 디지털 모델과 연결해 가상 실험과 실제 성능 비교를 가능하게 하므로, 수명주기 전반의 정보 흐름을 연결하는 후보가 된다.

## 연구에서 확인할 것

- 어느 단계의 데이터를 수집하고 다음 단계에 어떤 의미로 전달하는가?
- 설계·제조·사용 데이터의 식별자와 버전이 일관되게 유지되는가?
- 가상 시험 결과와 실제 성능 사이의 차이를 어떻게 검증·타당화하는가?
- 제품 수명주기 전체를 연결하는 것이 실제 연구 목적에 필요한가, 아니면 특정 단계에 맞춘 fit-for-purpose 모델이 더 적합한가?

## 혜영님의 연구와의 관련성

디지털트윈 기반 최적화 연구에서 PLM은 최적화 대상과 데이터의 시간적 범위를 정하는 틀이다. 예를 들어 공정 파라미터 최적화는 제조 단계에 집중하지만, 설계 변경·설비 유지보수·사용 중 고장 데이터가 목적함수와 제약조건에 영향을 줄 수 있다.

## 연결

- [[concepts/Digital Twin|디지털트윈]]
- [[topics/Digital Twin in Smart Manufacturing|스마트 제조 디지털트윈]]
- [[concepts/RAMI 4.0|RAMI 4.0]]
- [[concepts/Interoperability|상호운용성]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]

## 근거 자료

- [[papers/Past, present, and future research of digital twin for smart manufacturing (2021)]]
