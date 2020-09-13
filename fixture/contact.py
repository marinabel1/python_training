from selenium.webdriver.support.ui import Select
from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//*[@id='nav']/ul/li[2]/a").click()
        self.filling_fields_contact("firstname", contact.firstname)
        self.filling_fields_contact("middlename", contact.middlename)
        self.filling_fields_contact("lastname", contact.lastname)
        self.filling_fields_contact("nickname", contact.nick)
        self.filling_fields_contact("email", contact.mail)
        self.filling_fields_contact("email", contact.mail)
        wd.find_element_by_name("bday").click()
        Select(wd.find_element_by_name("bday")).select_by_visible_text(contact.bday_day)
        wd.find_element_by_name("bmonth").click()
        Select(wd.find_element_by_name("bmonth")).select_by_visible_text(contact.bday_month)
        self.filling_fields_contact("byear", contact.bday_year)
        wd.find_element_by_name("theform").click()
        wd.find_element_by_xpath("(//input[@name='submit'])[2]").click()
        self.contact_cache = None

    def filling_fields_contact(self, name, keys):
        wd = self.app.wd
        wd.find_element_by_name(name).click()
        wd.find_element_by_name(name).clear()
        wd.find_element_by_name(name).send_keys(keys)

    def delete_first_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_name('selected[]').click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def delete_all_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id('MassCB').click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        wd.switch_to_alert().accept()
        self.contact_cache = None

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//img[@title="Edit"]').click()
        self.filling_fields_contact("company", contact.company)
        self.filling_fields_contact("mobile", contact.mobile)
        self.filling_fields_contact("work", contact.work)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()
        self.contact_cache = None

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name('entry'):
                lastname = element.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[2]').text
                firstname = element.find_element_by_xpath('//*[@id="maintable"]/tbody/tr[2]/td[3]').text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                self.contact_cache.append(Contact(firstname=firstname, id=id, lastname=lastname))
        return self.contact_cache



