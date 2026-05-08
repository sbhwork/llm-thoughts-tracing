"""Panel 2: poetry / rhyme planning."""

from __future__ import annotations

import streamlit as st

from config import NAV_ACTIVE_SUFFIX
from data.content import (
    POETRY_CALLOUT,
    POETRY_FIRST_LINE,
    POETRY_FIRST_LINE_CAPTION,
    POETRY_MODE_LABELS,
    POETRY_MODES,
    POETRY_PROMPTS,
    POETRY_SCENARIOS,
    UI_LABELS,
)
from components.ui import render_callout, render_discussion_prompts
from utils.state import set_poetry_mode


def render() -> None:
    with st.container(border=True):
        st.caption(POETRY_FIRST_LINE_CAPTION)
        st.markdown(f"*{POETRY_FIRST_LINE}*")

    mc = st.columns(len(POETRY_MODES))
    for col, mode in zip(mc, POETRY_MODES):
        with col:
            base = POETRY_MODE_LABELS[mode]
            shown = f"{base}{NAV_ACTIVE_SUFFIX}" if st.session_state["poetry_mode"] == mode else base
            st.button(
                shown,
                key=f"poetry_{mode}",
                on_click=set_poetry_mode,
                args=(mode,),
                type="secondary",
                use_container_width=True,
            )

    scenario = POETRY_SCENARIOS[st.session_state["poetry_mode"]]
    o1, o2 = st.columns(2)
    with o1:
        with st.container(border=True):
            st.caption(UI_LABELS["planned_rhyme"])
            st.markdown(f"*{scenario['planned_rhyme']}*")
    with o2:
        with st.container(border=True):
            st.caption(UI_LABELS["completed_line"])
            st.markdown(f"*{scenario['second_line']}*")

    st.markdown(f"_{UI_LABELS['mechanistic_note']}: {scenario['mechanism_note']}_")

    render_callout(POETRY_CALLOUT, "warning")
    render_discussion_prompts(POETRY_PROMPTS)
