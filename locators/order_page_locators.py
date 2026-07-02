from selenium.webdriver.common.by import By


class OrderPageLocators:

    SEARCH_WINDOW = (By.CLASS_NAME, "order-body")
    SEARCH_TITLE = (By.XPATH,"//div[@class='order-header-title' and text()='Поиск машины']")
    SEARCH_TIMER = (By.CLASS_NAME, "order-header-time")
    DETAILS_BUTTON = (By.XPATH,"//div[normalize-space()='Детали']/preceding-sibling::button")
    CANCEL_BUTTON = (By.XPATH, "//img[@alt='close']")
    DETAILS_WINDOW = (By.CSS_SELECTOR,".order-details.shown")
    PICKUP_ADDRESS = (By.XPATH, "//div[text()='Адрес подачи']/preceding-sibling::div")
    DESTINATION_ADDRESS = (By.XPATH, "//div[text()='Адрес назначения']/preceding-sibling::div")
    PAYMENT_INFO = (By.XPATH, "//div[text()='Способ оплаты']/preceding-sibling::div")
    TRIP_INFO_TITLE = (By.XPATH, "//div[contains(@class,'o-d-h') and text()='Еще про поездку']")
    ORDER_PRICE = (By.XPATH, "//div[contains(@class,'o-d-sh') and contains(text(),'Стоимость')]")
    ORDER_COMPLETE_TITLE = (By.XPATH, "//div[contains(@class,'order-header-title') and contains(text(),'приедет')]")
    CAR_NUMBER = (By.CLASS_NAME, "number")

    TARIFF_IMAGE = (By.CSS_SELECTOR, ".order-number img")

    DRIVER_NAME = (By.XPATH,"(//div[@class='order-btn-group'])[1]/div[2]")

    DRIVER_PHOTO = (By.XPATH,"//div[@class='order-btn-group'][1]//img")
    DRIVER_RATING = (By.CLASS_NAME, "order-btn-rating")
