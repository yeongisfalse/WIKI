---
type: web
title: "Verification and validation of digital twins: a systematic literature review for manufacturing applications"
authors:
  - "Julia Bitencourt"
  - "Ana Wooley"
  - "Gregory Harris"
journal: "International Journal of Production Research"
published: "2025-01-02"
volume: 63
issue: 1
pages: "342–370"
doi: "10.1080/00207543.2024.2357741"
source: "https://www.tandfonline.com/doi/full/10.1080/00207543.2024.2357741"
site: "Taylor & Francis"
raw_file: "[[raw/web/2026-08-01_tandfonline.com_Verification and validation of digital twins a systematic literature review for manufacturing applications]]"
captured_at: "2026-08-01T23:29:10+09:00"
status: draft
confidence: high
confidence_reason: "International Journal of Production Research의 systematic literature review이며, Taylor & Francis 공식 본문에서 검색·분류 절차와 결과를 확인했다. 데이터베이스와 저자 분류 기준에 따른 범위 제한이 있다."
tags:
  - digital-twin
  - verification
  - validation
  - model-credibility
  - manufacturing
---

# Verification and validation of digital twins: a systematic literature review for manufacturing applications

## 핵심 내용

이 systematic literature review(SLR)는 제조 분야 디지털트윈(DT)에서 **verification(구현 검증)**과 **validation(사용 맥락 타당화)**이 실제로 어떻게 수행되는지, 그리고 두 과정이 구분되는지를 분석한다. 결론은 두 과정을 모두 수행했다고 보고한 연구가 적고, 검증과 타당화의 표준 절차와 목적에 대한 합의도 부족하다는 것이다. 신뢰할 수 있는 DT를 만들려면 DT의 capability·context of use·요구사항과 연결된 검증과 타당화가 필요하다.

## ingest 단계란?

이 위키에서 `ingest`는 `raw/`에 보관된 불변 원본을 읽어 위키용 요약·메타데이터·연결 제안으로 구조화하고, 처리 상태를 기록하는 초기 처리 단계다. 원본을 수정하거나 덮어쓰는 단계가 아니다.

## 연구 설계 및 범위

- ScienceDirect, Engineering Village, Web of Science에서 `digital twin`과 manufacturing/production/fabrication/assembly 및 verification/validation 검색어를 조합했다.
- 315편에서 중복 제거 후 269개 제목, 제조 DT 적용 기준을 거쳐 188편을 full-text 검토했고, 최종 분석에는 157편이 들어갔다.
- Phase 1은 DT capability를 4R(Representation, Replication, Reality, Relational) framework로 분류했다.
- Phase 2는 검증·타당화 활동의 유형, 목적, 기법과 DT 성숙도·적용 분야의 관계를 분류했다.

## 주요 발견

### 1. 많은 연구가 DT의 최소 조건을 충족하지 않는다

#### 4R framework의 단계

| 단계 | 의미 | 이 연구에서 본 capability 예시 |
| --- | --- | --- |
| **Representation** | 물리 시스템을 디지털 공간에 표현하기 위한 기반을 만드는 단계 | 실시간 데이터 수집 파이프라인, 저장·분석, 가상 표현 |
| **Replication** | 실제 데이터를 이용해 물리 시스템의 출력을 재현하는 디지털 복제물을 만드는 단계 | 물리 시스템과 디지털 복제물의 출력 일치 |
| **Reality** | 복제에 더해 물리 시스템의 동작을 예측하고 what-if 분석을 수행하는 단계 | 미래 상태 예측, 시나리오 비교, 고급 시뮬레이션 |
| **Relational** | 디지털트윈이 고차원 문제 해결과 자율적 조정을 수행하는 단계 | 자율 의사결정, self-calibration, 양방향 데이터·행동 연결 |

- 49%가 저자들이 채택한 정의상 DT가 아닌 것으로 분류되었다.
- 4R 분류에서 Representation 약 15%, Replication 26%, Reality 10%였고, Relational 수준은 없었다.
- 전통적인 offline simulation이나 물리–가상 간 실시간 동기화가 없는 모델을 DT로 부르는 사례가 많았다.

### 2. 검증과 타당화 현황

- 두 활동 모두 수행했다고 보고한 연구는 24%였다.
- 구현 검증만 보고한 연구는 31%, 사용 맥락 타당화만 보고한 연구는 35%였다.
- 두 과정을 모두 수행했다고 보고한 연구 중 47%는 검증과 타당화를 서로 다른 목적의 과정이 아니라 동의어처럼 사용했다.
- 자주 쓰인 근거는 case study, 물리·가상 출력 비교, KPI·오차 지표, 요구사항 추적, 모델 기반 시스템 엔지니어링 등이었다.

### 3. 논문이 제안하는 구분

- **구현 검증(verification)**: DT가 명세된 요구사항을 충족하고 구현이 개념 모델을 올바르게 반영하는지 증거를 제시하는 과정
- **사용 맥락 타당화(validation)**: 특정 context of use에서 DT가 물리 시스템을 정확히 대표하고 의도된 운영 목적을 달성하는지 증거를 제시하는 과정

## 출처와 맥락

- 저자: Julia Bitencourt, Ana Wooley, Gregory Harris
- 저널: *International Journal of Production Research*, 63(1), 342–370 (2025)
- 연구는 ISO 23247, 4R framework, 모델링·시뮬레이션의 검증·타당화 관행을 연결해 DT의 신뢰성 문제를 다룬다.

## 신뢰도와 근거

- 평가: `high`
- 근거: Taylor & Francis 공식 본문에서 SLR 검색·선정 절차, 4R 분류, 검증·타당화 결과와 결론을 확인했다.
- 범위 주의: 포함 데이터베이스·영어 문헌·저자들의 분류 기준에 의존하므로 모든 DT 연구를 대표한다고 단정하지 않는다.

## 혜영님의 연구와의 관련성

- 최적화 결과를 실제 시스템에 적용하려면 “모델이 요구사항대로 구현되었는가(구현 검증)”와 “사용 목적에 맞게 실제를 대표하는가(사용 맥락 타당화)”를 분리해 기록해야 한다.
- simulation-based DT를 구축할 때, 자료를 원본에서 위키용 구조로 바꾸는 ingest(수집·초기 정리) 단계부터 상태 동기화·출력 오차·KPI·요구사항 traceability를 메타데이터로 남기는 운영 규칙을 제안할 수 있다.
- 4R capability를 연구 아이디어 평가표로 사용하면, 단순 시뮬레이션·디지털 모델·실시간 DT·자율 의사결정의 차이를 명확히 할 수 있다.

## 한계와 확인 필요

- SLR의 검증·타당화 분류는 상당 부분 각 논문의 보고와 저자들의 판정에 기반한다.
- 4R 비율은 선택된 157편에 대한 결과이며 전체 분야의 절대 비율이 아니다.
- 검증·타당화 표준화와 trust metric은 연구 방향으로 제안되었지만, 본 논문이 완성된 표준을 제공하는 것은 아니다.

## 연결 후보

- [[concepts/Model Verification and Validation|모델 검증과 타당화]] — 구현 검증·사용 맥락 타당화의 목적과 증거
- [[concepts/Digital Twin Maturity|디지털트윈 성숙도]] — 4R framework와 capability 수준
- [[concepts/Digital Twin|디지털트윈]] — simulation과 동기화된 DT의 구분
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]] — 최적화 결과의 사용 맥락 검증
- [[topics/Trusted Digital Twin|신뢰할 수 있는 디지털트윈]] — 신뢰성·요구사항 추적·검증·타당화 연구 지도

## 원문 및 출처

- [Taylor & Francis 공식 논문 페이지](https://www.tandfonline.com/doi/full/10.1080/00207543.2024.2357741)
- [DOI: 10.1080/00207543.2024.2357741](https://doi.org/10.1080/00207543.2024.2357741)
- 원문 캡처: [[raw/web/2026-08-01_tandfonline.com_Verification and validation of digital twins a systematic literature review for manufacturing applications]]
