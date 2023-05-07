'''
Let's use the demo website "https://the-internet.herokuapp.com/dynamic_controls" to test the dynamic controls feature with Selenium 4 in Python. 
This website has a checkbox and an input field with buttons to enable/disable the input field and add/remove the checkbox.

REMEMBER! INSTALL SELENIUM IN VIRTUAL ENVIRONEMNT!

python -m venv .venv
.\.venv\Scripts\activate

pip install selenium

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the browser
browser = webdriver.Chrome()

# Open the dynamic controls page
browser.get("https://the-internet.herokuapp.com/dynamic_controls")

# Find the checkbox and remove button
checkbox = browser.find_element(By.CSS_SELECTOR, "#checkbox > input")
remove_button = browser.find_element(By.XPATH, "//button[@onclick='swapCheckbox()']")

# Click the remove button
remove_button.click()

# Wait for the checkbox to be removed
WebDriverWait(browser, 10).until(EC.invisibility_of_element(checkbox))

# Find the enable button and input field
enable_button = browser.find_element(By.XPATH, "//button[@onclick='swapInput()']")
input_field = browser.find_element(By.CSS_SELECTOR, "#input-example > input")

# Click the enable button
enable_button.click()

# Wait for the input field to be enabled
WebDriverWait(browser, 10).until(EC.element_to_be_clickable(input_field))

# Type text into the enabled input field
input_field.send_keys("Hello, Selenium 4!")

# Check if the input field contains the expected text
assert input_field.get_attribute("value") == "Hello, Selenium 4!"

print("Dynamic controls test with Selenium 4 passed successfully.")
browser.quit()
