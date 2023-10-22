from qa_guru_8_10.pages.registration_page import RegistrationPage


def test_demoqa():
    registration_page = RegistrationPage()

    registration_page.open()

    registration_page.fill_first_name('Anna')
    registration_page.fill_last_name('Torgova')
    registration_page.fill_email('test_anna@mail.ru')
    registration_page.choose_a_gender('Female')
    registration_page.fill_number_phone('79990001122')
    registration_page.choose_date_of_birth(month='November', year=1996, day=26)
    registration_page.choose_subject('Arts')
    registration_page.choose_hobby_1('Sports')
    registration_page.choose_hobby_2('Reading')
    registration_page.choose_hobby_3('Music')
    registration_page.scroll_into_view()
    registration_page.download_picture('test.jpg')
    registration_page.current_adress('Saint-Petersburg')
    registration_page.choose_state('NCR')
    registration_page.choose_city('Delhi')
    registration_page.submit_form()

    registration_page.should_regustration_user(
        'Anna Torgova',
        'test_anna@mail.ru',
        'Female',
        '7999000112',
        '26 November,1996',
        'Arts',
        'Sports, Reading, Music',
        'test.jpg',
        'Saint-Petersburg',
        'NCR Delhi')
