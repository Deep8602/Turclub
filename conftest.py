import pytest
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium import webdriver
from utilities import settings
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    parser.addoption('--browser-name',
                     dest='browser_name',
                     type=str,
                     help='Browser name',
                     default='Chrome')

    parser.addoption('--base-url',
                     dest='base_url',
                     type=str,
                     help='Base URL',
                     default='tcb.com.ua')


@pytest.fixture()
def get_browser_name(request):
    request.cls.browser_name = request.config.getoption("--browser-name")
    settings.browser_name = request.cls.browser_name


@pytest.fixture()
def get_base_host(request):
    request.cls.base_host = request.config.getoption("--base-url")
    settings.base_host = request.cls.base_host


@pytest.fixture()
def get_base_url(request):
    base_host = request.config.getoption("--base-url")
    request.cls.base_url = 'https://{}/'.format(base_host)
    settings.base_url = request.cls.base_url


# @pytest.fixture(scope="function")
# def get_driver(request):
#     driver: WebDriver = webdriver.Chrome(executable_path=ChromeDriverManager().install())
#     request.cls.driver = driver
#     # driver.get('https://tcb.com.ua/login/')
#     yield
#     driver.close()


