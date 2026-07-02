from selenium.webdriver.common.by import By


class RoutePageLocators:

    OPTIMAL_TAB = (By.XPATH, "//div[contains(@class,'mode') and normalize-space()='Оптимальный']")
    FAST_TAB = (By.XPATH, "//div[contains(@class,'mode') and normalize-space()='Быстрый']")
    CUSTOM_TAB = (By.XPATH, "//div[contains(@class,'mode') and normalize-space()='Свой']")
    ACTIVE_TAB = (By.CSS_SELECTOR, ".mode.active")
    PRICE = (By.CSS_SELECTOR, ".results-text .text")
    DURATION = (By.CSS_SELECTOR, ".results-text .duration")
    CAR_TYPE = (By.CSS_SELECTOR, ".type:nth-child(1)")
    WALK_TYPE = (By.CSS_SELECTOR, ".type:nth-child(2)")
    TAXI_TYPE = (By.CSS_SELECTOR, ".type:nth-child(3)")
    BIKE_TYPE = (By.CSS_SELECTOR, ".type:nth-child(4)")
    SCOOTER_TYPE = (By.CSS_SELECTOR, ".type:nth-child(5)")
    DRIVE_TYPE = (By.CSS_SELECTOR, ".type:nth-child(6)")
    ACTIVE_TRANSPORT = (By.CSS_SELECTOR, ".type.active")
    CALL_TAXI_BUTTON = (By.XPATH, "//button[normalize-space()='Вызвать такси']")
    BOOK_BUTTON = (By.XPATH, "//button[normalize-space()='Забронировать']")
    