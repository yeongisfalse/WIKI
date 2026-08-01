# Raw 원본 규칙

- 이 폴더는 사람이 수집한 불변 원본이다. AI는 파일을 수정, 이름 변경, 이동, 삭제하지 않는다.
- 새 원본은 유형별 하위 폴더에 둔다: `papers/`, `web/`, `notes/`.
- Web Clipper 자료는 `web/`에 `YYYY-MM-DD_domain_slug.md` 형식으로 저장한다.
- Web Clipper 원본에는 `type`, `title`, `source`, `site`, `captured_at`, `status: captured` 메타데이터를 둔다.
- 논문 PDF와 직접 작성한 원본 메모는 각각 `papers/`와 `notes/`에 보존한다.
- 원본의 의미 있는 해석, 요약, 연결은 `wiki/`에 작성한다.
- 원본이 불완전하거나 출처가 불명확하면 그 상태를 위키에 명시한다.
