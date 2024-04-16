from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from data import StellarBurgersTestData
from locators import StellarBurgersLocators

class TestProfilePage:
    # Переход в личный кабинет
    def test_navigate_to_profile_page(self, driver):
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

        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.PROFILE_LINK))

        assert driver.find_element(*StellarBurgersLocators.PROFILE_LINK).is_displayed()
