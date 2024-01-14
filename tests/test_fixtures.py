"""
Сделайте разные фикстуры для каждого теста, которые выставят размеры окна браузера
"""
from selene import have
from selene import browser


def test_github_desktop(browser_desktop):
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-in').press_enter()
    browser.element(".auth-form-header").should(have.exact_text('Sign in to GitHub'))
    pass


def test_github_mobile(browser_mobile):
    browser.open("https://github.com")
    browser.element('a[href*="login"]').press_enter()
    browser.element(".auth-form-header").should(have.exact_text('Sign in to GitHub'))
    pass
