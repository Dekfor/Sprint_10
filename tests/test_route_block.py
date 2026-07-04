import allure
from pages.main_page import MainPage
from pages.route_page import RoutePage
from data.test_data import FROM_ADDRESS
from data.test_data import TO_ADDRESS


@allure.feature("Блок выбора маршрута")
class TestRouteBlock:

    @allure.title("После ввода разных адресов отображается блок выбора маршрута")
    def test_route_block_is_displayed(self, driver):

        main = MainPage(driver)

        with allure.step("Вводим разные адреса маршрута"):
            main.fill_route(FROM_ADDRESS, TO_ADDRESS)

        with allure.step("Проверяем отображение блока выбора маршрута"):
            assert main.route_block_is_visible()

    @allure.title("При одинаковых адресах отображается бесплатный маршрут")
    def test_same_addresses_show_zero_route(self, driver):

        main = MainPage(driver)
        route = RoutePage(driver)

        with allure.step("Вводим одинаковые адреса"):
            main.fill_route(FROM_ADDRESS, FROM_ADDRESS)

        with allure.step("Проверяем, что маршрут бесплатный и нулевой по времени"):
            assert route.get_price() == "Авто Бесплатно"
            assert route.get_duration() == "В пути 0 мин."
        