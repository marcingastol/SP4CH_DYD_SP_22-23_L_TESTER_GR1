'''
Let's use the demo website "https://the-internet.herokuapp.com/login" to test the login functionality with Selenium 4 in Python. 
This website has a login form with a username and password field, as well as a login button.

REMEMBER! INSTALL SELENIUM IN VIRTUAL ENVIRONEMNT!

python -m venv .venv
.\.venv\Scripts\activate

pip install selenium

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the browser
browser = webdriver.Chrome()

# Open the login page
browser.get("https://the-internet.herokuapp.com/login")

# Fill in the username and password fields
username_input = browser.find_element(By.ID, "username")
password_input = browser.find_element(By.ID, "password")
username_input.send_keys("tomsmith")
password_input.send_keys("SuperSecretPassword!")

# Click the login button
login_button = browser.find_element(By.XPATH, "//button[@type='submit']")
login_button.click()

# Wait for the secure area page to load
time.sleep(1)

# Check if the login was successful by finding the logout button
logout_button = browser.find_element(By.XPATH, "//a[@href='/logout']")
assert logout_button is not None

print("Login test with Selenium 4 passed successfully.")
browser.quit()
