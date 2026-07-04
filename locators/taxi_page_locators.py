from selenium.webdriver.common.by import By


class TaxiPageLocators:

    TAXI_MODAL = (By.CLASS_NAME, "tariff-picker")
    TARIFFS = (By.CLASS_NAME, "tcard")
    ACTIVE_TARIFF = (By.CSS_SELECTOR, ".tcard.active")
    TARIFF_TITLES = (By.CSS_SELECTOR, ".tcard-title")
    INFO_BUTTONS = (By.CSS_SELECTOR, "button.tcard-i")
    TOOLTIP = (By.CSS_SELECTOR,"div.__react_component_tooltip.show")
    TOOLTIP_TITLE = (By.CSS_SELECTOR, ".i-title")
    TOOLTIP_DESCRIPTION = (By.CSS_SELECTOR, "div.__react_component_tooltip .i-dPrefix")
    PHONE_BUTTON = (By.CLASS_NAME, "np-button")
    PAYMENT_BUTTON = (By.CLASS_NAME, "pp-button")
    COMMENT_INPUT = (By.ID, "comment")
    REQUIREMENTS_BLOCK = (By.CLASS_NAME, "reqs")
    REQUIREMENTS_HEADER = (By.XPATH,"//div[contains(@class,'reqs-header')]")
    LAPTOP_CHECKBOX = (By.XPATH,"//span[contains(@class,'slider')]")
    ORDER_BUTTON = (By.CLASS_NAME, "smart-button")
    