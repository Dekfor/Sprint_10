from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators
from selenium.common.exceptions import TimeoutException



class OrderPage(BasePage):

    def search_window_visible(self):
        try:
            return self.is_visible(OrderPageLocators.SEARCH_WINDOW)
        except TimeoutException:
            return False

    def search_title(self):
        return self.get_text(OrderPageLocators.SEARCH_TITLE)

    def search_timer_visible(self):
        return self.is_visible(OrderPageLocators.SEARCH_TIMER)

    def click_details(self):
        self.click(OrderPageLocators.DETAILS_BUTTON)

    def click_cancel(self):
        self.click(OrderPageLocators.CANCEL_BUTTON)

    def details_visible(self):
        return self.is_visible(OrderPageLocators.DETAILS_WINDOW)

    def pickup_address(self):
        return self.get_text(OrderPageLocators.PICKUP_ADDRESS)

    def destination_address(self):
        return self.get_text(OrderPageLocators.DESTINATION_ADDRESS)

    def payment_info(self):
        return self.get_text(OrderPageLocators.PAYMENT_INFO)

    def trip_info_title(self):
        return self.get_text(OrderPageLocators.TRIP_INFO_TITLE)

    def order_price(self):
        return self.get_text(OrderPageLocators.ORDER_PRICE)

    def order_complete_title(self):
        return self.get_text(OrderPageLocators.ORDER_COMPLETE_TITLE)

    def car_number_visible(self):
        return self.is_visible(OrderPageLocators.CAR_NUMBER)

    def tariff_image_visible(self):
        return self.is_visible(OrderPageLocators.TARIFF_IMAGE)

    def driver_name_visible(self):
        return self.is_visible(OrderPageLocators.DRIVER_NAME)

    def driver_photo_visible(self):
        return self.is_visible(OrderPageLocators.DRIVER_PHOTO)

    def driver_rating_visible(self):
        return self.is_visible(OrderPageLocators.DRIVER_RATING)
    
    def wait_order_complete(self):
        self.find_element(OrderPageLocators.CAR_NUMBER)

    def wait_search_window_disappear(self):
        self.wait_until_invisible(OrderPageLocators.SEARCH_WINDOW)