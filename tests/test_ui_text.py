from pathlib import Path

from capital_gains_app.ui_text import ASSISTANT_FONT_FAMILY, RTL_MARK, app_root, ui_text


def test_hebrew_text_is_prepared_for_ltr_tk_widgets() -> None:
    rendered = ui_text("היי ליאת, יש קבצים לניתוח?")

    assert rendered.startswith(RTL_MARK)
    assert "תאיל ייה" in rendered
    assert ASSISTANT_FONT_FAMILY == "Assistant"


def test_assistant_font_asset_is_bundled() -> None:
    assert (app_root() / "assets" / "fonts" / "Assistant.ttf").exists()
    assert Path(app_root()).exists()
