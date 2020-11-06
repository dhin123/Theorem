from selenium.webdriver.common.by import By


class Account:
    def __init__(self, driver):
        self.driver = driver

    signin = By.CSS_SELECTOR("a.login")
    account_email = By.ID("email_create")
    create_account = By.ID("SubmitCreate")
    first_name = By.ID("customer_firstname")
    last_name = By.ID("customer_lastname")
    password = By.ID("passwd")
    address = By.ID("address1")
    city = By.ID("city")
    zipcode = By.ID("postcode")
    states = By.XPATH("//*[@id='id_state']/option[5]")
    phone_number = By.ID("phone_mobile")
    address_alias = By.ID("alias")
    register = By.ID("submitAccount")

    def signing(self):
        return self.driver.find_element(*Account.signin).click()

    def sendemail(self):
        return self.driver.find_element(*Account.account_email).send_keys("sindhus1305@gmail.com")

    def createaccount(self):
        return self.driver.find_element(*Account.create_account).click()

    def firstnamesend(self):
        return self.driver.find_element(*Account.first_name).send_keys("Sindhu")

    def lastnamesend(self):
        return self.driver.find_element(*Account.last_name).send_keys("Sh")

    def passwordsend(self):
        return self.driver.find_element(*Account.password).send_keys("Sindhu124")

    def addresssend(self):
        return self.driver.find_element(*Account.address).send_keys("2421 carlmont")

    def citysend(self):
        return self.driver.find_element(*Account.city).send_keys("Belmont")

    def statesend(self):
        return self.driver.find_element(*Account.states).click()

    def zipcodesend(self):
        return self.driver.find_element(*Account.zipcode).send_keys("94002")

    def phonesend(self):
        return self.driver.find_element(*Account.phone_number).send_keys("6504036567")

    def addressaliassend(self):
        return self.driver.find_element(*Account.address_alias).send_keys("Bangalore India")

    def registered(self):
        return self.driver.find_element(*Account.register).click()















