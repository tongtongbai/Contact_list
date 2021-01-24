from base.base_driver import init_driver
from page.page import Page
import pytest
from base.base_analyze_data import analyze_data
import time
import allure
class TestSendMessage:
    def setup(self):
        self.driver = init_driver()
        self.page = Page(self.driver)

    def teardown(self):
        self.driver.quit()

    @allure.severity(allure.severity_level.CRITICAL)
    @pytest.mark.parametrize("args", analyze_data("contact_data.yml", "test_add_contact"))
    def test_send_message(self, args):
        self.page.contact_list_page.click_new_contact_button()
        self.page.new_contact_page.click_pop_up_message_text_button()
        self.page.new_contact_page.input_name(args["name"])
        self.page.new_contact_page.input_phone(args["phone"])
        self.page.new_contact_page.click_back_button()
        time.sleep(1)
        assert args["name"] == self.page.saved_contact_title.get_name_title()

    @allure.severity("minor")
    def test_login1(self):
        assert 1==1

    @allure.severity("critical")
    def test_login2(self):
        assert 1==0