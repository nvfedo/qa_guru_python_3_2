from selene.support.shared import browser
import pytest

@pytest.fixture()
def set_browser_size_window():
    browser.config.window_height = 1080
    browser.config.window_width = 1920

@pytest.fixture()
def open_browser(set_browser_size_window):
    browser.open('https://google.com')