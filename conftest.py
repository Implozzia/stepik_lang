from selenium import webdriver
import pytest
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default='en', help="Choose language: ru, en, etc.")


@pytest.fixture()
def driver(request):
    user_language = request.config.getoption('language')
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
    print('\nStart browser for test: ')
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(3)
    yield driver
    print('\nBrowser quit ...')
    driver.quit()
