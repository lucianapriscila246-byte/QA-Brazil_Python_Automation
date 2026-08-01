from selenium.webdriver.common.by import By
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("https://cnt-12b6d93a-6105-44e1-a0aa-b8fb7192f307.containerhub.tripleten-services.com?lng=pt")
time.sleep(2)

driver.find_element(By.ID, "from").send_keys("East 2nd Street, 601")
time.sleep(1)
driver.find_element(By.ID, "to").send_keys("1300 1st St")
time.sleep(1)
driver.quit()