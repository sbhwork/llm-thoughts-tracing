"""Panel 5: refusal default vs known-entity feature."""

from __future__ import annotations

import streamlit as st

from data.content import (
    HALLUCINATION_CALLOUT,
    HALLUCINATION_CIRCUIT_TITLE,
    HALLUCINATION_DIAGRAM_ARROW,
    HALLUCINATION_DIAGRAM_ENTITY_BLOCK,
    HALLUCINATION_DIAGRAM_REFUSAL_BLOCK,
    HALLUCINATION_INPUT_LABEL,
    HALLUCINATION_INDICATOR_ENTITY,
    HALLUCINATION_INDICATOR_REFUSAL,
    HALLUCINATION_MISFIRE_TEMPLATE,
    HALLUCINATION_PROMPTS,
    HALLUCINATION_RESPONSES,
    HALLUCINATION_TRACE_BUTTON,
    KNOWN_NAMES,
    MISFIRE_NAMES,
    UNKNOWN_NAMES,
    UI_LABELS,
)
from components.ui import render_callout, render_discussion_prompts, render_indicator_card


def _classify(raw: str) -> tuple[str, str, str, str, str]:
    """Returns tier, refusal status, refusal desc, entity status, entity desc."""
    name = raw.strip()
    if not name:
        return (
            "",
            "inactive",
            "Idle until a name is supplied.",
            "silent",
            "No recognised entity signal.",
        )
    key = name.lower()
    if key in KNOWN_NAMES:
        return (
            "known",
            "inhibited",
            "Answer path enabled: refusal suppressed for recognised public figures.",
            "active",
            "Strong ‘known entity’ activation; factual associations retrieved.",
        )
    if key in UNKNOWN_NAMES:
        return (
            "unknown",
            "active",
            "Default refusal circuit runs end-to-end.",
            "silent",
            "No confident entity match; no inhibition of refusal.",
        )
    if key in MISFIRE_NAMES:
        return (
            "misfire",
            "inhibited",
            "Refusal partially suppressed despite thin factual grounding.",
            "partial",
            "Entity-like signal without veridical knowledge → confident fabrication risk.",
        )
    return (
        "unknown",
        "active",
        "Treat as unknown in this demo: default refusal applies.",
        "silent",
        "No hardcoded tier; maps to cautious behaviour for discussion.",
    )


def _response_text(name: str, tier: str) -> str:
    if not tier:
        return HALLUCINATION_RESPONSES["default"]
    if tier == "known":
        return HALLUCINATION_RESPONSES["known"]
    if tier == "unknown":
        return HALLUCINATION_RESPONSES["unknown"]
    return HALLUCINATION_MISFIRE_TEMPLATE.format(name=name.strip() or "This person")


def render() -> None:
    st.text_input(HALLUCINATION_INPUT_LABEL, key="hallucination_input")

    if st.button(HALLUCINATION_TRACE_BUTTON, key="hallucination_trace"):
        raw = str(st.session_state.get("hallucination_input", "")).strip()
        st.session_state["hallucination_traced_name"] = raw

    traced = st.session_state.get("hallucination_traced_name")
    if traced is not None:
        tier, rs, rd, es, ed = _classify(traced)
        render_indicator_card(HALLUCINATION_INDICATOR_REFUSAL, rs, rd)
        render_indicator_card(HALLUCINATION_INDICATOR_ENTITY, es, ed)

        st.markdown(f"**{HALLUCINATION_CIRCUIT_TITLE}**")
        c1, c2, c3 = st.columns([2, 1, 2])
        with c1:
            st.markdown(HALLUCINATION_DIAGRAM_ENTITY_BLOCK)
        with c2:
            st.markdown(HALLUCINATION_DIAGRAM_ARROW)
        with c3:
            st.markdown(HALLUCINATION_DIAGRAM_REFUSAL_BLOCK)

        with st.container(border=True):
            st.caption(UI_LABELS["hallucination_output"])
            st.markdown(_response_text(traced, tier))

    render_callout(HALLUCINATION_CALLOUT, "info")
    render_discussion_prompts(HALLUCINATION_PROMPTS)
