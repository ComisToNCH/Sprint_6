import allure
from selenium.webdriver import ActionChains
from constants import BASE_URL
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)
        self.url = BASE_URL
        self.action_chains = ActionChains(self.driver)

    def open_page(self):
        self.driver.get(self.url)

    def wait_url_contains(self, url):
        self.wait.until(EC.url_contains(url))

    @allure.step("Открыть страницу: {url}")
    def go_to_site(self, url=None):
        if not url:  # Проверка, если url не передан или равен None
            url = self.url  # Используем self.url, определенный в BasePage
        self.driver.get(url)

    @allure.step("Ищем элемент по локатору: {locator}")
    def find_clickable_element(self, locator):
        """Находит элемент, доступный для клика"""
        element = self.wait.until(EC.element_to_be_clickable(locator))
        return element

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    @allure.step("Кликаем на элемент по локатору: {locator}")
    def click(self, locator):
        """Кликает по элементу, предварительно ожидая его доступности"""
        element = self.find_clickable_element(locator)
        element.click()

    @allure.step("Ищем видимый элемент по локатору: {locator}")
    def find_visible_element(self, locator):
        """Находит видимый элемент"""
        return self.wait.until(EC.visibility_of_element_located(locator))

    @allure.step("Вводим текст '{text}' в элемент по локатору: {locator}")
    def enter_text(self, locator, text):
        """Очищает поле и вводит текст"""
        element = self.find_visible_element(locator)
        element.clear()
        element.send_keys(text)

    @allure.step("Получаем текст из элемента по локатору: {locator}")
    def get_text(self, locator):
        """Получает текст из элемента"""
        element = self.find_visible_element(locator)
        return element.text

    @allure.step("Проверяем наличие элемента по локатору: {locator}")
    def is_element_present(self, locator):
        """Проверяет, присутствует ли элемент на странице"""
        try:
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False

    def switch_to_second_tab(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @property
    def current_url(self):
        current_url = self.driver.current_url
        return current_url

    @allure.step("Клик по логотипу 'Самокат'")
    def click_scooter_logo(self):
        """Кликает на логотип 'Самокат'"""
        self.click(BasePageLocators.SCOOTER_LOGO)  # Используем click из BasePage

    @allure.step("Клик по логотипу 'Яндекс'")
    def click_yandex_logo(self):
        """Кликает на логотип 'Яндекс'"""
        self.click(BasePageLocators.YANDEX_LOGO)  # Используем click из BasePage