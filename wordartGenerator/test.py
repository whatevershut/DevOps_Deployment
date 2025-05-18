from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time

# Start browser
driver = webdriver.Chrome()

# Open your web app
driver.get("http://127.0.0.1:5000/")

# Input text
textarea = driver.find_element(By.TAG_NAME, "textarea")
textarea.clear()
textarea.send_keys("Hello World")

# Choose a font
dropdown = Select(driver.find_element(By.TAG_NAME, "select"))
dropdown.select_by_index(1)  # or select_by_visible_text("YourFont")

# Click Generate
generate_btn = driver.find_element(By.XPATH, "//button[text()='Generate']")
generate_btn.click()

# Wait for result to show
time.sleep(3)

# Validate that image is updated
img_container = driver.find_element(By.CLASS_NAME, "image-container")
assert img_container.is_displayed()

print("Test passed!")

driver.quit()
