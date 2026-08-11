---
type: paper
content_type: literature_review
title: "Past, present, and future research of digital twin for smart manufacturing"
authors:
  - "Yoo Ho Son"
  - "Goo-Young Kim"
  - "Hyeon Chan Kim"
  - "Chanmo Jun"
  - "Sang Do Noh"
journal: "Journal of Computational Design and Engineering"
published: "2021-12-30"
volume: 9
issue: 1
pages: "1–23"
doi: "10.1093/jcde/qwab067"
source: "https://academic.oup.com/jcde/article/9/1/1/6490313"
site: "OUP Academic"
raw_file: "[[raw/web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing]]"
captured_at: "2026-08-01T22:36:17+09:00"
status: draft
confidence: high
confidence_reason: "OUP 공식 저널 페이지에서 저자·출판일·DOI·본문을 확인한 peer-reviewed literature review이다. 다만 검색·스크리닝 범위가 Scopus, 2003–2020, English/engineering/article로 제한된다."
tags:
  - digital-twin
  - smart-manufacturing
  - simulation
  - optimization
---

# Past, present, and future research of digital twin for smart manufacturing

## 빠른 이해

- 이 문헌 연구는 스마트 제조 디지털트윈 연구를 적용 대상, 제품 수명주기, RAMI 4.0 계층, 기능의 조합으로 분류한다.
- 핵심 주장은 디지털트윈을 단일 기술이 아니라 물리 대상·디지털 모델·데이터 흐름·사용 기능이 결합된 시스템으로 봐야 한다는 것이다.
- 결과를 읽을 때는 2003–2020년, Scopus, 영어·engineering·article 중심의 검색 범위를 먼저 기억해야 하며, 최신 기술과 다른 분야까지 자동으로 일반화하면 안 된다.

## 핵심 내용

이 논문은 스마트 제조에서 디지털 트윈(DT)이 **어디에 적용되고 어떤 기능을 수행하는지**를 제품 수명주기 관리(PLM) 단계와 RAMI 4.0의 계층 수준으로 분류한 문헌 연구다. 분석 결과 DT의 핵심 기능을 설계 단계의 **prototyping·pilot testing**, 제조 단계의 **monitoring·improvement·control**로 정리하고, 여러 기능과 적용 대상을 함께 다루는 통합 아키텍처를 미래 방향으로 제안한다.

## 연구 설계 및 범위

- Scopus에서 2003년 1월–2020년 12월의 `article`·`engineering`·영어 문헌을 검색했다.
- 2,579편에서 필터와 초록·서론·결론 스크리닝을 거쳐 91편을 분석했다.
- 분석 축은 PLM의 제품 수명주기 단계와 RAMI 4.0의 hierarchy level이다.
- 연구 질문은 적용 위치, DT 기능, 기존 연구의 미흡한 점, 향후 연구 방향을 다룬다.

## 주요 발견

### 1. DT는 단순 시뮬레이션과 다르다

논문이 정리한 DT의 최소 구성은 다음 세 요소다.

1. 물리 공간의 물리 객체
2. 사이버 공간의 디지털 객체
3. 두 공간을 동기화하는 데이터·정보 연결

따라서 물리 시스템과 데이터를 연결하지 않는 독립적인 가상 시뮬레이션 모델은 DT의 일부 활용 기술일 수는 있어도, 논문이 정의하는 DT 자체와 동일하지 않다.

### 2. 기능과 적용 대상

| PLM 단계 | DT 기능 | 대표 적용 대상(RAMI 4.0 hierarchy) |
| --- | --- | --- |
| 설계 | Prototyping, pilot testing | 제품, 기계, 공정 |
| 제조 | Monitoring, improvement, control | 기계, 공정, 공장, 물류 |

사례들은 레이아웃·공정 설계, 생산 모니터링, 예지·상태 개선, 스케줄링·자원 배분, 공정 파라미터 조정과 제어에 DT를 사용한다. 논문은 과거·현재 연구가 대체로 한 번에 하나의 기능과 적용 대상만 다뤘다고 보고, 설계와 제조 DT의 통합을 제안한다.

### 3. 통합 아키텍처의 방향

미래 시스템은 여러 적용 대상에 대해 prototyping부터 control까지의 기능을 연계해야 한다. 이를 위해 참조 아키텍처, 전체 시스템을 구동하는 절차, 엔지니어링 애플리케이션에 필요한 데이터를 정의해야 한다.

## 분석적 시사점

이 연구의 분류 축은 새로운 문헌이나 시스템을 읽을 때 “무엇을 복제하는가”만 보지 않고, 어느 수명주기 단계와 계층에서 어떤 기능을 수행하는지 분해하게 해준다. 특히 모니터링·예측·what-if·최적화·제어를 구분하면 시뮬레이션 모델이 실제 운영 의사결정에 사용되는 지점을 추적할 수 있다.

다만 이 시사점은 문헌 분류 틀을 분석에 적용한 해석이다. 특정 디지털트윈 아키텍처가 이 분류의 모든 축을 구현한다고 단정하지 않으며, 시스템 경계·데이터 주기·검증 증거를 사례별로 다시 확인해야 한다.

## 출처와 맥락

- 저자: Yoo Ho Son, Goo-Young Kim, Hyeon Chan Kim, Chanmo Jun, Sang Do Noh
- 저널: *Journal of Computational Design and Engineering*, 9(1), 1–23
- 이 논문은 새로운 실험을 수행한 연구가 아니라 2003–2020년 제조 분야 DT 문헌을 분류·종합한 literature review다.
- 공식 페이지의 초록에는 “gab study”라는 오탈자가 있으나, 본 요약에서는 문맥상 “기존 연구의 미흡한 측면 분석”으로만 정리한다.

## 신뢰도와 근거

- 평가: `high`
- 근거: OUP의 공식 저널 페이지에서 서지정보, DOI, 초록, 본문 및 문헌 선택 절차를 확인했다. 원문은 open access다.
- 범위 주의: Scopus 검색과 사전 정의된 필터·스크리닝 기준에 포함된 문헌만 분석했으므로 전체 DT 연구를 빠짐없이 대표한다고 단정할 수 없다.

## 한계와 확인 필요

- 분석 기간이 2003–2020년이므로 최신 연구 동향은 별도 자료로 보완해야 한다.
- `article`·`engineering`·영어·Scopus 조건으로 인해 다른 데이터베이스, 언어, 학문 분야의 연구가 제외될 수 있다.
- 91편의 분류는 저자들의 스크리닝 및 분류 기준에 의존하며, 분류 결과가 모든 제조 현장에 일반화되는지는 추가 검증이 필요하다.
- 통합 아키텍처는 제안 수준이며, 본 논문 자체가 그 아키텍처의 실험적 성능을 검증한 것은 아니다.

## 연결 후보

- [[concepts/Digital Twin]] — 물리 공간·사이버 공간·데이터 연결, 시뮬레이션과의 구분
- [[topics/Digital Twin in Smart Manufacturing]] — PLM × RAMI 4.0 × DT 기능 분류 지도
- [[concepts/Product Lifecycle Management]] — 설계·제조·사용·서비스 전 과정의 적용 맥락
- [[concepts/RAMI 4.0]] — hierarchy level과 스마트 제조 아키텍처
- [[methods/Simulation-based Optimization]] — DT 시뮬레이션과 최적화·의사결정의 접점
- [[ideas/Integrated Digital Twin Optimization Loop]] — 다기능 DT 아키텍처를 연구 아이디어로 확장할 후보

## 원문 및 출처

- [OUP 공식 논문 페이지](https://academic.oup.com/jcde/article/9/1/1/6490313)
- [DOI: 10.1093/jcde/qwab067](https://doi.org/10.1093/jcde/qwab067)
- 원문 캡처: [[raw/web/2026-08-01_oup.com_Past, present, and future research of digital twin for smart manufacturing]]
