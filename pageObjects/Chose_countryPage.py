from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select



class Chose_country:

    select_countryr = (By.CSS_SELECTOR, "div[class='wrapperTwo'] div select")
    terms_agreer = (By.XPATH, "//input[@class='chkAgree']")
    finalize = (By.CSS_SELECTOR, "div[class='wrapperTwo'] button:last-child")

    def __init__(self, driver):
        self.driver = driver

    def select_country(self):
        return self.driver.find_element(*Chose_country.select_countryr)

    def terms_agree(self):
        return self.driver.find_element(*Chose_country.terms_agreer)

    def finalize_order(self):
        return self.driver.find_element(*Chose_country.finalize)
    


