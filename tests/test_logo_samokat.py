import constants


def test_scooter_logo_goes_to_main(order_page):

    # 1. Кликаем логотип "Самокат"
    order_page.click_scooter_logo()

    # 2. Проверяем, что попали на https://qa-scooter.praktikum-services.ru/
    assert constants.BASE_URL in order_page.current_url
