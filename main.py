from selenium import webdriver
from selenium.webdriver import Keys
import time
from time import sleep
from selenium.webdriver.common.by import By


driver = webdriver.Chrome()
driver.get('https://m.youtube.com/')
# elem = driver.find_element(By.TAG_NAME, 'search')
# elem = driver.find_element(By.XPATH, '//*[@id="search"]')
# elem = driver.find_element(By.LINK_TEXT, "Explore")
elem = driver.find_element(By.TAG_NAME, 'html')
elem.send_keys(Keys.END)
time.sleep(5)
elem.send_keys(Keys.HOME)
# driver.refresh()
# elem.click()
# time.sleep(5)
# driver.back()
# elem = driver.find_element(By.LINK_TEXT, "Trending")
# time.sleep(5)
# driver.forward()
# elem.click()
# elem.clear()
# elem.send_keys("IGN")
# elem.send_keys(Keys.RETURN)
print(driver.current_url)