from selenium.webdriver.common.by import By
import allure
from base.base_action import BaseAction


class ContactListPage(BaseAction):

    new_contact_button = (By.ID,"com.android.contacts:id/floating_action_button")

    @allure.step(title="Click Add New Contact Button")
    def click_new_contact_button(self):
        self.click_element(self.new_contact_button)

