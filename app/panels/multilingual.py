"""Panel 1: multilingual conceptual space."""

from __future__ import annotations

import streamlit as st

from config import NAV_ACTIVE_SUFFIX
from data.content import (
    MULTILINGUAL_CALLOUT,
    MULTILINGUAL_FEATURES,
    MULTILINGUAL_LABELS,
    MULTILINGUAL_LANGUAGES,
    MULTILINGUAL_OUTPUTS,
    MULTILINGUAL_PROMPTS,
    MULTILINGUAL_QUERIES,
    UI_LABELS,
)
from components.ui import render_callout, render_discussion_prompts, render_indicator_card
from utils.state import set_multilingual_lang


def render() -> None:
    langs = list(MULTILINGUAL_LANGUAGES)
    cols = st.columns(len(langs))
    for col, code in zip(cols, langs):
        with col:
            base = MULTILINGUAL_LABELS[code]
            shown = f"{base}{NAV_ACTIVE_SUFFIX}" if st.session_state["multilingual_lang"] == code else base
            st.button(
                shown,
                key=f"lang_{code}",
                on_click=set_multilingual_lang,
                args=(code,),
                type="secondary",
                use_container_width=True,
            )

    lang = st.session_state["multilingual_lang"]

    with st.container(border=True):
        st.caption(UI_LABELS["input_query_card"])
        st.markdown(f"**{MULTILINGUAL_QUERIES[lang]}**")

    st.subheader(UI_LABELS["feature_activation"])
    fcols = st.columns(3)
    for col, feat in zip(fcols, MULTILINGUAL_FEATURES):
        with col:
            render_indicator_card(
                feat["label"],
                "active",
                feat["description"],
            )

    with st.container(border=True):
        st.caption(UI_LABELS["output_card"])
        st.markdown(f"**{MULTILINGUAL_OUTPUTS[lang]}**")

    render_callout(MULTILINGUAL_CALLOUT, "info")
    render_discussion_prompts(MULTILINGUAL_PROMPTS)
