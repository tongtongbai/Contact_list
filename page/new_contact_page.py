from selenium.webdriver.common.by import By
from base.base_action import BaseAction
import allure
class NewContactPage(BaseAction):
    name_input_box = (By.XPATH,"//*[@text='姓名']")
    phone_input_box = (By.XPATH,"//*[@text='电话']")
    pop_up_message_text = (By.XPATH,"//*[@text='本地保存']")

    def click_pop_up_message_text_button(self):
        self.click_element(self.pop_up_message_text)

    @allure.step(title="Input Name")
    def input_name(self,content):
        allure.attach("input Name:",content,attachment_type=allure.attachment_type.TEXT)
        self.input_element(self.name_input_box,content)

    @allure.step(title="Input Phone number")
    def input_phone(self,content):
        allure.attach("input Phone:", content,attachment_type=allure.attachment_type.TEXT)
        self.input_element(self.phone_input_box,content)
