UI_CSS = r"""
<style>
@import url("https://fonts.bunny.net/css?family=ibm-plex-mono:500,600|ibm-plex-sans:400,500,600,700");
:root {
  color-scheme: dark;
  --xrd-bg: #0b0f14;
  --xrd-surface: #121821;
  --xrd-control: #18202b;
  --xrd-hover: #1c2633;
  --xrd-border: #2a3441;
  --xrd-hairline: #1e2733;
  --xrd-text: #f3f6fa;
  --xrd-muted: #aeb8c5;
  --xrd-accent: #22c7d6;
  --xrd-warning: #f2b84b;
  --xrd-error: #ff5a67;
  --xrd-valid: #48c78e;
  --xrd-ink: #071014;
  --xrd-shadow: 0 8px 20px rgba(7, 16, 24, 0.28);
  --xrd-radius: 6px;
  --xrd-radius-outer: 8px;
  --xrd-font-sans: "IBM Plex Sans", "Segoe UI Variable", "Segoe UI", system-ui, sans-serif;
  --xrd-font-mono: "IBM Plex Mono", "Cascadia Mono", Consolas, ui-monospace, monospace;
}
html, body, .stApp {
  font-family: var(--xrd-font-sans);
  font-variant-numeric: tabular-nums;
}
.stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
  background: var(--xrd-bg);
  color: var(--xrd-text);
}
[data-testid="stHeader"] {
  background: var(--xrd-bg);
  border-bottom: 1px solid var(--xrd-hairline);
}
[data-testid="stToolbar"],
footer, #MainMenu { visibility: hidden; height: 0; }
.block-container {
  width: min(100%, 1480px);
  max-width: 1480px;
  padding: 12px 20px 24px;
}
h1, h2, h3, h4, h5, p, label, span, div {
  letter-spacing: 0;
}
h1 {
  margin: 0;
  font-size: clamp(1.28rem, 1.8vw, 1.72rem);
  font-weight: 650;
  letter-spacing: -0.02em;
  line-height: 1.18;
}
h2 {
  font-size: 1.12rem;
  font-weight: 620;
  letter-spacing: -0.015em;
}
h3, h4 {
  font-size: 0.98rem;
  font-weight: 600;
}
[data-testid="stWidgetLabel"] p {
  font-size: 0.8rem;
  font-weight: 500;
  color: var(--xrd-muted);
}
[data-testid="stVerticalBlockBorderWrapper"] {
  background: var(--xrd-surface);
  border-color: var(--xrd-border);
  border-radius: var(--xrd-radius-outer);
}
[data-baseweb="popover"] {
  background: var(--xrd-surface);
  border: 1px solid var(--xrd-border);
  border-radius: var(--xrd-radius-outer);
  box-shadow: var(--xrd-shadow);
}
div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div,
div[data-baseweb="textarea"] > div {
  min-height: 40px;
  background: var(--xrd-control) !important;
  border-color: var(--xrd-border) !important;
  border-radius: var(--xrd-radius) !important;
  color: var(--xrd-text) !important;
  box-shadow: inset 0 1px 0 rgba(243, 246, 250, 0.04);
}
div[data-baseweb="select"] > div:hover,
div[data-baseweb="input"] > div:hover,
div[data-baseweb="textarea"] > div:hover {
  border-color: #3a4758;
  background: var(--xrd-hover);
}
div[data-baseweb="select"] input,
div[data-baseweb="input"] input,
textarea {
  color: var(--xrd-text) !important;
  font-family: var(--xrd-font-mono);
}
button:focus-visible,
input:focus-visible,
textarea:focus-visible,
select:focus-visible,
[role="button"]:focus-visible,
[data-baseweb="select"] > div:focus-within,
[data-baseweb="input"] > div:focus-within {
  outline: 2px solid var(--xrd-accent) !important;
  outline-offset: 2px;
}
.stButton > button,
.stDownloadButton > button,
[data-testid="stPopover"] > button {
  min-height: 40px;
  background: var(--xrd-control) !important;
  color: var(--xrd-text) !important;
  border: 1px solid var(--xrd-border) !important;
  border-radius: var(--xrd-radius) !important;
  font-family: var(--xrd-font-sans) !important;
  font-weight: 600;
  letter-spacing: 0.01em;
  transition: border-color 160ms ease, background 160ms ease, transform 120ms ease;
}
.stButton > button:hover,
.stDownloadButton > button:hover,
[data-testid="stPopover"] > button:hover {
  border-color: var(--xrd-accent);
  background: var(--xrd-hover);
  color: var(--xrd-text);
}
.stButton > button:active,
.stDownloadButton > button:active,
[data-testid="stPopover"] > button:active {
  transform: translateY(1px);
}
.stButton > button[kind="primary"],
.stDownloadButton > button[kind="primary"] {
  background: var(--xrd-accent) !important;
  border-color: var(--xrd-accent) !important;
  color: var(--xrd-ink) !important;
}
.stButton > button[kind="primary"]:hover,
.stDownloadButton > button[kind="primary"]:hover {
  background: #3ad4e1 !important;
  border-color: #3ad4e1 !important;
  color: var(--xrd-ink) !important;
}
button:disabled,
.stButton > button:disabled,
.stDownloadButton > button:disabled {
  color: #7f8a98 !important;
  background: #10161e !important;
  border-color: #222b36 !important;
  opacity: 1 !important;
  transform: none !important;
}
[data-testid="stButtonGroup"] {
  margin: 2px 0 12px;
  gap: 0;
  width: 100%;
  border: 1px solid var(--xrd-border);
  border-radius: var(--xrd-radius);
  overflow: hidden;
  background: var(--xrd-surface);
}
[data-testid="stButtonGroup"] button {
  min-height: 38px;
  border-radius: 0 !important;
  border: 0 !important;
  border-right: 1px solid var(--xrd-border) !important;
  background: transparent !important;
  color: var(--xrd-muted) !important;
  font-family: var(--xrd-font-sans) !important;
  font-weight: 600 !important;
}
[data-testid="stButtonGroup"] button:last-child {
  border-right: 0 !important;
}
[data-testid="stButtonGroup"] button:hover {
  background: var(--xrd-hover) !important;
  color: var(--xrd-text) !important;
}
[data-testid="stButtonGroup"] button[aria-checked="true"],
[data-testid="stButtonGroup"] button[kind="primary"] {
  background: var(--xrd-accent) !important;
  color: var(--xrd-ink) !important;
  box-shadow: none;
}
[data-testid="stDataFrame"] {
  overflow: hidden;
  border: 1px solid var(--xrd-border);
  border-radius: var(--xrd-radius);
}
[data-testid="stDataFrame"] thead tr {
  background: var(--xrd-control);
}
[data-testid="stDataFrame"] tbody tr:nth-child(even) {
  background: rgba(24, 32, 43, 0.35);
}
[data-testid="stCaptionContainer"],
[data-testid="stCaptionContainer"] p {
  color: var(--xrd-muted);
  font-size: 0.8rem;
  line-height: 1.45;
}
[data-testid="stAlert"] {
  border-radius: var(--xrd-radius);
}
[data-testid="stFileUploaderDropzone"] {
  background: var(--xrd-control);
  border-color: var(--xrd-border);
  border-radius: var(--xrd-radius);
}
[data-testid="stForm"] {
  border-color: var(--xrd-border);
  border-radius: var(--xrd-radius-outer);
  background: var(--xrd-surface);
}
[data-testid="stSlider"] [role="slider"] {
  background: var(--xrd-accent);
}
hr, [data-testid="stMarkdown"] hr {
  border: 0;
  border-top: 1px solid var(--xrd-hairline);
  margin: 10px 0;
}
.xrd-mast {
  display: flex;
  align-items: center;
  gap: 14px;
  min-width: 0;
  padding: 10px 12px;
  border: 1px solid var(--xrd-border);
  border-left: 4px solid var(--xrd-accent);
  border-radius: var(--xrd-radius-outer);
  background: var(--xrd-surface);
}
.xrd-mark {
  flex: 0 0 44px;
  width: 44px;
  height: 44px;
  display: grid;
  place-items: center;
  background: var(--xrd-accent);
  color: var(--xrd-ink);
  font: 700 0.92rem/1 var(--xrd-font-mono);
  letter-spacing: 0.04em;
  border-radius: var(--xrd-radius);
}
.xrd-mast-copy { min-width: 0; flex: 1; }
.xrd-titlebar {
  display: flex;
  align-items: baseline;
  gap: 10px;
  min-width: 0;
}
.xrd-titlebar h1 {
  font-family: var(--xrd-font-sans);
}
.xrd-model-tag {
  display: inline-block;
  padding: 3px 8px;
  border-radius: 999px;
  background: rgba(34, 199, 214, 0.16);
  color: var(--xrd-accent);
  font: 600 .72rem/1.2 var(--xrd-font-mono);
  letter-spacing: 0.03em;
  white-space: nowrap;
}
.xrd-subtitle {
  margin-top: 4px;
  color: var(--xrd-muted);
  font-size: .82rem;
  line-height: 1.4;
  max-width: 78ch;
}
.xrd-summary-grid {
  display: grid;
  grid-template-columns: repeat(9, minmax(92px, 1fr));
  gap: 0;
  margin: 8px 0 10px;
  overflow: hidden;
  border: 1px solid var(--xrd-border);
  border-radius: var(--xrd-radius);
  background: var(--xrd-surface);
}
.xrd-summary-grid .xrd-summary-card {
  min-width: 0;
  padding: 9px 10px 10px;
  border-right: 1px solid var(--xrd-hairline);
  background: transparent;
}
.xrd-summary-grid .xrd-summary-card:last-child { border-right: 0; }
.xrd-summary-label {
  color: var(--xrd-muted);
  font-size: .64rem;
  font-weight: 600;
  letter-spacing: 0.04em;
  line-height: 1.2;
}
.xrd-summary-value {
  margin-top: 5px;
  overflow: hidden;
  color: var(--xrd-accent);
  font: 600 1.02rem/1.15 var(--xrd-font-mono);
  font-variant-numeric: tabular-nums;
  text-overflow: ellipsis;
  white-space: nowrap;
}
.xrd-note, .xrd-readout-card, .xrd-state {
  border: 1px solid var(--xrd-border);
  border-radius: var(--xrd-radius);
  background: var(--xrd-control);
  padding: 8px 10px;
  color: var(--xrd-muted);
  font-size: .8rem;
  line-height: 1.45;
}
.xrd-readout-card {
  min-height: 72px;
}
.xrd-readout-label {
  color: var(--xrd-muted);
  font-size: .72rem;
}
.xrd-readout-value {
  margin-top: 5px;
  color: var(--xrd-text);
  font: 600 1rem/1.2 var(--xrd-font-mono);
  font-variant-numeric: tabular-nums;
}
.xrd-readout-meta {
  margin-top: 3px;
  color: var(--xrd-muted);
  font-size: .7rem;
}
.xrd-state--warning {
  border-color: rgba(242,184,75,.65);
  color: #f6d58f;
}
.xrd-state--valid {
  border-color: rgba(72,199,142,.58);
  color: #8be0b7;
}
.xrd-kpi-row {
  display: grid;
  grid-template-columns: repeat(4, minmax(100px, 1fr));
  gap: 6px;
  margin: 8px 0;
}
.xrd-kpi-row .xrd-summary-card {
  min-width: 0;
  padding: 8px 10px;
  background: var(--xrd-surface);
  border: 1px solid var(--xrd-border);
  border-radius: var(--xrd-radius);
}
code, pre, kbd {
  font-family: var(--xrd-font-mono);
}
@media (prefers-reduced-motion: reduce) {
  .stButton > button,
  .stDownloadButton > button,
  [data-testid="stPopover"] > button {
    transition: none;
  }
}
@media (max-width: 900px) {
  .block-container { padding: .65rem .75rem 1.25rem; }
  .xrd-titlebar { flex-wrap: wrap; }
  .xrd-summary-grid { grid-template-columns: repeat(4, minmax(86px, 1fr)); }
  .xrd-summary-grid .xrd-summary-card { border-bottom: 1px solid var(--xrd-hairline); }
  .xrd-kpi-row { grid-template-columns: repeat(2, minmax(100px, 1fr)); }
  [data-testid="stHorizontalBlock"] { flex-wrap: wrap; }
  [data-testid="stColumn"] {
    min-width: min(100%, 260px) !important;
    flex: 1 1 calc(50% - .5rem) !important;
  }
}
@media (max-width: 520px) {
  .block-container { padding: .5rem .55rem 1rem; }
  .xrd-titlebar { align-items: flex-start; flex-direction: column; gap: 4px; }
  .xrd-summary-grid { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .xrd-kpi-row { grid-template-columns: repeat(2, minmax(0, 1fr)); }
  .xrd-summary-card { padding: 7px 8px; }
  [data-testid="stHorizontalBlock"] { flex-wrap: wrap; }
  [data-testid="stColumn"] { min-width: min(100%, 240px) !important; flex: 1 1 100% !important; }
}
</style>
"""