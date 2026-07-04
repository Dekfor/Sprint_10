from pages.base_page import BasePage
from locators.route_page_locators import RoutePageLocators


class RoutePage(BasePage):

    def click_optimal(self):
        self.click(RoutePageLocators.OPTIMAL_TAB)

    def click_fast(self):
        self.click(RoutePageLocators.FAST_TAB)

    def click_custom(self):
        self.click(RoutePageLocators.CUSTOM_TAB)

    def click_drive(self):
        self.click(RoutePageLocators.DRIVE_TYPE)

    def click_taxi(self):
        self.click(RoutePageLocators.TAXI_TYPE)

    def click_call_taxi(self):
        self.click(RoutePageLocators.CALL_TAXI_BUTTON)

    def click_book(self):
        self.click(RoutePageLocators.BOOK_BUTTON)

    def get_active_tab(self):
        return self.get_text(RoutePageLocators.ACTIVE_TAB)

    def get_price(self):
        return self.get_text(RoutePageLocators.PRICE)

    def get_duration(self):
        return self.get_text(RoutePageLocators.DURATION)

    def call_taxi_button_visible(self):
        return self.is_visible(RoutePageLocators.CALL_TAXI_BUTTON)

    def book_button_visible(self):
        return self.is_visible(RoutePageLocators.BOOK_BUTTON)

    def active_transport(self):
        return self.find_element(RoutePageLocators.ACTIVE_TRANSPORT)

    def all_transport_visible(self):
        return (
            self.is_visible(RoutePageLocators.CAR_TYPE)
            and self.is_visible(RoutePageLocators.WALK_TYPE)
            and self.is_visible(RoutePageLocators.TAXI_TYPE)
            and self.is_visible(RoutePageLocators.BIKE_TYPE)
            and self.is_visible(RoutePageLocators.SCOOTER_TYPE)
            and self.is_visible(RoutePageLocators.DRIVE_TYPE)
        )

    def active_transport_text(self):
        return self.get_text(RoutePageLocators.ACTIVE_TRANSPORT)