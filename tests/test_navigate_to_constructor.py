from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import settings
from locators import StellarBurgersLocators

class TestNavigateToConstructor:
    # Переход из личного кабинета по клику на «Конструктор»
    def test_navigate_from_personal_account_to_constructor_by_header(self, driver, login):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.PROFILE_LINK))

        driver.find_element(*StellarBurgersLocators.CONSTRUCTOR_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_THE_ORDER_BUTTON))

        assert driver.find_element(*StellarBurgersLocators.MAKE_THE_ORDER_BUTTON).is_displayed()

    # Переход из личного кабинета по клику логотип Stellar Burgers
    def test_navigate_from_personal_account_to_constructor_by_logo(self, driver, login):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.PROFILE_LINK))

        driver.find_element(*StellarBurgersLocators.LOGO_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.MAKE_THE_ORDER_BUTTON))

        assert driver.find_element(*StellarBurgersLocators.MAKE_THE_ORDER_BUTTON).is_displayed()
