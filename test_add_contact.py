# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import unittest
from contact import Contact

class TestAddGroup(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome("/Users/marinabelousova/chromedriver/chromedriver")
        self.driver.implicitly_wait(30)

    def open_page(self, driver):
        driver.get("http://localhost:8080/addressbook/index.php")

    def login(self, driver, username, password):
        driver.find_element_by_name("user").clear()
        driver.find_element_by_name("user").send_keys(username)
        driver.find_element_by_name("pass").click()
        driver.find_element_by_name("pass").clear()
        driver.find_element_by_name("pass").send_keys(password)
        driver.find_element_by_xpath("//*[@id='LoginForm']/input[3]").click()

    def add_new_contact(self, driver, contact):
        driver.find_element_by_xpath("//*[@id='nav']/ul/li[2]/a").click()
        driver.find_element_by_name("firstname").click()
        driver.find_element_by_name("firstname").clear()
        driver.find_element_by_name("firstname").send_keys(contact.firstname)
        driver.find_element_by_name("middlename").click()
        driver.find_element_by_name("middlename").clear()
        driver.find_element_by_name("middlename").send_keys(contact.middlename)
        driver.find_element_by_name("lastname").click()
        driver.find_element_by_name("lastname").clear()
        driver.find_element_by_name("lastname").send_keys(contact.lastname)
        driver.find_element_by_name("nickname").click()
        driver.find_element_by_name("nickname").clear()
        driver.find_element_by_name("nickname").send_keys(contact.nick)
        driver.find_element_by_name("email").click()
        driver.find_element_by_name("email").clear()
        driver.find_element_by_name("email").send_keys(contact.mail)
        driver.find_element_by_name("bday").click()
        Select(driver.find_element_by_name("bday")).select_by_visible_text(contact.bday_day)
        driver.find_element_by_name("bmonth").click()
        Select(driver.find_element_by_name("bmonth")).select_by_visible_text(contact.bday_month)
        driver.find_element_by_name("byear").click()
        driver.find_element_by_name("byear").clear()
        driver.find_element_by_name("byear").send_keys(contact.bday_year)
        driver.find_element_by_name("theform").click()
        driver.find_element_by_xpath("(//input[@name='submit'])[2]").click()

    def logout(self, driver):
        driver.find_element_by_link_text("Logout").click()

    def test_add_group(self):
        driver = self.driver
        self.open_page(driver)
        self.login(driver, username="admin", password="secret")
        self.add_new_contact(driver, Contact("Test", "Testovich", "Test", "Test_Testovich", "test@test.ru", "10", "November",
                             "1997"))
        self.logout(driver)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
