from base.base_action import BaseAction
from selenium.webdriver.common.by import By
import allure
class SavedContactPage(BaseAction):
    name_title = (By.ID, "com.android.contacts:id/large_title")

    def get_name_title(self):
        title = self.find_element(self.name_title).text
        allure.attach("screenshot:",title,attachment_type=allure.attachment_type.PNG)
        return title