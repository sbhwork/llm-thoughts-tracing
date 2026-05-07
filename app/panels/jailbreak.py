"""Panel 6: BOMB acrostic jailbreak anatomy."""

from __future__ import annotations

import streamlit as st

from data.content import (
    JAILBREAK_CALLOUT_ERROR,
    JAILBREAK_CALLOUT_SUCCESS,
    JAILBREAK_KEY_FINDING,
    JAILBREAK_PHASE1_TEXT,
    JAILBREAK_PHASE1_TITLE,
    JAILBREAK_PHASE2_TEXT,
    JAILBREAK_PHASE2_TITLE,
    JAILBREAK_PROMPT,
    JAILBREAK_PROMPT_CAPTION,
    JAILBREAK_PROMPTS,
    JAILBREAK_STEPS,
    UI_LABELS,
)
from components.ui import (
    render_callout,
    render_discussion_prompts,
    render_highlight_box,
    render_step_trace,
)


def render() -> None:
    with st.container(border=True):
        st.caption(JAILBREAK_PROMPT_CAPTION)
        st.code(JAILBREAK_PROMPT, language=None)

    render_step_trace(list(JAILBREAK_STEPS))

    st.markdown(f"**{UI_LABELS['simulated_output']}**")
    st.caption(JAILBREAK_PHASE1_TITLE)
    render_highlight_box(JAILBREAK_PHASE1_TEXT, "danger")
    st.caption(JAILBREAK_PHASE2_TITLE)
    render_highlight_box(JAILBREAK_PHASE2_TEXT, "safe")

    with st.container(border=True):
        st.caption(UI_LABELS["key_finding"])
        st.markdown(JAILBREAK_KEY_FINDING)

    render_callout(JAILBREAK_CALLOUT_ERROR, "error")
    render_callout(JAILBREAK_CALLOUT_SUCCESS, "success")
    render_discussion_prompts(JAILBREAK_PROMPTS)
