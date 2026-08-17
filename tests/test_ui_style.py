import re
from pathlib import Path

from orthoxrd.ui_css import UI_CSS
from orthoxrd.ui_plot_theme import plot_layout
from orthoxrd.ui_style import ACCENT, AMBER, CANVAS, GREEN, RED, SURFACE, TEXT


def _css_rules(source: str) -> list[tuple[str, str]]:
    return [
        (selector.strip(), body)
        for selector, body in re.findall(r"([^{}]+)\{([^{}]+)\}", source)
    ]


def _selectors_setting(property_name: str) -> list[str]:
    return [
        selector
        for selector, body in _css_rules(UI_CSS)
        if re.search(rf"(^|;)\s*{re.escape(property_name)}\s*:", body)
    ]


def test_workbench_css_ships_visible_instrument_chrome() -> None:
    assert ".xrd-mast" in UI_CSS
    assert ".xrd-mark" in UI_CSS
    assert ".xrd-summary-grid" in UI_CSS
    assert "ibm-plex-sans" in UI_CSS.lower()
    assert "ibm-plex-mono" in UI_CSS.lower()
    app_source = (Path(__file__).parents[1] / "orthoxrd" / "ui_app.py").read_text(
        encoding="utf-8"
    )
    assert 'class="xrd-mast"' in app_source
    assert 'class="xrd-mark"' in app_source


def test_workbench_css_keeps_functional_palette() -> None:
    assert "--xrd-bg: #0b0f14" in UI_CSS
    assert "--xrd-surface: #121821" in UI_CSS
    assert f"--xrd-accent: {ACCENT}" in UI_CSS
    assert f"--xrd-warning: {AMBER}" in UI_CSS
    assert f"--xrd-error: {RED}" in UI_CSS
    assert f"--xrd-valid: {GREEN}" in UI_CSS
    assert "font-variant-numeric: tabular-nums" in UI_CSS
    assert "outline: 2px solid var(--xrd-accent)" in UI_CSS


def test_workbench_css_rejects_landing_chrome() -> None:
    lowered = UI_CSS.lower()
    assert "hero" not in lowered
    assert "blob" not in lowered
    assert "linear-gradient" not in lowered
    assert "radial-gradient" not in lowered
    assert "100vh" not in lowered


def test_workbench_css_does_not_override_material_icon_font() -> None:
    for selector in _selectors_setting("font-family"):
        assert "st-emotion" not in selector
        assert '[class*="st-emotion"]' not in selector


def test_workbench_css_does_not_repaint_alert_paragraphs() -> None:
    for selector in _selectors_setting("color"):
        parts = [part.strip() for part in selector.split(",")]
        paints_paragraph = any(part in {"p", "label"} or part.startswith("p ") for part in parts)
        if not paints_paragraph:
            continue
        assert "stAlert" in selector


def test_plot_layout_uses_workbench_surfaces() -> None:
    layout = plot_layout(height=420, x_title="2theta", y_title="I")
    assert layout["paper_bgcolor"] == CANVAS
    assert layout["plot_bgcolor"] == SURFACE
    assert layout["paper_bgcolor"] != "#ffffff"
    assert layout["plot_bgcolor"] != "#ffffff"
    assert layout["font"]["color"] == TEXT
    assert layout["height"] == 420
    assert layout["xaxis"]["title"] == "2theta"
