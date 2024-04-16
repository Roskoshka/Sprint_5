from locators import StellarBurgersLocators

class TestNavigateToConstructorTabs:
    # Переход к разделу «Соусы»
    def test_navigate_to_sauces_tab(self, driver, login):
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()
        assert driver.find_element(*StellarBurgersLocators.SELECTED_SECTION).text == 'Соусы'

    # Переход к разделу «Начинки»
    def test_navigate_to_fillings_tab(self, driver, login):
        driver.find_element(*StellarBurgersLocators.FILLINGS_SECTION).click()
        assert driver.find_element(*StellarBurgersLocators.SELECTED_SECTION).text == 'Начинки'

    # Переход к разделу «Булки»
    def test_navigate_to_buns_tab(self, driver, login):
        driver.find_element(*StellarBurgersLocators.SAUCES_SECTION).click()
        driver.find_element(*StellarBurgersLocators.BUNS_SECTION).click()
        assert driver.find_element(*StellarBurgersLocators.SELECTED_SECTION).text == 'Булки'
