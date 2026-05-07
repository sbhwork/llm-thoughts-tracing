"""Reusable Streamlit rendering primitives."""

from __future__ import annotations

import html

import streamlit as st

from config import (
    COLOUR_DOT_ACTIVE,
    COLOUR_DOT_INACTIVE,
    COLOUR_DOT_INHIBITED,
    COLOUR_DOT_MISFIRE,
    COLOUR_DOT_PARTIAL,
    COLOUR_STEP_AMBER,
    COLOUR_STEP_GREEN,
    COLOUR_STEP_RED,
)
from data.content import DISCUSSION_PROMPTS_EXPANDER_LABEL


def render_callout(text: str, level: str) -> None:
    if level == "info":
        st.info(text)
    elif level == "warning":
        st.warning(text)
    elif level == "success":
        st.success(text)
    elif level == "error":
        st.error(text)
    else:
        st.info(text)


def _step_border_and_icon(status: str) -> tuple[str, str]:
    s = status.lower()
    if s == "green" or s == "success":
        return COLOUR_STEP_GREEN, "✓"
    if s == "amber" or s == "warning":
        return COLOUR_STEP_AMBER, "~"
    if s == "red" or s == "error":
        return COLOUR_STEP_RED, "✗"
    return COLOUR_STEP_AMBER, "•"


def render_step_trace(steps: list[dict[str, str]]) -> None:
    blocks: list[str] = []
    for step in steps:
        label = step.get("label", "")
        text = step.get("text", "")
        status = step.get("status", "amber")
        safe_label = html.escape(label)
        safe_text = html.escape(text)
        border, icon = _step_border_and_icon(status)
        body = (
            f"<p style='margin:0 0 6px 0;'><strong>{icon} {safe_label}</strong></p>"
        )
        if safe_text:
            body += f"<p style='margin:0; color:#374151;'>{safe_text}</p>"
        blocks.append(
            f'<div style="border-left: 4px solid {border}; padding: 10px 14px; margin: 10px 0; '
            f'background: #FAFAFA; border-radius: 4px;">'
            f"{body}</div>"
        )
    st.markdown("\n".join(blocks), unsafe_allow_html=True)


def _indicator_dot_colour(status: str) -> str:
    s = status.lower()
    mapping = {
        "active": COLOUR_DOT_ACTIVE,
        "inactive": COLOUR_DOT_INACTIVE,
        "misfire": COLOUR_DOT_MISFIRE,
        "inhibited": COLOUR_DOT_INHIBITED,
        "silent": COLOUR_DOT_INACTIVE,
        "partial": COLOUR_DOT_PARTIAL,
    }
    return mapping.get(s, COLOUR_DOT_INACTIVE)


def render_indicator_card(label: str, status: str, description: str) -> None:
    colour = _indicator_dot_colour(status)
    status_key = html.escape(status)
    safe_label = html.escape(label)
    safe_description = html.escape(description)
    st.markdown(
        f'<div style="border: 1px solid #E5E7EB; border-radius: 8px; padding: 12px 14px; background: #FFFFFF;">'
        f'<p style="margin:0 0 6px 0;"><span style="display:inline-block;width:10px;height:10px;'
        f"border-radius:999px;background:{colour};margin-right:8px;vertical-align:middle;"
        f'"></span><strong>{safe_label}</strong> '
        f'<span style="color:#6B7280;font-size:0.9em;">({status_key})</span></p>'
        f'<p style="margin:0;color:#374151;font-size:0.95em;">{safe_description}</p>'
        f"</div>",
        unsafe_allow_html=True,
    )


def render_tag(text: str, colour: str) -> None:
    safe = html.escape(text)
    st.markdown(
        f'<span style="display:inline-block;padding:2px 10px;border-radius:999px;'
        f"font-size:0.8rem;font-weight:600;color:#ffffff;background:{colour};"
        f'margin-right:8px;">{safe}</span>',
        unsafe_allow_html=True,
    )


def render_discussion_prompts(prompts: list[str] | tuple[str, ...]) -> None:
    lines = "\n".join(f"- {html.escape(p)}" for p in prompts)
    with st.expander(DISCUSSION_PROMPTS_EXPANDER_LABEL):
        st.markdown(lines, unsafe_allow_html=False)


def render_quote_block(title: str, body: str, monospace: bool = False) -> None:
    font = "ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace" if monospace else "inherit"
    style = "font-style: italic;" if not monospace else ""
    st.markdown(
        f'<div style="border-left: 4px solid #94A3B8; padding: 12px 16px; margin: 12px 0; '
        f'background: #F8FAFC; border-radius: 4px;">'
        f"<p style='margin:0 0 8px 0; font-weight: 600;'>{html.escape(title)}</p>"
        f"<p style='margin:0; {style} font-family: {font}; color: #334155;'>{html.escape(body)}</p>"
        "</div>",
        unsafe_allow_html=True,
    )


def render_highlight_box(text: str, variant: str) -> None:
    if variant == "danger":
        bg = "#FEF2F2"
        border = "#FECACA"
    else:
        bg = "#F0FDF4"
        border = "#BBF7D0"
    st.markdown(
        f'<div style="background:{bg}; border: 1px solid {border}; border-radius: 8px; '
        f'padding: 12px 14px; color: #1F2937;">{html.escape(text)}</div>',
        unsafe_allow_html=True,
    )
