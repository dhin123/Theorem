import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from PageObjects.AccountSignin import Account
from PageObjects.BrowseCat import Browse
from Utils.Baseclass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):
        log = self.getLogger()
        Account = (self.driver)
        Login = Browse.login()


        menu_list = []
        for m in Browse.menu:
            menu_list.append(m.text)
        print(menu_list)
        for m in Browse.menu:
            m.click()
        assert self.driver.title == "Women - My Store"
        self.driver.find_element_by_css_selector("a[class*='btn-primary']").click()


        self.verifyLinkPresence("Women")
        self.verifyLinkPresence("Dresses")
        self.verifyLinkPresence("T-Shirts")

        number = (By.XPATH("//*[@id='center_column']/h1/span[@class='heading-counter']").text)
        assert "0" not in number
