import allure
from data.test_data import FROM_ADDRESS, TO_ADDRESS


@allure.feature("Полный сценарий заказа Такси")
class TestOrder:

    def prepare_order(self, main_page, route_page, taxi_page):
        main_page.fill_route(FROM_ADDRESS, TO_ADDRESS)
        route_page.click_fast()

        price = route_page.get_price().split("~")[1].replace("руб.", "").strip()

        route_page.click_call_taxi()
        taxi_page.select_tariff(0)
        taxi_page.expand_requirements()
        taxi_page.click_laptop_checkbox()
        taxi_page.click_order_button()

        return price

    @allure.title("После оформления заказа отображается окно поиска машины")
    def test_search_window_visible(self, main_page, route_page, taxi_page, order_page):
        self.prepare_order(main_page, route_page, taxi_page)

        assert order_page.search_window_visible()

    @allure.title("В окне поиска машины отображается корректный заголовок")
    def test_search_window_title(self, main_page, route_page, taxi_page, order_page):
        self.prepare_order(main_page, route_page, taxi_page)

        assert order_page.search_title() == "Поиск машины"

    @allure.title("В окне поиска машины отображается таймер")
    def test_search_timer_visible(self, main_page, route_page, taxi_page, order_page):
        self.prepare_order(main_page, route_page, taxi_page)

        assert order_page.search_timer_visible()

    @allure.title("В деталях заказа отображается корректная информация")
    def test_details(self, main_page, route_page, taxi_page, order_page):
        price = self.prepare_order(main_page, route_page, taxi_page)

        order_page.click_details()

        assert order_page.details_visible()
        assert order_page.pickup_address() == FROM_ADDRESS
        assert order_page.destination_address() == TO_ADDRESS
        assert order_page.trip_info_title() == "Еще про поездку"
        assert price in order_page.order_price()

    @allure.title("После окончания поиска отображается окно выполненного заказа")
    def test_completed_order(self, main_page, route_page, taxi_page, order_page):
        self.prepare_order(main_page, route_page, taxi_page)

        order_page.wait_order_complete()

        assert order_page.car_number_visible()
        assert order_page.tariff_image_visible()
        assert order_page.driver_name_visible()
        assert order_page.driver_photo_visible()
        assert order_page.driver_rating_visible()

    @allure.title("Заказ можно отменить")
    def test_cancel(self, main_page, route_page, taxi_page, order_page):
        self.prepare_order(main_page, route_page, taxi_page)

        order_page.click_cancel()
        order_page.wait_search_window_disappear()

        assert not order_page.search_window_visible()
