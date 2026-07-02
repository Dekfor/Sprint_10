import allure

from pages.main_page import MainPage
from pages.route_page import RoutePage

from data.test_data import FROM_ADDRESS
from data.test_data import TO_ADDRESS


@allure.feature("Подготовка к заказу такси")
class TestRoutePrepare:

    @allure.title("Переключение между Оптимальным и Быстрым маршрутом")
    def test_switch_route_modes(self, driver):

        main = MainPage(driver)
        route = RoutePage(driver)

        main.fill_route(FROM_ADDRESS, TO_ADDRESS)

        route.click_fast()

        fast_price = route.get_price()
        fast_duration = route.get_duration()

        assert route.get_active_tab() == "Быстрый"

        route.click_optimal()

        optimal_price = route.get_price()
        optimal_duration = route.get_duration()

        assert route.get_active_tab() == "Оптимальный"
        assert fast_price != optimal_price or fast_duration != optimal_duration

    @allure.title("При выборе режима Свой отображаются виды транспорта")
    def test_custom_route_contains_transport(self, driver):

        main = MainPage(driver)
        route = RoutePage(driver)

        main.fill_route(FROM_ADDRESS, TO_ADDRESS)

        route.click_custom()

        assert route.get_active_tab() == "Свой"
        assert route.all_transport_visible()

    @allure.title("В режиме Быстрый доступна кнопка Вызвать такси")
    def test_fast_route_has_call_button(self, driver):

        main = MainPage(driver)
        route = RoutePage(driver)

        main.fill_route(FROM_ADDRESS, TO_ADDRESS)

        route.click_fast()

        assert route.call_taxi_button_visible()

    @allure.title("В режиме Драйв доступна кнопка Забронировать")
    def test_drive_route_has_book_button(self, driver):

        main = MainPage(driver)
        route = RoutePage(driver)

        main.fill_route(FROM_ADDRESS, TO_ADDRESS)

        route.click_custom()
        route.click_drive()

        assert route.book_button_visible()