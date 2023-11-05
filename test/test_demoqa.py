from qaguru.pages.registration_page import RegistrationPage
from qaguru.data.user import User
import allure
from allure_commons.types import Severity

registration_page = RegistrationPage()


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.feature("Регистрация пользователя")
def test_demoqa():
    user = User(first_name='Anna',
                last_name='Torgova',
                email='test_anna@mail.ru',
                gender='Female',
                phone_number='7999000112',
                month_of_birth='November',
                year_of_birth='1996',
                day_of_birth='26',
                subject='Arts',
                hobby='Sports, Reading, Music',
                picture='test.jpg',
                current_address='Saint-Petersburg',
                country='NCR',
                city='Delhi')

    registration_page.open()
    registration_page.register(user)
    registration_page.user_must_be_registered(user)
