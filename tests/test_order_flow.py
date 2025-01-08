import pytest
from dataclasses import dataclass

@dataclass
class OrderTestData:
    name: str
    surname: str
    address: str
    metro: str
    phone: str
    date: str
    duration_text: str
    color_black: bool
    color_grey: bool
    comment: str

@pytest.mark.parametrize("test_data", [
    OrderTestData(
        name="Иван",
        surname="Иванов",
        address="Москва",
        metro="Сокол",
        phone="89990001122",
        date="02.02.2025",
        duration_text="трое суток",
        color_black=True,
        color_grey=False,
        comment="Позвонить за час"
    ),
    OrderTestData(
        name="Мария",
        surname="Петрова",
        address="Москва",
        metro="Бабушкинская",
        phone="88888888888",
        date="03.03.2025",
        duration_text="двое суток",
        color_black=False,
        color_grey=True,
        comment="Доставить к подъезду"
    )
])
def test_order_positive_flow(order_page, test_data):
    """
    Тест позитивного сценария заказа самоката.
    Параметры входных данных передаются одним объектом (DTO).
    """

    # 3. Заполнить первую часть формы
    order_page.fill_personal_data(
        test_data.name,
        test_data.surname,
        test_data.address,
        test_data.metro,
        test_data.phone
    )
    order_page.click_next_button()

    # 4. Заполнить вторую часть
    order_page.fill_rent_data(
        test_data.date,
        test_data.duration_text,
        test_data.color_black,
        test_data.color_grey,
        test_data.comment
    )
    order_page.click_order_button()

    # 5. Подтвердить заказ
    order_page.confirm_order_modal()

    # 6. Проверить, что заказ оформлен
    success_text = order_page.get_success_message()
    assert "Заказ оформлен" in success_text, (
        f"Не найдено подтверждение заказа. Текст: {success_text}"
    )
