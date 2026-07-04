import pytest, allure

from data.test_data import (FROM_ADDRESS,TO_ADDRESS,WORK_DESCRIPTION,SLEEPY_DESCRIPTION,VACATION_DESCRIPTION,TALKATIVE_DESCRIPTION,COMFORT_DESCRIPTION,GLOSSY_DESCRIPTION,)

@allure.feature("Заказ тарифа Такси")
class TestTaxiOrder:

    def open_taxi_order(self, main_page, route_page):
        main_page.fill_route(FROM_ADDRESS, TO_ADDRESS)
        route_page.click_fast()
        route_page.click_call_taxi()

    @allure.title("Открывается форма заказа со всеми тарифами и полями")
    def test_taxi_order_form_displayed(self, main_page, route_page, taxi_page):
        self.open_taxi_order(main_page, route_page)

        assert taxi_page.taxi_modal_visible()
        assert taxi_page.tariffs_count() == 6
        assert taxi_page.active_tariff_count() == 1

    @allure.title("Тариф Рабочий - tooltip корректный")
    def test_tariff_work(self, main_page, route_page, taxi_page):
        self.open_taxi_order(main_page, route_page)

        taxi_page.open_tariff_tooltip(0)

        assert taxi_page.tooltip_visible()
        assert taxi_page.tooltip_title() == "Рабочий"
        assert taxi_page.tooltip_description() == WORK_DESCRIPTION

    @allure.title("Тариф Сонный - tooltip (ожидаемый баг)")
    @pytest.mark.xfail(reason="BUG: неверный текст tooltip для тарифа Сонный")
    def test_tariff_sleepy(self, main_page, route_page, taxi_page):
        self.open_taxi_order(main_page, route_page)

        taxi_page.open_tariff_tooltip(1)

        assert taxi_page.tooltip_title() == "Сонный"
        assert taxi_page.tooltip_description() == SLEEPY_DESCRIPTION

    @allure.title("Тариф Отпускной - tooltip корректный")
    def test_tariff_vacation(self, main_page, route_page, taxi_page):
        self.open_taxi_order(main_page, route_page)

        taxi_page.open_tariff_tooltip(2)

        assert taxi_page.tooltip_title() == "Отпускной"
        assert taxi_page.tooltip_description() == VACATION_DESCRIPTION

    @allure.title("Тариф Разговорчивый - tooltip (ожидаемый баг)")
    @pytest.mark.xfail(reason="BUG: неверный текст tooltip для тарифа Разговорчивый")
    def test_tariff_talkative(self, main_page, route_page, taxi_page):
        self.open_taxi_order(main_page, route_page)

        taxi_page.open_tariff_tooltip(3)

        assert taxi_page.tooltip_title() == "Разговорчивый"
        assert taxi_page.tooltip_description() == TALKATIVE_DESCRIPTION

    @allure.title("Тариф Утешительный - tooltip корректный")
    def test_tariff_comfort(self, main_page, route_page, taxi_page):
        self.open_taxi_order(main_page, route_page)

        taxi_page.open_tariff_tooltip(4)

        assert taxi_page.tooltip_title() == "Утешительный"
        assert taxi_page.tooltip_description() == COMFORT_DESCRIPTION

    @allure.title("Тариф Глянцевый - tooltip корректный")
    def test_tariff_glossy(self, main_page, route_page, taxi_page):
        self.open_taxi_order(main_page, route_page)

        taxi_page.open_tariff_tooltip(5)

        assert taxi_page.tooltip_title() == "Глянцевый"
        assert taxi_page.tooltip_description() == GLOSSY_DESCRIPTION

    @allure.title("Под тарифами отображается блок подготовки заказа")
    def test_order_preparation_block_displayed(self, main_page, route_page, taxi_page):
        self.open_taxi_order(main_page, route_page)

        assert taxi_page.phone_button_visible()
        assert taxi_page.payment_button_visible()
        assert taxi_page.comment_input_visible()
        assert taxi_page.requirements_block_visible()