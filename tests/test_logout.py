from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators import StellarBurgersLocators
import settings

class TestLogout:
    # Выход по кнопке «Выйти» в личном кабинете
    def test_logout(self, driver, login):
        driver.find_element(*StellarBurgersLocators.ACCOUNT_HEADER_LINK).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.PROFILE_LINK))

        driver.find_element(*StellarBurgersLocators.LOGOUT_BUTTON).click()

        WebDriverWait(driver, settings.MAX_WAIT_TIME).until(
            expected_conditions.visibility_of_element_located(StellarBurgersLocators.LOGIN_TITLE))

        assert driver.find_element(*StellarBurgersLocators.LOGIN_TITLE).is_displayed()
