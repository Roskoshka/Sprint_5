from selenium.webdriver.common.by import By

class StellarBurgersLocators:

    # Ссылка "Личный кабинет" в хедере
    ACCOUNT_HEADER_LINK = (By.XPATH, "//a[@href = '/account']")
    # Ссылка "Регистрация" на странице авторизации
    REGISTRATION_ACCOUNT_LINK = (By.XPATH, "//a[@href = '/register']")
    # Заголовок страницы "Регистрация"
    REGISTRATION_TITLE = (By.XPATH, "//h2[text() = 'Регистрация']")
    # Поле "Имя" на странице регистрации
    REGISTRATION_NAME_INPUT = (By.XPATH, "//label[text() = 'Имя']/following-sibling::input")
    # Поле "Email" на странице регистрации
    REGISTRATION_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    # Поле "Пароль" на странице регистрации
    REGISTRATION_PASSWORD_INPUT = (By.XPATH, "//input[@name='Пароль']")
    # Кнопка "Зарегистрироваться" на странице регистрации
    REGISTRATION_SUBMIT_BUTTON = (By.XPATH, "//button[text() = 'Зарегистрироваться']")
    # Ошибка валидации "Некорректный пароль" на странице регистрации
    NOTIFICATION_REG_INVALID_PASSWORD = (By.XPATH, "//p[text() = 'Некорректный пароль']")
    # Кнопка "Войти в аккаунт" на Главной
    LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text() = 'Войти в аккаунт']")
    # Заголовок страницы "Войти" на странице авторизации
    LOGIN_TITLE = (By.XPATH, "//h2[text() = 'Вход']")
    # Поле "Email" на странице авторизации
    LOGIN_EMAIL_INPUT = (By.XPATH, "//label[text() = 'Email']/following-sibling::input")
    # Поле "Пароль" на странице авторизации
    LOGIN_PASSWORD_INPUT = (By.XPATH, "//label[text() = 'Пароль']/following-sibling::input")
    # Кнопка "Войти" на странице авторизации
    LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text() = 'Войти']")
    # Ссылка "Восстановить пароль" на странице авторизации
    FORGOT_PASSWORD_LINK = (By.XPATH, "//a[text() = 'Восстановить пароль']")
    # Ссылка "Войти" на восстановления пароля на странице авторизации
    LOGIN_LINK = (By.XPATH, "//a[@href = '/login']")
    # Кнопка "Оформить заказ" в авторизованной зоне
    MAKE_THE_ORDER_BUTTON = (By.XPATH, "//button[text() = 'Оформить заказ']")
    # Ссылка "Профиль" в личном кабинете
    PROFILE_LINK = (By.XPATH, "//a[@href = '/account/profile']")
    # Ссылка "Конструктор" в хедере
    CONSTRUCTOR_LINK = (By.XPATH, "//p[text() = 'Конструктор']")
    # Ссылка "Логотип" в хедере
    LOGO_LINK = (By.XPATH, "//div[@class='AppHeader_header__logo__2D0X2']")
    # Кнопка "Выход" в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text() = 'Выход']")
    # Селект, обозначающий, что раздел выбран
    SELECTED_SECTION = (By.XPATH, "//div[@class = 'tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect']")
    # Раздел "Булки"
    BUNS_SECTION = (By.XPATH, "//span[text() = 'Булки']")
    # Раздел "Соусы"
    SAUCES_SECTION = (By.XPATH, "//span[text() = 'Соусы']")
    # Раздел "Начинки"
    FILLINGS_SECTION = (By.XPATH, "//span[text() = 'Начинки']")
