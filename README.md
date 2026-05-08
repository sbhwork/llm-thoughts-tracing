# AI Thought Tracer

An interactive **Streamlit** demo for reading groups, built around Anthropic’s interpretability work on [tracing the thoughts of a large language model](https://www.anthropic.com/research/tracing-thoughts-language-model). Six panels walk through case studies from the paper (multilingual representation, poetry planning, mental math, faithful vs. motivated reasoning, hallucination, and jailbreak dynamics). All “model” behaviour is **scripted from the paper**—there are **no live API calls**.

## Requirements

- Python 3.9+ (3.10+ recommended)
- Dependencies listed in `requirements.txt` (Streamlit ≥ 1.33 for bordered containers)

## Run locally

From the repository root:

```bash
pip install -r requirements.txt
cd app
streamlit run main.py
```

Then open the URL Streamlit prints (typically `http://localhost:8501`).

## Project layout

| Path | Role |
|------|------|
| `app/main.py` | Entry point: page config, sidebar, nav, panel routing |
| `app/config.py` | Title, panel order, tag colours, theme hex values |
| `app/data/content.py` | All copy and structured data (importable without Streamlit) |
| `app/components/ui.py` | Shared UI primitives (callouts, step traces, tags, …) |
| `app/components/layout.py` | Panel header, sidebar (about + glossary + visit count) |
| `app/panels/*.py` | One `render()` per case study |
| `app/utils/state.py` | `st.session_state` defaults and navigation helpers |

## Licence / attribution

The demo is an educational summary; cite Anthropic’s research when presenting the underlying findings.
