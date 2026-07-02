from selenium.webdriver.common.by import By


class MainPageLocators:

    FROM_INPUT = (By.ID, "from")
    TO_INPUT = (By.ID, "to")
    ROUTE_BLOCK = (By.CSS_SELECTOR, ".type-picker.shown")
    ROUTE_POINTS = (By.CSS_SELECTOR, ".route-pin")
    MAP = (By.ID, "map")
    