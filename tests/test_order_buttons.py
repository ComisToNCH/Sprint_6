import pytest
import allure


@allure.title("Тест кнопки 'Заказать'")
@allure.description("Проверяет, что переход на страницу оформления происходит при нажатии на верхнюю или нижнюю кнопку 'Заказать'.")
@pytest.mark.parametrize("order_button", ["top", "bottom"])
def test_order_button(main_page, order_button):

    with allure.step(f"Нажать на кнопку 'Заказать' ({order_button})"):
        main_page.click_order_button(order_button)

    with allure.step("Проверить, что произошел переход на страницу оформления"):
        assert "order" in main_page.current_url, f"Переход не сработал при клике на кнопку {order_button}"