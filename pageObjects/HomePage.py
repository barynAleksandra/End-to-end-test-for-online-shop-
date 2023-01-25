from selenium.webdriver.common.by import By


class MainPage:

    home_page = "https://rahulshettyacademy.com/seleniumPractise/#/"
    search = (By.XPATH, "//input[@class='search-keyword']")
    products = (By.XPATH, "//div[@class='products']/div")
    cart = (By.CLASS_NAME, "cart-icon")
    submit_cart = (By.XPATH, "//div[@class='cart-preview active']/div[2]/button")

    def __init__(self, driver):
        self.driver = driver

    
    def open_page(self):
        self.driver.get(MainPage.home_page)

    
    def search_item(self):
        return self.driver.find_element(*MainPage.search)

    
    def get_items(self):
        items = self.driver.find_elements(*MainPage.products)
        assert len(items) > 0
        return items


    def cart_box(self):
        return self.driver.find_element(*MainPage.cart)


    def proceed(self):
        return self.driver.find_element(*MainPage.submit_cart)
