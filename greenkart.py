import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from Chose_country import Chose_country
from Cart import Cart
from MainPage import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

# == ZMIENNE I LOKATORY ==
discount_code = "rahulshettyacademy"
promoInfo = (By.CSS_SELECTOR, ".promoInfo")
add_to_cart = (By.XPATH, "div/button")
item_name = (By.XPATH, "h4")

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
driver.implicitly_wait(2)

main_page = MainPage(driver)
main_page.open_page()
main_page.search_item().send_keys("ber")
time.sleep(2)
items = main_page.get_items()
products = []
for item in items:
    item.find_element(*add_to_cart).click()
    products.append(item.find_element(*item_name).text)
assert len(products) == 3
main_page.cart_box().click()
main_page.proceed().click()
print(products)


cart = Cart(driver)
cart.enter_promo().send_keys(discount_code)
cart.apply().click()
wait = WebDriverWait(driver, 6)
wait.until(expected_conditions.presence_of_element_located((promoInfo)))
sum = cart.sum_assert()
total_p = cart.price()
assert sum == total_p
assert "10%" == cart.discount()
assert float(cart.price_disc().text) < total_p
cart.order().click()


chose_country = Chose_country(driver)
dropdown = Select(chose_country.select_country())
dropdown.select_by_value("Poland")
chose_country.terms_agree().click()
chose_country.finalize_order().click()

