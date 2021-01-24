from page.contact_list_page import ContactListPage
from page.saved_contacts_page import SavedContactPage
from page.new_contact_page import NewContactPage

class Page:

    def __init__(self,driver):
        self.driver = driver

    @property
    def contact_list_page(self):
        return ContactListPage(self.driver)
    @property
    def new_contact_page(self):
        return NewContactPage(self.driver)

    @property
    def saved_contact_title(self):
        return SavedContactPage(self.driver)