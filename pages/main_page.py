from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    def enter_from_address(self, address):
        self.send_keys(MainPageLocators.FROM_INPUT, address)

    def enter_to_address(self, address):
        self.send_keys(MainPageLocators.TO_INPUT, address)

    def fill_route(self, from_address, to_address):
        self.enter_from_address(from_address)
        self.enter_to_address(to_address)

    def route_block_is_visible(self):
        return self.is_visible(MainPageLocators.ROUTE_BLOCK)

    def get_route_block_text(self):
        return self.get_text(MainPageLocators.ROUTE_BLOCK)

    def map_is_visible(self):
        return self.is_visible(MainPageLocators.MAP)