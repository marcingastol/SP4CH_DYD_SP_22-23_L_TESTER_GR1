'''
Let's use the demo website "https://demoqa.com/automation-practice-form" to test a web form submission with Selenium 4 in Python. 
This website has a form that collects a user's name, gender, email, mobile number, and other details.

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

# Open the form page
browser.get("https://demoqa.com/automation-practice-form")

# Fill in the form fields
first_name_input = browser.find_element(By.ID, "firstName")
last_name_input = browser.find_element(By.ID, "lastName")
email_input = browser.find_element(By.ID, "userEmail")
gender_input = browser.find_element(By.XPATH, "//label[@for='gender-radio-1']")
mobile_number_input = browser.find_element(By.ID, "userNumber")

first_name_input.send_keys("John")
last_name_input.send_keys("Doe")
email_input.send_keys("john.doe@example.com")
gender_input.click()
mobile_number_input.send_keys("1234567890")

# Submit the form
submit_button = browser.find_element(By.ID, "submit")
submit_button.click()

# Wait for the submission result to load
time.sleep(2)

# Check if the form submission was successful
submitted_table = browser.find_element(By.XPATH, "//table[@class='table table-dark table-striped table-bordered table-hover']")
output_name = submitted_table.find_element(By.XPATH, "//td[text()='Student Name']/following-sibling::td").text
output_email = submitted_table.find_element(By.XPATH, "//td[text()='Student Email']/following-sibling::td").text
output_gender = submitted_table.find_element(By.XPATH, "//td[text()='Gender']/following-sibling::td").text
output_mobile = submitted_table.find_element(By.XPATH, "//td[text()='Mobile']/following-sibling::td").text

assert output_name == "John Doe"
assert output_email == "john.doe@example.com"
assert output_gender == "Male"
assert output_mobile == "1234567890"

print("Form submission test with Selenium 4 passed successfully.")
browser.quit()
