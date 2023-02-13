import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service


@pytest.fixture(scope="class")  # wykona sie raz dla calej klasy, a nie dla każdej metody
def setup(request):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.maximize_window()
    driver.get("https://rahulshettyacademy.com/seleniumPractise/")
    driver.implicitly_wait(2)
    
    # nie mozemy uzyc return i yield jednoczesnie, dlatego uzywamy request
    # request przenosi driver do klasy (cls) 
    # i ustawia driver z test_e2e na driver z conftest
    request.cls.driver = driver
    
    yield
    driver.close()
