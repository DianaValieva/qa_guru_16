"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest

from selene import have
from selenium import webdriver
from selene import browser


@pytest.fixture(params=["1536*864", "1920*1080", "516*800", "720*1100"])
def browser2(request):
    [width, height] = request.param.split("*")
    browser.config.driver=webdriver.Chrome()
    browser.driver.set_window_size(width, height)
    yield browser
    browser.quit()


def test_github_desktop(browser2):
    size = browser2.driver.get_window_size()
    if ((size["width"] == 516 and size["height"] == 800) or
            (size["width"] == 720 and size["height"] == 1100)):
        pytest.skip("неподходящий размер для desktop версии")
    browser2.open("https://github.com")
    browser2.element('.HeaderMenu-link--sign-in').press_enter()
    browser2.element(".auth-form-header").should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser2):
    size = browser2.driver.get_window_size()
    if ((size["width"] == 1536 and size["height"] == 864) or
            (size["width"] == 1920 and size["height"] == 1080)):
        pytest.skip("неподходящий размер для мобильной версии")
    browser2.open("https://github.com")
    browser.element('a[href*="login"]').press_enter()
    browser.element(".auth-form-header").should(have.exact_text('Sign in to GitHub'))
