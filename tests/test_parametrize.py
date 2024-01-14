"""
Переопределите параметр с помощью indirect параметризации на уровне теста
"""
import pytest
from selene import browser
from selene import have


@pytest.mark.parametrize("browser_desktop_mobile", ["1536*864", "1920*1080"], indirect=True)
def test_github_desktop(browser_desktop_mobile):
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-in').press_enter()
    browser.element(".auth-form-header").should(have.exact_text('Sign in to GitHub'))
    pass


@pytest.mark.parametrize("browser_desktop_mobile", ["516*800", "720*1100"], indirect=True)
def test_github_mobile(browser_desktop_mobile):
    browser.open("https://github.com")
    browser.element('a[href*="login"]').press_enter()
    browser.element(".auth-form-header").should(have.exact_text('Sign in to GitHub'))
    pass
