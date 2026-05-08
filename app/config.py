"""Single source of truth for layout, navigation, and theme colours."""

PAGE_TITLE = "AI Thought Tracer"
PAGE_LAYOUT = "wide"

ANTHROPIC_RESEARCH_URL = "https://www.anthropic.com/research/tracing-thoughts-language-model"

PANEL_ORDER: list[tuple[str, str]] = [
    ("multilingual", "Multilingual thought"),
    ("poetry", "Poetry planning"),
    ("mental_math", "Mental math"),
    ("reasoning", "Faithful vs. motivated"),
    ("hallucination", "Hallucination"),
    ("jailbreak", "Jailbreak anatomy"),
]

TAG_COLOURS: dict[str, str] = {
    "multilingual": "#1E64C8",
    "poetry": "#7C3AED",
    "mental_math": "#D97706",
    "reasoning": "#D97706",
    "hallucination": "#059669",
    "jailbreak": "#DC2626",
}

# HTML / step-trace / UI accents (light theme)
COLOUR_STEP_GREEN = "#16A34A"
COLOUR_STEP_AMBER = "#D97706"
COLOUR_STEP_RED = "#DC2626"

COLOUR_CARD_BORDER = "#E5E7EB"
COLOUR_CARD_BG = "#FAFAFA"

COLOUR_DOT_ACTIVE = "#16A34A"
COLOUR_DOT_INACTIVE = "#9CA3AF"
COLOUR_DOT_MISFIRE = "#D97706"
COLOUR_DOT_PARTIAL = "#CA8A04"
COLOUR_DOT_INHIBITED = "#64748B"

COLOUR_PHASE_DANGER_BG = "#FEF2F2"
COLOUR_PHASE_DANGER_BORDER = "#FECACA"
COLOUR_PHASE_SAFE_BG = "#F0FDF4"
COLOUR_PHASE_SAFE_BORDER = "#BBF7D0"

COLOUR_QUOTE_BOX_BG = "#F8FAFC"
COLOUR_QUOTE_BOX_BORDER = "#CBD5E1"
