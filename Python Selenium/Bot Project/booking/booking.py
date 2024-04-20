import booking.constants as const
import os
from selenium import webdriver
from selenium.webdriver.common.by import By

#this class inherits from chrome class in order to use the specifically designed
#methods in Booking as well as pre-defined methods from webdriver.chrome class
class Booking(webdriver.Chrome):
    #constructer of class
    def __init__(self, driver_path = r"C:/Users/Vyom/Downloads/chromedriver-win64", teardown = False):
        self.driver_path = driver_path
        self.teardown = teardown
        os.environ['PATH'] += self.driver_path
        super(Booking, self).__init__()
        self.implicitly_wait(15)
        self.maximize_window() #to maximaize window of browser

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.teardown:
            self.quit()
    
    def land_first_page(self):
        self.get(const.BASE_URL)

    def change_currency(self, currency=None):
        currency_element = self.find_element(
            By.CSS_SELECTOR, 'button[data-tooltip-text = "Choose your currency"]'
        )
        currency_element.click()
        selected_currency_element = self.find_element(
            By.CSS_SELECTOR, 'a[data-model-header-async-url-param*="selected_currency = {currency}"]'
        )