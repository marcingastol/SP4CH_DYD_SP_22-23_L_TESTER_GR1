'''
Let's use the demo website "https://the-internet.herokuapp.com/drag_and_drop" to test the drag-and-drop functionality with Selenium 4 in Python. 
This website has two boxes (A and B) that you can drag and drop onto each other.

REMEMBER! INSTALL SELENIUM IN VIRTUAL ENVIRONEMNT!

python -m venv .venv
.\.venv\Scripts\activate

pip install selenium

'''

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize the browser
browser = webdriver.Chrome()

# Open the drag-and-drop page
browser.get("https://the-internet.herokuapp.com/drag_and_drop")

# Locate the boxes A and B
box_a = browser.find_element(By.ID, "column-a")
box_b = browser.find_element(By.ID, "column-b")

# Perform the drag-and-drop action
action_chains = ActionChains(browser)
action_chains.drag_and_drop(box_a, box_b).perform()

# Wait for the boxes to swap positions
time.sleep(1)

# Check if the boxes have swapped positions
box_a_header = box_a.find_element(By.XPATH, ".//header").text
box_b_header = box_b.find_element(By.XPATH, ".//header").text

assert box_a_header == "B"
assert box_b_header == "A"

print("Drag and drop test with Selenium 4 passed successfully.")
browser.quit()
