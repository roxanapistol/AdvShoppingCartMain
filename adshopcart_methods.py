
import datetime
from time import sleep

from selenium import webdriver  # import selenium to the file
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
import advantage_shopping_cart.adshopcart_locators as locators
from selenium.webdriver.support.ui import Select  # this is for drop down lists
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


def check_homepage():

    driver.get(locators.adshopcart_url)

    check_list1 = ["SPEAKERS", "TABLETS", "LAPTOPS", "MICE"]
    for element in check_list1:
        if driver.find_element(By.XPATH, f"//span[contains(., '{element}')]").is_displayed():
            print(f"****We can see '{element}' link on the homepage.****")
        else:
            print("'{element}' link is not displayed on the homepage!")


    check_list2 = ["SPECIAL OFFER", "POPULAR ITEMS", "CONTACT US"]
    for item in check_list2:
        if driver.find_element(By.XPATH, f'//a[contains(., "{item}")]').is_displayed():
            sleep(0.5)
            driver.find_element(By.XPATH, f'//a[contains(., "{item}")]').click()
            sleep(1)
            if driver.find_element(By.XPATH, f"//*[self::h1 or self::h3][contains(., '{item}')]").is_displayed():
                sleep(0.5)
                print(f'****{item} is displayed.****')
            else:
                print(f'{item} is not displayed.')




    if driver.find_element(By.XPATH, '//span[contains(., "dvantage")]').is_displayed() \
        and driver.find_element(By.XPATH, '//span[contains(., "DEMO")]').is_displayed():
        sleep(0.5)
        print(f'****The logo is displayed: dvantage DEMO.****')
    else:
        print('The logo is not displayed, check your code.')


    driver.find_element(By.XPATH, '//h1[contains(.,"CONTACT US")]').is_displayed()
    Select(driver.find_element(By.NAME, 'categoryListboxContactUs')).select_by_visible_text('Speakers')
    sleep(0.25)
    Select(driver.find_element(By.NAME, 'productListboxContactUs')).select_by_visible_text('HP Roar Mini Wireless Speaker')
    sleep(0.5)
    driver.find_element(By.NAME, 'emailContactUs').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'subjectTextareaContactUs').send_keys(locators.subject)
    sleep(0.5)
    driver.find_element(By.ID, 'send_btnundefined').click()
    sleep(0.5)
    if driver.find_element(By.XPATH, '//*[@id="registerSuccessCover"]/div/a').is_displayed():
        sleep(0.5)
        print('****Continue shopping button is displayed.****')
    else:
        print('The Continue shopping is not displayed')







def sign_up():
    print(f'---The new account is being created:---')
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1.5)
    driver.find_element(By.CSS_SELECTOR, 'a.create-new-account').click()
    sleep(0.5)
    driver.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.username)
    sleep(0.5)
    driver.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
    sleep(0.5)
    driver.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
    sleep(0.5)
    driver.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone)
    sleep(0.5)
    Select(driver.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text(locators.country)
    sleep(0.5)
    driver.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
    sleep(0.5)
    driver.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
    sleep(0.5)
    driver.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.province)
    sleep(0.5)
    driver.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
    sleep(0.5)
    driver.find_element(By.NAME, 'i_agree').click()
    sleep(0.5)
    driver.find_element(By.ID, 'register_btnundefined').click()
    sleep(0.5)
    print(f'---The new account is created.---')


def check_full_name():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    #driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    #driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[@translate="My_account"]').click()
    driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate = "My_account"]').click()
    sleep(0.5)

    if driver.find_element(By.XPATH, f'//label[contains(., "{locators.full_name}")]').is_displayed():
        print(f'---The full name of the new user is: {locators.full_name}.---')
    else:
        print(f"Something it's not working, not able to open account page.")
    sleep(0.5)


def check_orders():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My orders")]').click()
    #driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[@translate="My_orders"]').click()
    #driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate = "My_orders"]').click()
    sleep(0.5)

    assert driver.find_element(By.XPATH, '//label[contains(., "No orders")]').is_displayed()
    sleep(0.5)
    no_order = driver.find_element(By.XPATH, '//label[contains(., "No orders")]').is_displayed()
    if no_order == True:
        print(f"---Checking for no orders on the account page.---")
    else:
        print(f'Something is wrong, check the code.')


def log_in():
    if driver.current_url == locators.adshopcart_url:
        print(f'---You are again on the Advantage Shopping website. We are checking the new account.---')
        sleep(0.5)
        driver.find_element(By.ID, 'menuUser').click()
        sleep(0.5)
        driver.find_element(By.NAME, 'username').send_keys(locators.username)
        sleep(0.5)
        driver.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(0.5)
        driver.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(0.5)
        print(f'---Successful log in with new account!---')
    else:
        print('Something is wrong, check your code or website.')




def log_out():
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    #driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "Sign out")]').click()
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[@translate="Sign_out"]').click()
    #driver.find_element(By.CSS_SELECTOR, 'div#loginMiniTitle > label[translate = "Sign_out"]').click()
    sleep(0.5)


def delete_test_account():
    print(f"---We need to delete the new user.---")
    driver.find_element(By.ID, 'menuUser').click()
    sleep(0.5)
    #driver.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[contains(., "My account")]').click()
    driver.find_element(By.XPATH, '//div[@id="loginMiniTitle"]/label[@translate="My_account"]').click()
    sleep(0.5)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    driver.find_element(By.XPATH, '//button[contains(., "Delete Account")]').click()
    sleep(0.5)
    driver.find_element(By.CSS_SELECTOR, 'div.deletePopupBtn.deleteRed').click()
    sleep(3)
    #driver.switch_to.alert.accept() # this is for pop-up windows

    #verify the account is deleted
    driver.find_element(By.ID, 'menuUser').click()
    sleep(1)

    driver.find_element(By.NAME, 'username').send_keys(locators.username)
    sleep(0.5)
    driver.find_element(By.NAME, 'password').send_keys(locators.password)
    sleep(0.5)
    driver.find_element(By.ID, 'sign_in_btnundefined').click()
    sleep(0.5)

    if driver.find_element(By.XPATH, '//*[@id="signInResultMessage"]'
                                     '[contains(., "Incorrect user name or password")]').is_displayed():
        print(f'---You have successfully deleted the account of {locators.username}.---')
    else:
        print('Something is wrong.')




def tearDown():
    if driver is not None:
        print('===========================================')
        print(f'->The test is completed at: {datetime.datetime.now()}')
        sleep(2)
        driver.close()
        driver.quit()


# setUp ()
# sign_up()
# check_full_name()
# check_orders()
# log_out()
# log_in()
# delete_test_account()
# check_homepage()
# tearDown()