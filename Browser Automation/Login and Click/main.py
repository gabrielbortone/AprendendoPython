from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("disabled-infobars")
    options.add_argument("start-maxized")
    options.add_argument("disabled-dev-shm-usage")
    options.add_argument("no-sandbox")
    options.add_experimental_option("excludeSwitches",
        ["enable-automation"])
    options.add_argument("disabled-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.get("http://automated.pythonanywhere.com/login/")

    return driver

def clean_text(text):
    """Extract only the temperature from text"""
    output = float(text.split(": ")[1])
    return output


def login(driver):
    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)
    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + 
                                                              Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()

def get_phrase(driver):
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[1]")
    return element.text

def get_temperature(driver):
    driver = get_driver()
    time.sleep(3)
    element = driver.find_element(by="xpath", value="/html/body/div[1]/div/h1[2]")
    return clean_text(element.text)


def main():
    driver = get_driver()
    login(driver)
    print(get_phrase(driver))
    print(get_temperature(driver))

print(main())