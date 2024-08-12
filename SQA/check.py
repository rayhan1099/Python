from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Path to your WebDriver. Make sure to download the appropriate driver for your browser.
# Here, I'm using Chrome, so make sure you have chromedriver installed and its path specified.
driver = webdriver.Chrome('/path/to/chromedriver')

# Open SQA admin site
driver.get('https://admin.theaddresspms.com/users/login/')

# Find username and password fields and login button
username_field = driver.find_element_by_id('Email')
password_field = driver.find_element_by_id('Password')
login_button = driver.find_element_by_id('Log in')

# Fill in username and password
username_field.send_keys('admin@admin.com')
password_field.send_keys('@admin123')

# Click the login button
login_button.click()

# Wait for the dashboard to load
dashboard_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.ID, 'dashboard'))
)

# Perform other actions as needed, such as navigating to specific pages, filling forms, etc.

# Example: Click on a link to navigate to a specific page
specific_page_link = driver.find_element_by_id('specificPageLink')
specific_page_link.click()

# Example: Fill in a form field
form_field = driver.find_element_by_id('formField')
form_field.send_keys('some value')

# Example: Submit the form
submit_button = driver.find_element_by_id('submitButton')
submit_button.click()

# After you're done, you can close the browser
driver.quit()
