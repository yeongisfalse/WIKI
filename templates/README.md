# Web Clipper 템플릿

`web-clipper-general.json`을 Obsidian Web Clipper 설정에서 Import한다.

- 수집 위치: `raw/web/`
- `raw/web/`는 수집 경로일 뿐 문서 유형을 확정하지 않는다.
- 템플릿은 `capture_type: web_clipper`, `document_type: unknown`, `status: captured`를 기록한다.
- ingest 때 논문·문헌 리뷰는 `wiki/papers/`로, Editorial·Commentary·기사·블로그·일반 웹 문서는 `wiki/web/`로 컴파일한다.
- 원본과 메타데이터만 저장하며, 원문을 짧게 줄이거나 개인화된 해석을 원본에 삽입하지 않는다.
- AI 요약과 위키 연결은 프로젝트 대화창에서 명시적으로 대기열 처리를 요청할 때 수행한다.
- 생성된 위키 페이지는 한 문장 정의부터 근거·원문까지의 계층형 구조를 사용하고, 원문을 다시 열지 않아도 작동 원리와 한계를 이해할 수 있게 작성한다.
