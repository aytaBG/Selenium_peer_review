from selenium import webdriver
from selenium.webdriver.chrome.options import Options as options_chrome
from selenium.webdriver.firefox.options import Options as options_firefox
import pytest


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='Chrome',
                     help='Choose browser: Chrome or Firefox')
    parser.addoption('--language', action='store', default='ru',
                     help='Choose language: ru, ')


@pytest.fixture()
def browser_select(request):
    user_language = request.config.getoption('language')
    browser_name = request.config.getoption('browser_name')
    browser = None
    if browser_name == 'Chrome':
        options = options_chrome()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        print('\nStarting Chrome for test..')
        browser = webdriver.Chrome(options=options)
    elif browser_name == 'Firefox':
        options = options_firefox()
        options.set_preference('intl.accept_languages', user_language)
        print('\nStarting Firefox for test ..')
        browser = webdriver.Firefox(options=options)
    else:
        raise pytest.UsageError('--browser_name should be Chrome or Firefox')
    yield browser
    print('\nClosing browser after test')
    browser.quit()
