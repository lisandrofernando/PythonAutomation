import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--browser_name", action="store", default="chrome"
    )


@pytest.fixture(scope="class")
def set(request):
    browser_name = request.config.getoption("browser_name")
    if browser_name =="chrome":
        driver = webdriver.Chrome(executable_path='')
    elif browser_name =="firefox":
        driver = webdriver.Firefox(executable_path='')
    elif browser_name =="internetexplorer":
        driver = webdriver.Ie(executable_path='')
    driver.get('http://automationpractice.com/')
    driver.maximize_window()
    yield
    driver.close()