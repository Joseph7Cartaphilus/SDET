import pytest
from selenium import webdriver
from pages.practice_form import PracticePage


@pytest.fixture
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://demoqa.com/automation-practice-form")
    yield driver
    driver.quit()


def test_registration_form(setup):
    registration_page = PracticePage(setup)

    registration_page.fill_first_name("John")
    registration_page.fill_last_name("Doe")
    registration_page.fill_email("john.doe@example.com")

    registration_page.select_gender()

    registration_page.fill_mobile("1234567890")
    registration_page.select_date_of_birth("10 Oct 1990")
    registration_page.fill_subjects("Maths")

    registration_page.upload_picture()

    registration_page.fill_address("123 Main St, Anytown")
    registration_page.select_state("NCR")
    registration_page.select_city("Delhi")

    registration_page.submit_form()

    assert "Thanks for submitting the form" in setup.page_source
