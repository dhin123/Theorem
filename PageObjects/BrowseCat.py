from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Browse:
    def __init__(self, driver):
        self.driver = driver

    signin = By.CSS_SELECTOR("a.login")
    loginemail = By.ID("email")
    loginpassword = By.ID("passwd")
    loginsubmit = By.ID("SubmitLogin")
    menu = By.XPATH("//div[@id='block_top_menu']/ul/li/a")
    searchbar = By.ID("search_query_top")

    def login(self):
        return self.driver.find_element(*Browse.signin).click()

    def logemail(self):
        return self.driver.find_element(*Browse.loginemail).send_keys("sindhus1305@gmail.com")

    def logpassword(self):
        return self.driver.find_element(*Browse.loginpassword).send_keys("Sindhu124")

    def logsubmit(self):
        return self.driver.find_element(*Browse.loginsubmit).click()

    def search(self):
        return self.driver.find_element(*Browse.searchbar).send_keys("printed")

    def searchenter(self):
        return self.driver.find_element(*Browse.searchbar).send_keys(Keys.ENTER)



