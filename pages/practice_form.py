import os

from selenium.webdriver.common.by import By


class PracticePage:

    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "firstName")
        self.last_name_input = (By.ID, "lastName")
        self.email_input = (By.ID, "userEmail")
        self.gender_radio = (By.XPATH, "//label[text()='Male']")
        self.mobile_input = (By.ID, "userNumber")
        self.date_of_birth_input = (By.ID, "dateOfBirthInput")
        self.subjects_input = (By.ID, "subjectsInput")
        self.picture_upload = (By.ID, "uploadPicture")
        self.address_input = (By.ID, "currentAddress")
        self.state_dropdown = (By.ID, "react-select-3-input")
        self.city_dropdown = (By.ID, "react-select-4-input")
        self.submit_button = (By.CSS_SELECTOR, "#submit")

    def fill_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)

    def fill_email(self, email):
        self.driver.find_element(*self.email_input).send_keys(email)

    def select_gender(self, gender='Male'):
        self.driver.find_element(*self.gender_radio).click()

    def fill_mobile(self, mobile):
        self.driver.find_element(*self.mobile_input).send_keys(mobile)

    def select_date_of_birth(self, date):
        date_of_birth_element = self.driver.find_element(*self.date_of_birth_input)
        date_of_birth_element.clear()
        date_of_birth_element.send_keys(date)
        date_of_birth_element.click()

    def fill_subjects(self, subject):
        subjects_element = self.driver.find_element(*self.subjects_input)
        subjects_element.send_keys(subject)
        subjects_element.send_keys('\n')

    def upload_picture(self):
        data_dir = '/home/joseph/PycharmProjects/SDET/data'
        file_path = os.path.join(data_dir, 'test_image.jpg')

        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Файл не найден: {file_path}")

        self.driver.find_element(*self.picture_upload).send_keys(file_path)

    def fill_address(self, address):
        self.driver.find_element(*self.address_input).send_keys(address)

    def select_state(self, state):
        state_element = self.driver.find_element(*self.state_dropdown)
        state_element.send_keys(state)
        state_element.send_keys('\n')

    def select_city(self, city):
        city_element = self.driver.find_element(*self.city_dropdown)
        city_element.send_keys(city)
        city_element.send_keys('\n')

    def submit_form(self):
        submit_btn = self.driver.find_element(*self.submit_button)
        self.driver.execute_script("arguments[0].scrollIntoView();", submit_btn)
        submit_btn.click()
