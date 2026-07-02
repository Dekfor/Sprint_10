import allure

from pages.main_page import MainPage

from data.test_data import FROM_ADDRESS
from data.test_data import TO_ADDRESS


@allure.feature("Отрисовка маршрута")
class TestRouteDrawing:

    @allure.title("После ввода двух адресов отображается карта и маршрут")
    def test_map_is_displayed(self, driver):

        main = MainPage(driver)

        main.fill_route(FROM_ADDRESS, TO_ADDRESS)

        assert main.map_is_visible()
        assert main.route_block_is_visible()