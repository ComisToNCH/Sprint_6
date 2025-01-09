from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Шаг 1 (персональные данные)
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    METRO_OPTIONS = (By.CLASS_NAME, "select-search__row")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")

    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    # Шаг 2 (данные аренды)
    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENT_DURATION_DROPDOWN = (By.CLASS_NAME, "Dropdown-control")
    RENT_DURATION_OPTION = (By.CLASS_NAME, "Dropdown-menu")
    OPTION_LOCATOR = (By.XPATH, "//div[contains(@class, 'Dropdown-option'")

    COLOR_BLACK_CHECKBOX = (By.CSS_SELECTOR, "label[for='black']")
    COLOR_GREY_CHECKBOX = (By.CSS_SELECTOR, "label[for='grey']")

    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    CONFIRM_MODAL_YES_BUTTON = (By.XPATH, "//button[text()='Да']")

    # Сообщение об успехе — «Заказ оформлен»
    SUCCESS_MODAL_TEXT = (By.CLASS_NAME, "Order_ModalHeader__3FDaJ")
