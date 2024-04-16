from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from data import StellarBurgersTestData
from locators import StellarBurgersLocators

class TestLogin:
    # Вход по кнопке «Войти в аккаунт» на главной
    def test_login_by_button_login_in_main_page(self, driver):
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.LOGIN_BUTTON_MAIN))

        driver.find_element(*StellarBurgersLocators.LOGIN_BUTTON_MAIN).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(StellarBurgersTestData.AUTH_EMAIL)

        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_THE_ORDER_BUTTON))

        assert driver.find_element(*StellarBurgersLocators.MAKE_THE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку «Личный кабинет»
    def test_login_by_button_personal_account_in_header(self, driver):
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_HEADER_LINK))

        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(StellarBurgersTestData.AUTH_EMAIL)

        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_THE_ORDER_BUTTON))

        assert driver.find_element(*StellarBurgersLocators.MAKE_THE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку "Войти" в форме регистрации
    def test_login_by_button_login_in_registration_form(self, driver):
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_HEADER_LINK))

        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))

        driver.find_element(*StellarBurgersLocators.REGISTRATION_ACCOUNT_LINK).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_LINK).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(StellarBurgersTestData.AUTH_EMAIL)

        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(StellarBurgersTestData.AUTH_PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_THE_ORDER_BUTTON))

        assert driver.find_element(*StellarBurgersLocators.MAKE_THE_ORDER_BUTTON).is_displayed()

    # Вход через кнопку "Войти" в форме восстановления пароля
    def test_login_by_button_login_in_forgot_password_form(self, driver):
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_HEADER_LINK))

        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))

        driver.find_element(*StellarBurgersLocators.FORGOT_PASSWORD_LINK).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_LINK).click()

        driver.find_element(*StellarBurgersLocators.LOGIN_EMAIL_INPUT).send_keys(StellarBurgersTestData.AUTH_EMAIL)

        driver.find_element(*StellarBurgersLocators.LOGIN_PASSWORD_INPUT).send_keys(
            StellarBurgersTestData.AUTH_PASSWORD)

        driver.find_element(*StellarBurgersLocators.LOGIN_SUBMIT_BUTTON).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_THE_ORDER_BUTTON))

        assert driver.find_element(*StellarBurgersLocators.MAKE_THE_ORDER_BUTTON).is_displayed()
