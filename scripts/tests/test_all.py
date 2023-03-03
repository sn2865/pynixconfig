from scripts import get_color_code, get_font_code, get_full_path
from scripts import add_ls_colors, config


def test_color_code():
    assert get_color_code("red") == "31"
    assert get_color_code("blue") == "34"


def test_font_code():
    assert get_font_code("bold") == "1"


def test_get_full_path():
    assert get_full_path("~/.bashrc") == "/Users/sergionahas/.bashrc"


def test_config():
    assert config("31", "1") == "di=1;31"


def test_add_ls_colors():
    assert add_ls_colors("", "di=1;31") == '\nLS_COLORS="di=1;31"'
