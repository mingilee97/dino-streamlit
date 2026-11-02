# dino-streamlit

- 크롬 인터넷 끊김 공룡 게임(Chromium T-Rex runner)을 Streamlit 앱에 넣어 Streamlit Community Cloud로 공개한다. 참고한 방식: https://pinko-eugene527.streamlit.app/ (사용자 사이트가 아니다. 만든 방식만 따른다).
- GitHub: 공개 저장소 `mingilee97/dino-streamlit`. 배포는 이 저장소 main을 Streamlit Community Cloud에 연결한다.
- 게임 코드는 직접 비슷하게 새로 짜지 않는다. 원작(Chromium, BSD) 또는 공개된 튜닝판(포크·모드)을 라이선스를 지켜 가져와 쓰고, 출처와 라이선스 파일을 저장소에 남긴다.
- 구조는 최소로: `app.py`(st.components.v1.html로 게임 HTML/JS를 띄움), `requirements.txt`, 게임 파일 폴더 하나.
- `.env`나 비밀값은 커밋하지 않는다.
- 계획 `docs/계획.md`, 진행 `docs/진행.md`, 보고 `docs/보고서/`.
