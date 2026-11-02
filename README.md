# dino-streamlit

크롬 인터넷 끊김 공룡 게임(T-Rex runner)을 Streamlit 앱으로 띄운다. 게임 화면을 클릭한 뒤 스페이스(모바일은 탭).

## 실행
```
pip install -r requirements.txt
streamlit run app.py
```

## 바꾼 설정값 (`game/index.js`, `Runner.config`)
| 항목 | 원래 값 | 바꾼 값 |
|---|---|---|
| `ACCELERATION` (가속) | 0.001 | 0.0015 |
| `MAX_SPEED` (최고 속도) | 13 | 14 |

## 출처·라이선스
- 게임: [wayou/t-rex-runner](https://github.com/wayou/t-rex-runner) `gh-pages` (BSD 3-Clause, `game/LICENSE`).
- 원작: Chromium 오프라인 공룡 게임 (The Chromium Authors, BSD). 저작권 머리말은 `game/index.js`에 그대로 있다.
