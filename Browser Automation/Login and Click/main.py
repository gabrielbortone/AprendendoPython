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


def main():
    driver = get_driver()

    driver.find_element(by="id", value="id_username").send_keys("automated")
    time.sleep(2)

    driver.find_element(by="id", value="id_password").send_keys("automatedautomated" + 
                                                                Keys.RETURN)
    driver.find_element(by="xpath", value="/html/body/nav/div/a").click()
    print(driver.current_url)
    return ""

print(main())