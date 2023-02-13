from selenium.webdriver.common.by import By


class ChoseCountry:

    country = (By.CSS_SELECTOR, "div[class='wrapperTwo'] div select")
    terms = (By.XPATH, "//input[@class='chkAgree']")
    finalize = (By.CSS_SELECTOR, "div[class='wrapperTwo'] button:last-child")

    def __init__(self, driver):
        self.driver = driver

    def select_country(self):
        return self.driver.find_element(*ChoseCountry.country)

    def terms_agree(self):
        return self.driver.find_element(*ChoseCountry.terms)

    def finalize_order(self):
        return self.driver.find_element(*ChoseCountry.finalize)
    


