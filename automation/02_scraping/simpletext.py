from selenium import webdriver
from selenium.webdriver.common.by import By 
from selenium.webdriver.chrome.service import Service

path_chrome_driver = "./chromedriver_linux64/chromedriver"

xpath = "/html/body/header/div[2]/div/h1/span"
url = "https://gianfrancolasala.com/"

def get_driver(url='https://gianfrancolasala.com/'):
    # Make browsing easier
    options = webdriver.ChromeOptions()
    options.add_argument("disable-infobars")
    options.add_argument("start-maximized")
    options.add_argument('disable-dev-shm-usage') # avoid issues when interact with the browser on a linux
    options.add_argument("no-sandbox")

    service = Service(path_chrome_driver)
    options.add_experimental_option("excludeSwitches", ["enable-automation"]) 
    options.add_argument("disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options, service=service)
    driver.get(url)
    return driver

def main(url,xpath):
    driver = get_driver(url)
    # ? Deprecated: element = driver.find_element_by_xpath("/html/body/header/div[2]/div/h1/span")
    element = driver.find_element(by=By.XPATH, value=xpath)
    return element

print(main(url,xpath))