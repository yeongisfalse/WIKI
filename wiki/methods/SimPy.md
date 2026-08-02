---
type: method
title: "SimPy"
status: draft
confidence: medium
confidence_reason: "기존 로컬 수업·실습 노트에서 SimPy의 기본 실행 구조와 Resource·Container 사용 사례를 컴파일했다. 라이브러리 버전과 공식 문서는 아직 재확인하지 않았고, 실습 코드는 연구용 모델의 검증 증거가 아니다."
source_vault_paths:
  - "/Users/Hyeyeong/Vault/03_AI/01_Language/01_Python/Implementation_Lab/SimPy Introduction.md"
  - "/Users/Hyeyeong/Vault/03_AI/01_Language/01_Python/Implementation_Lab/SimPy - Gas Station Process.md"
  - "/Users/Hyeyeong/Vault/03_AI/01_Language/01_Python/Implementation_Lab/SimPy - Car charging process.md"
source_vault_modified_at:
  - "2026-02-20T16:41:57+09:00"
  - "2026-02-20T18:18:47+09:00"
tags:
  - simpy
  - python
  - discrete-event-simulation
  - simulation
---

# SimPy

## 정의와 역할

SimPy는 Python에서 이산사건 시뮬레이션(Discrete-Event Simulation, DES)을 구현할 때 사용하는 프로세스 기반 라이브러리다. 자동차·고객·작업물과 같은 **프로세스(Process)**가 공통 **환경(Environment)** 안에서 사건(Event)을 기다리고, 사건이 발생한 시점에 다시 실행되도록 모델을 작성한다.

SimPy는 제조 시스템의 의미론이나 실제 데이터의 타당성을 보장하는 도구가 아니다. 연구에서는 시스템을 코드로 표현하는 실행 엔진으로 사용하고, 별도의 구현 검증(verification)과 사용 맥락 타당화(validation)가 필요하다.

## 핵심 구성요소

| SimPy 요소 | 모델링 의미 | 제조 시스템 예 |
| --- | --- | --- |
| `Environment` | 시뮬레이션 시계와 이벤트 큐를 관리하는 실행 환경 | 공장 또는 생산 셀 |
| `Process` | 시간에 따라 행동하는 활성 객체 | 작업물, 차량, 고객, 유조차 |
| `Event` | 프로세스를 재개시키는 사건 | 도착, 완료, 고장, 인터럽트 |
| `Timeout` | 지정한 시뮬레이션 시간이 지난 뒤 발생하는 이벤트 | 처리시간, 이동시간, 도착 간격 |
| `Resource` | 개수가 제한된 공유 자원 | 주유기, 설비, 작업자, 로봇 |
| `Container` | 양(amount)을 저장하고 입·출고하는 자원 | 연료, 재고, 배터리 에너지 |

## 실행 메커니즘

1. `Environment`를 생성하고 프로세스를 등록한다.
2. 프로세스는 Python **generator**와 `yield`를 사용해 사건을 기다린다.
3. 환경은 이벤트 큐에서 가장 이른 사건을 꺼내 시뮬레이션 시계를 그 시점으로 이동시킨다.
4. 사건과 연결된 프로세스가 재개되어 상태를 갱신한다.
5. 이벤트가 더 이상 없거나 `until` 조건에 도달하면 실행을 종료한다.

따라서 `env.timeout(5)`는 실제 프로그램을 5초 동안 멈추는 명령이 아니다. 해당 프로세스가 시뮬레이션 시간 5만큼 기다리도록 이벤트를 등록하고, 그동안 환경은 다른 사건을 처리한다.

## 공유 자원과 상태량

- `Resource`는 `request()`로 점유를 요청하고, 사용이 끝나면 반납한다. 여러 프로세스가 동시에 요청하면 용량을 넘는 요청은 대기열에 들어간다.
- `Container`는 `get(amount)`으로 양을 소비하고 `put(amount)`으로 보충한다. 재고 수준이나 에너지 잔량처럼 개수가 아닌 양을 모델링할 때 적합하다.
- 실습 노트의 주유소 모델은 제한된 주유기(`Resource`)와 탱크 잔량(`Container`)을 함께 사용하고, 임계수준 아래에서 보충 프로세스를 실행한다. 이 구조는 설비 용량·재고·대기행렬이 서로 영향을 주는 제조 모델로 일반화할 수 있다.

## 모델링 체크리스트

- 사건 목록과 상태 변수의 정의가 실제 시스템의 시간 해상도와 일치하는가?
- 도착 간격·처리시간·고장·복구를 어떤 분포와 의존성으로 표현했는가?
- `Resource`의 용량, 우선순위, 선점 여부와 대기 규칙을 명시했는가?
- 초기 상태, 종료 조건, 난수 시드, warm-up과 반복 횟수를 기록했는가?
- 구현 검증과 실제 시스템 출력에 대한 타당화를 별도로 수행했는가?
- 출력 KPI의 단위와 집계 구간을 명확히 했는가?

## 주의와 확인 필요

- 이 페이지는 로컬 수업·실습 노트를 정제한 초안이며 SimPy 공식 문서와 현재 설치 버전의 API를 재확인하지 않았다.
- 차량 충전·주유소 실습은 개념 학습용 예제다. 예제 결과를 실제 충전소나 생산 시스템의 예측 결과로 해석해서는 안 된다.
- 실습에 포함된 코드와 이미지는 이 Wiki로 복사하지 않았다. 원본 코드가 필요하면 로컬 Vault의 원본 경로를 확인한다.

## 원본 학습 노트

- `/Users/Hyeyeong/Vault/03_AI/01_Language/01_Python/Implementation_Lab/SimPy Introduction.md`
- `/Users/Hyeyeong/Vault/03_AI/01_Language/01_Python/Implementation_Lab/SimPy - Gas Station Process.md`
- `/Users/Hyeyeong/Vault/03_AI/01_Language/01_Python/Implementation_Lab/SimPy - Car charging process.md`

## 연결

- [[methods/Discrete-Event Simulation|이산사건 시뮬레이션]]
- [[methods/Simulation-based Optimization|시뮬레이션 기반 최적화]]
- [[concepts/Queueing Theory|대기행렬 이론]]
- [[concepts/Poisson Process|포아송 과정]]
- [[concepts/Model Verification and Validation|모델 검증과 타당화]]
