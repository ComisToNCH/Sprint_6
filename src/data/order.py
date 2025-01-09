from dataclasses import dataclass

@dataclass
class OrderData:
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

ORDER_DATA_LIST = [
    OrderData(
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
    OrderData(
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
    ]