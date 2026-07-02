from pages.base_page import BasePage
from locators.taxi_page_locators import TaxiPageLocators


class TaxiPage(BasePage):

    def taxi_modal_visible(self):
        return self.is_visible(TaxiPageLocators.TAXI_MODAL)

    def tariffs_count(self):
        return len(self.find_elements(TaxiPageLocators.TARIFFS))

    def active_tariff_count(self):
        return len(self.find_elements(TaxiPageLocators.ACTIVE_TARIFF))

    def select_tariff(self, index):
        self.find_elements(TaxiPageLocators.TARIFFS)[index].click()
        
    def open_tariff_tooltip(self, index):
        self.find_elements(TaxiPageLocators.TARIFFS)[index].click()
        self.wait.until(lambda d: "active" in d.find_elements(*TaxiPageLocators.TARIFFS)[index].get_attribute("class"))
        info_button = self.wait.until(lambda d: d.find_elements(*TaxiPageLocators.TARIFFS)[index].find_element(*TaxiPageLocators.INFO_BUTTONS))

        self.hover(info_button)

    def tooltip_visible(self):
        return self.is_visible(TaxiPageLocators.TOOLTIP)

    def tooltip_title(self):
        tooltip = self.find_element(TaxiPageLocators.TOOLTIP)
        return tooltip.find_element(*TaxiPageLocators.TOOLTIP_TITLE).text

    def tooltip_description(self):
        tooltip = self.find_element(TaxiPageLocators.TOOLTIP)
        return tooltip.find_element(*TaxiPageLocators.TOOLTIP_DESCRIPTION).text

    def phone_button_visible(self):
        return self.is_visible(TaxiPageLocators.PHONE_BUTTON)

    def payment_button_visible(self):
        return self.is_visible(TaxiPageLocators.PAYMENT_BUTTON)

    def comment_input_visible(self):
        return self.is_visible(TaxiPageLocators.COMMENT_INPUT)

    def requirements_block_visible(self):
        return self.is_visible(TaxiPageLocators.REQUIREMENTS_BLOCK)

    def click_laptop_checkbox(self):
        self.click(TaxiPageLocators.LAPTOP_CHECKBOX)

    def laptop_checkbox_selected(self):
        return self.find_element(TaxiPageLocators.LAPTOP_CHECKBOX).is_selected()

    def order_button_visible(self):
        return self.is_visible(TaxiPageLocators.ORDER_BUTTON)

    def order_button_enabled(self):
        return self.find_element(TaxiPageLocators.ORDER_BUTTON).is_enabled()

    def click_order_button(self):
        self.click(TaxiPageLocators.ORDER_BUTTON)

    def expand_requirements(self):
        self.click(TaxiPageLocators.REQUIREMENTS_HEADER)