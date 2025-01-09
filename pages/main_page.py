import allure
from selenium.webdriver.remote.webelement import WebElement
import constants
from pages.base_page import BasePage
from pages.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = constants.BASE_URL

    @allure.step("Получить ответ на вопрос")
    def get_answer(self, question_locator, answer_locator) -> WebElement:
        """Открывает вопрос и возвращает ответ"""
        self.click(question_locator)  # Используем метод click из BasePage
        return self.find_visible_element(answer_locator)  # Используем find_visible_element из BasePage

    @allure.step("Кликнуть на кнопку заказать: верхнюю или нижнюю")
    def click_order_button(self, button_position):
        """
        Кликает на кнопку «Заказать» (верхнюю или нижнюю),
        в зависимости от значения button_position.
        """
        if button_position == "top":
            self.click(MainPageLocators.TOP_ORDER_BUTTON)
        else:
            element = self.find_clickable_element(MainPageLocators.BOTTOM_ORDER_BUTTON)
            self.scroll_to_element(element)
            self.action_chains.click(element).perform()
