"""Panel 2: poetry / rhyme planning."""

from __future__ import annotations

import streamlit as st

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


def render() -> None:
    with st.container(border=True):
        st.caption(POETRY_FIRST_LINE_CAPTION)
        st.markdown(f"*{POETRY_FIRST_LINE}*")

    mc = st.columns(len(POETRY_MODES))
    for col, mode in zip(mc, POETRY_MODES):
        with col:
            if st.button(
                POETRY_MODE_LABELS[mode],
                key=f"poetry_{mode}",
                type="primary" if st.session_state["poetry_mode"] == mode else "secondary",
                use_container_width=True,
            ):
                st.session_state["poetry_mode"] = mode

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
