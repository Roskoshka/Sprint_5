from faker import Faker
fake = Faker()

class StellarBurgersTestData:

    #Тестовые данные для регистрации нового пользователя
    REG_NAME = "Алена"
    REG_EMAIL = fake.email()
    REG_PASSWORD = "123456"

    #Параметры для теста невалидного пароля
    WRONG_PASSWORD_PARAMETRIZE = ['1', '12345']

    #Тестовые данные для авторизации пользователя
    AUTH_EMAIL = "alenakalinovskaya7999@gmail.com"
    AUTH_PASSWORD = "123456"
