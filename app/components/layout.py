"""Application chrome: sidebar and panel headers."""

from __future__ import annotations

import streamlit as st

from config import ANTHROPIC_RESEARCH_URL, PANEL_ORDER, TAG_COLOURS
from data.content import (
    ABOUT_SUMMARY_SENTENCES,
    GLOSSARY,
    NAV_LABELS,
    PANEL_INTROS,
    SIDEBAR_LINK_TEXT,
)
from components.ui import render_tag


def render_panel_header(panel_id: str) -> None:
    intro = PANEL_INTROS[panel_id]
    colour = TAG_COLOURS[panel_id]
    c1, c2 = st.columns([1, 6])
    with c1:
        render_tag(intro["case_tag"], colour)
    with c2:
        st.markdown(intro["description"])


def render_sidebar() -> None:
    with st.sidebar:
        with st.expander(NAV_LABELS.section_about):
            st.write(ABOUT_SUMMARY_SENTENCES)
            st.markdown(
                f"[{SIDEBAR_LINK_TEXT}]({ANTHROPIC_RESEARCH_URL})",
                unsafe_allow_html=False,
            )
        with st.expander(NAV_LABELS.section_glossary):
            for term, definition in GLOSSARY.items():
                st.markdown(f"**{term}**")
                st.caption(definition)

        visited = st.session_state.get("visited_panels", [])
        total = len(PANEL_ORDER)
        st.caption(f"{NAV_LABELS.progress_label}: {len(visited)} / {total}")
