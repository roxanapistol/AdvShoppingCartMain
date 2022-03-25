import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import adshopcart_locators as locators
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException


s = Service(executable_path='../chromedriver.exe')
driver = webdriver.Chrome(service=s)

def setUp():
    print(f'->Launch {locators.app} App.')
    print(f'Test Started at: {datetime.datetime.now()}')
    print('=========================================')

    driver.maximize_window()

    driver.implicitly_wait(30)

    driver.get(locators.adshopcart_url)


    if driver.current_url == locators.adshopcart_url and driver.title == locators.adshopcart_home_page_title:
        print(f'->Bravo! {locators.app} App website launched successfully!')
        print(f'->{locators.app} homepage URL: {driver.current_url}, homepage title: {driver.title}')
        sleep(0.5)

    else:
        print(f'->{locators.app} did not launched, check your code or application.')
        print(f'->Current URL: {driver.current_url}, page title: {driver.title}')
        


def tearDown():
    if driver is not None:
        print('===========================================')
        print(f'->The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


setUp()
tearDown()
