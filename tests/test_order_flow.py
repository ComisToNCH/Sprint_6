import pytest
from src.data.order import ORDER_DATA_LIST

@pytest.mark.parametrize("test_data", ORDER_DATA_LIST)
def test_order_positive_flow(order_page, test_data):
    """
    Тест позитивного сценария заказа самоката.
    Берём набор данных из ORDER_DATA_LIST (src/data/order.py).
    """
    # 1. Заполнить первую часть формы
    order_page.fill_personal_data(
        test_data.name,
        test_data.surname,
        test_data.address,
        test_data.metro,
        test_data.phone
    )
    order_page.click_next_button()

    # 2. Заполнить вторую часть
    order_page.fill_rent_data(
        test_data.date,
        test_data.duration_text,
        test_data.color_black,
        test_data.color_grey,
        test_data.comment
    )
    order_page.click_order_button()

    # 3. Подтвердить заказ
    order_page.confirm_order_modal()

    # 4. Проверить, что заказ оформлен
    success_text = order_page.get_success_message()
    assert "Заказ оформлен" in success_text, (
        f"Не найдено подтверждение заказа. Текст: {success_text}"
    )
