class BaseAction:

    def __init__(self,driver):
        self.driver = driver

    def find_element(self,location):
        location_by,location_value = location
        return self.driver.find_element(location_by,location_value)

    def click_element(self,location):
        self.find_element(location).click()

    def input_element(self,location,content):
        self.find_element(location).send_keys(content)

    def clear_element(self,location):
        self.find_element(location).clear()
    #back action
    def click_back_button(self):
        self.driver.press_keycode(4)
