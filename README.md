# Sprint_5
## Финальный проект - Спринт 5

Автотесты для сервиса https://stellarburgers.nomoreparties.site/

### Проект содержит:

Папка testы - здесь лежат файлы с тестами, для каждой функциональности свой файл.
Файл conftest.py - фикстуры, необходимые для запуска тестов.
Файл data.py - тестовые данные для запуска тестов.
Файл locators.py - локаторы, используемые в тестах.
Файл settings - настройки для проекта.
Файд README.md - полное описание проекта.

### Описание тестов из папки tests:

**Регистрация** - test_registration.py:
* test_registration_success - Успешная регистрация

**Вход** - test_login.py:
* test_login_by_button_login_in_main_page - Вход по кнопке «Войти в аккаунт» на главной
* test_login_by_button_personal_account_in_header - Вход через кнопку «Личный кабинет»
* test_login_by_button_login_in_registration_form - Вход через кнопку "Войти" в форме регистрации
* test_login_by_button_login_in_forgot_password_form - Вход через кнопку "Войти" в форме восстановления пароля

**Переход в личный кабинет** - test_profile_page.py:
* test_navigate_to_profile_page - Переход в личный кабинет

**Переход из личного кабинета в конструктор** - test_navigate_to_constructor:
* test_navigate_from_personal_account_to_constructor_by_header - Переход из личного кабинета по клику на «Конструктор»
* test_navigate_from_personal_account_to_constructor_by_logo - Переход из личного кабинета по клику логотип Stellar Burgers

**Выход из аккаунта** - test_logout.py:
* test_logout - Выход по кнопке «Выйти» в личном кабинете


**Раздел «Конструктор»** - test_constructor_section.py:
* test_navigate_to_sauces_tab - Переход к разделу «Соусы»
* test_navigate_to_fillings_tab - Переход к разделу «Начинки»
* test_navigate_to_buns_tab - Переход к разделу «Булки»

Команда для терминала, запускающая все тесты: `pytest -v`