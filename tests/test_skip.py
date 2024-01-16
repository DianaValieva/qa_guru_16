"""
Параметризуйте фикстуру несколькими вариантами размеров окна
Пропустите мобильный тест, если соотношение сторон десктопное (и наоборот)
"""
import pytest

from selene import have
from selene import browser


@pytest.fixture(params=["1536*864", "1920*1080", "516*800", "720*1100"])
def browser2(request):
    [width, height] = request.param.split("*")
    browser.config.window_width = width
    browser.config.window_height = height
    if (width, height) in [("516", "800"), ("720", "1100")]:
        return 'mobile'
    if (width, height) in [("1536", "864"), ("1920", "1080")]:
        return 'desktop'


def test_github_desktop(browser2):
    if browser2 == "mobile":
        pytest.skip("неподходящий размер для desktop версии")
    browser.open("https://github.com")
    browser.element('.HeaderMenu-link--sign-in').press_enter()
    browser.element(".auth-form-header").should(have.exact_text('Sign in to GitHub'))


def test_github_mobile(browser2):
    if browser2 == "desktop":
        pytest.skip("неподходящий размер для мобильной версии")
    browser.open("https://github.com")
    browser.element('a[href*="login"]').press_enter()
    browser.element(".auth-form-header").should(have.exact_text('Sign in to GitHub'))
