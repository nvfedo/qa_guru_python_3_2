from selene.support.shared import browser
from selene import be, have

def test_should_find_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('selene').press_enter()
    browser.element('[id="search"]').should(have.text('yashaka/selene: User-oriented Web UI browser tests in Python'))

def test_shouldnt_find_selene(open_browser):
    browser.element('[name="q"]').should(be.blank).type('1231jkbzsnkb 12b3ui12bdasjklbasnd').press_enter()
    browser.element('#res').should(have.text('По запросу 1231jkbzsnkb 12b3ui12bdasjklbasnd ничего не найдено.'))