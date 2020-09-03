from selenium.webdriver.support.ui import Select


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def add_new_contact(self, contact):
        wd = self.app.wd
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

    def delete_all_contact(self):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_id('MassCB').click()
        wd.find_element_by_xpath('//input[@value="Delete"]').click()
        wd.switch_to_alert().accept()

    def modify_first_contact(self, contact):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath('//img[@title="Edit"]').click()
        self.filling_fields_contact("company", contact.company)
        self.filling_fields_contact("mobile", contact.mobile)
        self.filling_fields_contact("work", contact.work)
        wd.find_element_by_xpath("(//input[@name='update'])[2]").click()




