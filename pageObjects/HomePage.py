from selenium.webdriver.common.by import By
from CartPage import Cart


class MainPage:

    home_page = "https://rahulshettyacademy.com/seleniumPractise/#/"
    search = (By.XPATH, "//input[@class='search-keyword']")
    products = (By.XPATH, "//div[@class='products']/div")
    cart = (By.CLASS_NAME, "cart-icon")
    submit_cart = (By.XPATH, "//div[@class='cart-preview active']/div[2]/button")
    add_to_cart = (By.XPATH, "div/button")
    item_name = (By.XPATH, "h4")
    
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

    def add_to_basket(self, items):
        products = []
        for item in items:
            item.find_element(*self.add_to_cart).click()
            products.append(item.find_element(*MainPage.item_name).text)
        assert len(products) == 3
        print(products)

    def cart_box(self):
        return self.driver.find_element(*MainPage.cart)

    def proceed(self):
        self.driver.find_element(*MainPage.submit_cart).click()
        cart = Cart(self.driver)  # forcing to use next page object, optimizing code
        return cart
