import allure
import pytest
from pages.locators.main_page_locators import MainPageLocators
from conftest import main_page

@pytest.mark.parametrize("locator, answer, expected_text", [
    (MainPageLocators.QUESTION_1, MainPageLocators.ANSWER_1, "Сутки — 400 рублей. Оплата курьеру — наличными или картой."),
    (MainPageLocators.QUESTION_2, MainPageLocators.ANSWER_2, "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим."),
    (MainPageLocators.QUESTION_3, MainPageLocators.ANSWER_3, "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30."),
    (MainPageLocators.QUESTION_4, MainPageLocators.ANSWER_4, "Только начиная с завтрашнего дня. Но скоро станем расторопнее."),
    (MainPageLocators.QUESTION_5, MainPageLocators.ANSWER_5, "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010."),
    (MainPageLocators.QUESTION_6, MainPageLocators.ANSWER_6, "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится."),
    (MainPageLocators.QUESTION_7, MainPageLocators.ANSWER_7, "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои."),
    (MainPageLocators.QUESTION_8, MainPageLocators.ANSWER_8, "Да, обязательно. Всем самокатов! И Москве, и Московской области.")
])

@allure.title("Тест на проверку текста ответов в FAQ")
@allure.description("Проверяет, что каждый вопрос в FAQ открывает правильный текст ответа.")
def test_questions(main_page, locator, answer, expected_text):
    """
    Проверяет, что текст ответа для каждого вопроса в FAQ совпадает с ожидаемым.
    """

    with allure.step(f"Клик по вопросу с локатором {locator}"):
        element = main_page.find_clickable_element(locator)
        main_page.scroll_to_element(element)
        main_page.action_chains.click(element).perform()

    with allure.step(f"Получение текста ответа по локатору {answer}"):
        answer_text = main_page.get_answer(locator, answer).text

    with allure.step(f"Проверка совпадения текста ответа: {expected_text}"):
        assert answer_text == expected_text, f"Ожидалось: {expected_text}, Получено: {answer_text}"
