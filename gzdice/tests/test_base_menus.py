import pytest

from gzdice.data.MenuObjects import menu_item
from ..menus import base_menus


@pytest.fixture
def mock_menu_list():
    whopos_dice = menu_item("w", "Whopos", "do_the_whopos")
    banana_fern = menu_item("bf", "Banana Fern", "Banana the Fern")
    return [whopos_dice, banana_fern]


def test_show_menu(mock_menu_list):
    assert (
        base_menus.show_menu(mock_menu_list)
        == "\nChoose your preferred option from the menu below by typing \
the shortcode or number for the option\nw: Whopos\nbf: Banana Fern\n"
    )


def test_selection(mock_menu_list, mocker):
    # mocked_main_menu = mocker.patch()
    test_choice = mock_menu_list[0].option_id
    assert (
        base_menus.selection(test_choice, mock_menu_list)
        == mock_menu_list[0].option_function
    )
