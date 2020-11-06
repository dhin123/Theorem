from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class Search:
    def __init__(self, driver):
        self.driver = driver

    searchbar = By.ID("search_query_top")
    searchbar.send_keys("printed")
    searchbar.send_keys(Keys.ENTER)
    print(By.XPATH("//*[@id='center_column']/h1/span[@class='heading-counter']").text)