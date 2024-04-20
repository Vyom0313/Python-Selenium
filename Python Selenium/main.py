import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


os.environ['PATH'] += r"C:/Users/Vyom/Downloads/chromedriver-win64"
driver = webdriver.Chrome()

driver.get("https://jqueryui.com/resources/demos/progressbar/download.html")
driver.implicitly_wait(3)
my_element = driver.find_element(By.ID, 'downloadButton')
my_element.click()

progress_element = driver.find_element(By.CLASS_NAME, 'progress-label')
print(f"{progress_element.text}") #shows the text which the element is displaying

WebDriverWait(driver, 30).until(
    EC.text_to_be_present_in_element(  #this can be used to make the driver wait till some expected condition i.e. EC is achieved
        (By.CLASS_NAME, 'progress-label'), #element filteration
        'Complete!' #expected text
    )
)