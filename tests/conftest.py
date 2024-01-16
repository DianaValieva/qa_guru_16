import pytest

from selene import browser


@pytest.fixture(params=["1536*864", "1920*1080"])
def browser_desktop(request):
    [width, height] = request.param.split("*")
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


@pytest.fixture(scope='function', params=["516*800", "720*1100"])
def browser_mobile(request):
    [width, height] = request.param.split("*")
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()


@pytest.fixture(params=["1536*864", "1920*1080", "516*800", "720*1100"])
def browser_desktop_mobile(request):
    [width, height] = request.param.split("*")
    browser.config.window_width = width
    browser.config.window_height = height
    yield browser
    browser.quit()

