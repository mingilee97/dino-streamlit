import base64
from pathlib import Path

import streamlit as st
import streamlit.components.v1 as components

G = Path(__file__).parent / "game"


def build_html():
    html = (G / "index.html").read_text(encoding="utf-8")
    html = html.replace('<link rel="stylesheet" href="index.css">', f'<style>{(G / "index.css").read_text(encoding="utf-8")}</style>')
    html = html.replace('<link href="https://fonts.googleapis.com/css?family=Open+Sans" rel="stylesheet"> ', "")
    html = html.replace('<script src="index.js"></script>', f'<script>{(G / "index.js").read_text(encoding="utf-8")}</script>')
    for p in G.glob("assets/*/*.png"):
        uri = "data:image/png;base64," + base64.b64encode(p.read_bytes()).decode()
        html = html.replace(f"assets/{p.parent.name}/{p.name}", uri)
    return html


st.title("공룡 게임")
st.caption("게임 화면을 클릭한 뒤 스페이스(모바일은 탭)")
components.html(build_html(), height=400)
