#1 Open Browser
from selenium import webdriver
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
print("Current URL:", driver.current_url)
driver.quit()

#2 Add wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, "gh-ac-box2")))
print("Current URL:", driver.current_url)
driver.quit()

#3 Search items:
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
print("Current URL:", driver.current_url)
search = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "gh-ac"))
)
search.send_keys("women watch")
search.send_keys(Keys.RETURN)
time.sleep(2)
driver.quit()

#4 Verify the search result
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get("https://www.ebay.com")
print("Current URL:", driver.current_url)
search = WebDriverWait(driver, 10).until(
    EC.visibility_of_element_located((By.ID, "gh-ac"))
)
search.send_keys("women watch")
search.send_keys(Keys.RETURN)
header = driver.find_element(By.XPATH, "//h1[contains(@class, 'srp-controls__count-heading')]")
    
time.sleep(2)

driver.quit()
