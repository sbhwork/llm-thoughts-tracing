"""Panel 3: parallel approximate and exact-digit paths."""

from __future__ import annotations

import streamlit as st

from data.content import (
    MENTAL_MATH_ADDEND_A_LABEL,
    MENTAL_MATH_ADDEND_B_LABEL,
    MENTAL_MATH_CALLOUT,
    MENTAL_MATH_COMBINED_LABEL,
    MENTAL_MATH_CONTRAST_NOTE,
    MENTAL_MATH_METRIC_ROUGH_CAPTION,
    MENTAL_MATH_METRIC_SUM_CAPTION,
    MENTAL_MATH_METRIC_UNITS_CAPTION,
    MENTAL_MATH_PATH_A_LABEL,
    MENTAL_MATH_PATH_B_LABEL,
    MENTAL_MATH_PROMPTS,
    MENTAL_MATH_STATED_TEXT,
    MENTAL_MATH_STATED_TITLE,
    UI_LABELS,
)
from components.ui import render_callout, render_discussion_prompts, render_quote_block


def render() -> None:
    a = int(
        st.number_input(
            MENTAL_MATH_ADDEND_A_LABEL,
            min_value=-10**9,
            max_value=10**9,
            step=1,
            key="mental_math_a",
        )
    )
    b = int(
        st.number_input(
            MENTAL_MATH_ADDEND_B_LABEL,
            min_value=-10**9,
            max_value=10**9,
            step=1,
            key="mental_math_b",
        )
    )

    if st.button(UI_LABELS["trace_action"], key="mental_trace"):
        st.session_state["mental_math_show_trace"] = True

    if st.session_state["mental_math_show_trace"]:
        total = a + b
        rough = int(round(total / 10) * 10)
        last_digit = total % 10

        c1, c2, c3 = st.columns(3)
        with c1:
            with st.container(border=True):
                st.caption(MENTAL_MATH_PATH_A_LABEL)
                st.metric(label=MENTAL_MATH_METRIC_ROUGH_CAPTION, value=str(rough))
        with c2:
            with st.container(border=True):
                st.caption(MENTAL_MATH_PATH_B_LABEL)
                st.metric(label=MENTAL_MATH_METRIC_UNITS_CAPTION, value=str(last_digit))
        with c3:
            with st.container(border=True):
                st.caption(MENTAL_MATH_COMBINED_LABEL)
                st.metric(label=MENTAL_MATH_METRIC_SUM_CAPTION, value=str(total))

        render_quote_block(MENTAL_MATH_STATED_TITLE, MENTAL_MATH_STATED_TEXT, monospace=False)
        st.caption(MENTAL_MATH_CONTRAST_NOTE)

    render_callout(MENTAL_MATH_CALLOUT, "warning")
    render_discussion_prompts(MENTAL_MATH_PROMPTS)
