import pytest
from selenium import webdriver


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """
    Фиксирует директорию для генерации отчётов Allure
    """
    config.option.allure_report_dir = "reports"


@pytest.fixture
def setup():
    """
    Настройка фикстуры для тестов
    """
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
