"""Streamlit entry: sidebar, navigation, active panel."""

from __future__ import annotations

import streamlit as st

from config import PAGE_LAYOUT, PAGE_TITLE, PANEL_ORDER
from components.layout import render_panel_header, render_sidebar
from data.content import MAIN_INTRO_CAPTION
from panels.hallucination import render as render_hallucination
from panels.jailbreak import render as render_jailbreak
from panels.mental_math import render as render_mental_math
from panels.multilingual import render as render_multilingual
from panels.poetry import render as render_poetry
from panels.reasoning import render as render_reasoning
from utils.state import get_active_panel, init_state, set_active_panel, touch_current_panel_visit

st.set_page_config(page_title=PAGE_TITLE, layout=PAGE_LAYOUT, initial_sidebar_state="expanded")

init_state()
render_sidebar()

st.title(PAGE_TITLE)
st.caption(MAIN_INTRO_CAPTION)

nav_cols = st.columns(len(PANEL_ORDER))
for col, (panel_id, label) in zip(nav_cols, PANEL_ORDER):
    with col:
        if st.button(
            label,
            key=f"nav_{panel_id}",
            type="primary" if get_active_panel() == panel_id else "secondary",
            use_container_width=True,
        ):
            set_active_panel(panel_id)

touch_current_panel_visit()

active = get_active_panel()

renderers = {
    "multilingual": render_multilingual,
    "poetry": render_poetry,
    "mental_math": render_mental_math,
    "reasoning": render_reasoning,
    "hallucination": render_hallucination,
    "jailbreak": render_jailbreak,
}

render_panel_header(active)
renderers[active]()
