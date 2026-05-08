"""Session state initialisation and navigation helpers."""

from __future__ import annotations

import streamlit as st

from config import PANEL_ORDER
from data import content as content_mod


def init_state() -> None:
    defaults = {
        "active_panel": PANEL_ORDER[0][0],
        "visited_panels": [],
        "multilingual_lang": "en",
        "poetry_mode": "none",
        "mental_math_a": content_mod.MENTAL_MATH_DEFAULT_A,
        "mental_math_b": content_mod.MENTAL_MATH_DEFAULT_B,
        "mental_math_show_trace": False,
        "reasoning_mode": "faithful",
        "hallucination_input": "",
        "hallucination_traced_name": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def get_active_panel() -> str:
    return str(st.session_state["active_panel"])


def set_active_panel(panel_id: str) -> None:
    st.session_state["active_panel"] = panel_id


def set_multilingual_lang(code: str) -> None:
    st.session_state["multilingual_lang"] = code


def set_poetry_mode(mode: str) -> None:
    st.session_state["poetry_mode"] = mode


def set_reasoning_mode(mode: str) -> None:
    st.session_state["reasoning_mode"] = mode


def touch_current_panel_visit() -> None:
    panel_id = get_active_panel()
    visited: list[str] = st.session_state["visited_panels"]
    if panel_id not in visited:
        visited.append(panel_id)
