import pytest
import time
import sys
sys.path.append('C:/Users/Aleksandra-Acer/PycharmProjects/pythonFramework/greencart/pageObjects')
sys.path.append('C:/Users/Aleksandra-Acer/PycharmProjects/pythonFramework/greencart/utilities')
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from HomePage import MainPage
from BaseClass import BaseClass


# @pytest.mark.usefixture("setup") # nie musimy bo dziedziczymy po BaseClass
class TestOne(BaseClass):
    
    # == ZMIENNE I LOKATORY ==
    discount_code = "rahulshettyacademy"
    promoInfo = (By.CSS_SELECTOR, ".promoInfo")
    country_name = "Poland"
    
    def test_e2e(self):
        
        main_page = MainPage(self.driver)
        #  main_page.open_page()
        main_page.search_item().send_keys("ber")
        time.sleep(2)
        items = main_page.get_items()
        main_page.add_to_basket(items)
        main_page.cart_box().click()
        
        cart = main_page.proceed()
        cart.enter_promo().send_keys(self.discount_code)
        cart.apply().click()
        self.verify_presence(self.promoInfo)
        cost = cart.sum_assert()
        total_p = cart.price()
        assert cost == total_p
        assert "10%" == cart.discount()
        assert float(cart.price_disc().text) < total_p
        
        chose_country = cart.order()
        dropdown = Select(chose_country.select_country())
        dropdown.select_by_value(self.country_name)
        chose_country.terms_agree().click()
        chose_country.finalize_order().click()

        

