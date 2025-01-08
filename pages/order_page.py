import allure
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import constants
from pages.base_page import BasePage
from pages.locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support import expected_conditions as EC


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)
        self.url = constants.ORDER_URL

    @allure.step("Заполнить личные данные: {name}, {surname}, {address}, {metro}, {phone}")
    def fill_personal_data(self, name, surname, address, metro, phone):
        """Заполняет личные данные"""
        self.enter_text(OrderPageLocators.NAME_INPUT, name)  # Используем метод enter_text из BasePage
        self.enter_text(OrderPageLocators.SURNAME_INPUT, surname)
        self.enter_text(OrderPageLocators.ADDRESS_INPUT, address)
        self.select_metro_station(metro)  # Используем кастомный метод для выбора метро
        self.enter_text(OrderPageLocators.PHONE_INPUT, phone)

    @allure.step("Выбрать станцию метро: {metro}")
    def select_metro_station(self, metro):
        """Вводит название станции метро и кликает на нужный вариант"""
        self.enter_text(OrderPageLocators.METRO_INPUT, metro)  # Используем enter_text
        metro_options = self.wait.until(
            EC.presence_of_all_elements_located(OrderPageLocators.METRO_OPTIONS)
        )
        for option in metro_options:
            if metro in option.text:
                option.click()
                return

    @allure.step("Нажать на кнопку 'Далее'")
    def click_next_button(self):
        """Кликает на кнопку 'Далее'"""
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step("Заполнить данные аренды: {date}, {duration_text}, цвет черный: {color_black}, цвет серый: {color_grey}, комментарий: {comment}")
    def fill_rent_data(self, date, duration_text, color_black=False, color_grey=False, comment=""):
        """Заполняет данные аренды"""
        self.enter_text(OrderPageLocators.DATE_INPUT, date)  # Используем enter_text
        self.find_visible_element(OrderPageLocators.DATE_INPUT).send_keys(Keys.ENTER)  # Нажимаем Enter
        self.select_rent_duration(duration_text)
        self.select_scooter_color(color_black=color_black, color_grey=color_grey)
        self.enter_text(OrderPageLocators.COMMENT_INPUT, comment)

    @allure.step("Выбрать срок аренды: {duration}")
    def select_rent_duration(self, duration):
        """Выбирает срок аренды из выпадающего списка"""
        self.click(OrderPageLocators.RENT_DURATION_DROPDOWN)  # Используем click
        option_locator = (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{duration}']")
        self.click(option_locator)  # Используем click

    @allure.step("Выбрать цвет самоката: черный={color_black}, серый={color_grey}")
    def select_scooter_color(self, color_black=False, color_grey=False):
        """Выбирает цвет самоката"""
        if color_black:
            self.click(OrderPageLocators.COLOR_BLACK_CHECKBOX)  # Используем click
        if color_grey:
            self.click(OrderPageLocators.COLOR_GREY_CHECKBOX)  # Используем click

    @allure.step("Нажать на кнопку 'Заказать'")
    def click_order_button(self):
        """Кликает на кнопку 'Заказать'"""
        self.click(OrderPageLocators.ORDER_BUTTON)  # Используем click

    @allure.step("Подтвердить заказ в модальном окне")
    def confirm_order_modal(self):
        """Подтверждает заказ в модальном окне"""
        self.click(OrderPageLocators.CONFIRM_MODAL_YES_BUTTON)  # Используем click

    @allure.step("Получить сообщение об успешном заказе")
    def get_success_message(self):
        """Возвращает текст сообщения об успешном заказе"""
        return self.get_text(OrderPageLocators.SUCCESS_MODAL_TEXT)  # Используем get_text
