import pytest
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from data import StellarBurgersTestData
from locators import StellarBurgersLocators


class TestRegistration:

    # Успешная регистрация
    def test_registration_success(self, driver):
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_HEADER_LINK))

        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_ACCOUNT_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.REGISTRATION_TITLE))

        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_INPUT).send_keys(StellarBurgersTestData.REG_NAME)

        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_INPUT).send_keys(StellarBurgersTestData.REG_EMAIL)

        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_INPUT).send_keys(StellarBurgersTestData.REG_PASSWORD)

        driver.find_element(*StellarBurgersLocators.REGISTRATION_SUBMIT_BUTTON).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))

        assert driver.find_element(*StellarBurgersLocators.LOGIN_TITLE).is_displayed()

    # Ошибка для некорректного пароля
    @pytest.mark.parametrize('wrong_password', StellarBurgersTestData.WRONG_PASSWORD_PARAMETRIZE)
    def test_registration_invalid_password(self, driver, wrong_password):
        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.element_to_be_clickable(StellarBurgersLocators.ACCOUNT_HEADER_LINK))

        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()
        driver.find_element(*StellarBurgersLocators.REGISTRATION_ACCOUNT_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.REGISTRATION_TITLE))

        driver.find_element(*StellarBurgersLocators.REGISTRATION_NAME_INPUT).send_keys(StellarBurgersTestData.REG_NAME)

        driver.find_element(*StellarBurgersLocators.REGISTRATION_EMAIL_INPUT).send_keys(StellarBurgersTestData.REG_EMAIL)

        driver.find_element(*StellarBurgersLocators.REGISTRATION_PASSWORD_INPUT).send_keys(wrong_password)

        driver.find_element(*StellarBurgersLocators.REGISTRATION_SUBMIT_BUTTON).click()

        assert driver.find_element(*StellarBurgersLocators.NOTIFICATION_REG_INVALID_PASSWORD).text == "Некорректный пароль"
