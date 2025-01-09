from selenium.webdriver.common.by import By

class BasePageLocators:
    # Локаторы для логотипов яндекса и самоката
    SCOOTER_LOGO = (By.CSS_SELECTOR, "a.Header_LogoScooter__3lsAR img")
    YANDEX_LOGO = (By.XPATH, "//img[@alt='Yandex']")