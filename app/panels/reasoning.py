"""Panel 4: faithful vs motivated chain-of-thought."""

from __future__ import annotations

import streamlit as st

from config import NAV_ACTIVE_SUFFIX
from data.content import (
    REASONING_FAITHFUL_ANSWER,
    REASONING_FAITHFUL_CALLOUT,
    REASONING_FAITHFUL_PROBLEM,
    REASONING_FAITHFUL_STEPS,
    REASONING_MODE_LABELS,
    REASONING_MODES,
    REASONING_MOTIVATED_CALLOUT,
    REASONING_MOTIVATED_HINT,
    REASONING_MOTIVATED_HINT_LABEL,
    REASONING_MOTIVATED_PROBLEM,
    REASONING_MOTIVATED_STATED,
    REASONING_MOTIVATED_STEPS,
    REASONING_PROMPTS,
    UI_LABELS,
)
from components.ui import render_callout, render_discussion_prompts, render_step_trace
from utils.state import set_reasoning_mode


def render() -> None:
    rc = st.columns(len(REASONING_MODES))
    for col, mode in zip(rc, REASONING_MODES):
        with col:
            base = REASONING_MODE_LABELS[mode]
            shown = f"{base}{NAV_ACTIVE_SUFFIX}" if st.session_state["reasoning_mode"] == mode else base
            st.button(
                shown,
                key=f"reason_{mode}",
                on_click=set_reasoning_mode,
                args=(mode,),
                type="secondary",
                use_container_width=True,
            )

    mode = st.session_state["reasoning_mode"]

    if mode == "faithful":
        with st.container(border=True):
            st.caption(UI_LABELS["problem_card"])
            st.markdown(REASONING_FAITHFUL_PROBLEM)
            st.caption(UI_LABELS["reasoning_sqrt_hint"])
        render_step_trace(list(REASONING_FAITHFUL_STEPS))
        with st.container(border=True):
            st.caption(UI_LABELS["answer_card"])
            st.markdown(REASONING_FAITHFUL_ANSWER)
        render_callout(REASONING_FAITHFUL_CALLOUT, "success")
    else:
        with st.container(border=True):
            st.caption(UI_LABELS["problem_card"])
            st.markdown(REASONING_MOTIVATED_PROBLEM)
            st.caption(UI_LABELS["reasoning_cos_hint"])
            st.markdown(
                f"*{REASONING_MOTIVATED_HINT_LABEL}: {REASONING_MOTIVATED_HINT}*",
            )
        render_step_trace(list(REASONING_MOTIVATED_STEPS))
        with st.container(border=True):
            st.caption(UI_LABELS["stated_answer"])
            st.markdown(f"*{REASONING_MOTIVATED_STATED}*")
        render_callout(REASONING_MOTIVATED_CALLOUT, "error")

    render_discussion_prompts(REASONING_PROMPTS)
