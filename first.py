#selenium practice script
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# # creating driver instance
driver = webdriver.Chrome("D:\Selenium_Essentials\chromedriver.exe")
driver.get("https://google.com/") 

print(driver.current_url)# current url
print(driver.title)# getting the drivertitle
box = driver.find_element_by_name("q")
box.send_keys("Hello World")
box.send_keys(Keys.RETURN) # Keys.RETURN is equivalent to pressing enter!!

print(driver.window_handles)

# Implicit and explicit waits
# explicit waits - makes your driver wait for a specific action to be completed (like content load using AJAX)
'''
Done using try finally block ->
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
element = WebDriverWait(driver, 5).until(
EC.presence_of_element_located((By.ID, "id-of-new-element"))
)
finally:
driver.quit()

'''

# implicit waits - An implicit wait makes the driver wait for a particular time.
driver.implicitly_wait(10) # if this doesnt work try this ->
time.sleep(10)
bar = driver.find_element_by_name("q")
bar.send_keys("Hello World")
bar.send_keys(Keys.RETURN)

# closing the tab
driver.close()

# closing all the tabs
driver.quit()