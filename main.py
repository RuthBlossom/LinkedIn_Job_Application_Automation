# The webdriver module provides the API for browser automation. It allows you to interact with web elements, navigate web pages, and perform various actions on them.
from selenium import webdriver
# The Keys module provides special keys like ENTER, TAB, ARROW_UP, etc., which can be used to simulate keyboard actions while interacting with web elements.
from selenium.webdriver.common.keys import Keys
# he NoSuchElementException class is raised when an element is not found on the web page, typically used for handling scenarios when an expected element is missing.
from selenium.common.exceptions import NoSuchElementException
# The By module provides mechanisms to locate elements on a web page using different locator strategies like ID, CLASS_NAME, CSS_SELECTOR, etc.
from selenium.webdriver.common.by import By
# The time module provides various functions for working with time-related tasks, such as sleeping for a specified duration, measuring elapsed time, etc.
import time

# Your LinkedIn credentials
ACCOUNT_EMAIL = "YOUR LOGIN EMAIL"
ACCOUNT_PASSWORD = "YOUR LOGIN PASSWORD"
PHONE = "YOUR PHONE NUMBER"

# Path to ChromeDriver executable
chrome_driver_path = "C:\\chromedriver.exe"  # Assuming the ChromeDriver executable is named chromedriver.exe

# Optional - Keep the browser open if the script crashes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# Create and configure the Chrome webdriver with the specified path to ChromeDriver and options
driver = webdriver.Chrome(executable_path=chrome_driver_path, options=chrome_options)

# Open LinkedIn Jobs page
driver.get("https://www.linkedin.com/jobs/search/?currentJobId=3586148395&f_LF=f_AL&geoId=101356765&"
           "keywords=python&location=London%2C%20England%2C%20United%20Kingdom&refresh=true")

# Click Reject Cookies Button
time.sleep(2)  # Wait for 2 seconds before interacting with the page
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()  # Click on the Reject Cookies button

# Click Sign in Button
time.sleep(2)  # Wait for 2 seconds before interacting with the page
sign_in_button = driver.find_element(by=By.LINK_TEXT, value="Sign in")
sign_in_button.click()  # Click on the Sign in button

# Sign in
time.sleep(5)  # Wait for 5 seconds before entering credentials
email_field = driver.find_element(by=By.ID, value="username")
email_field.send_keys(ACCOUNT_EMAIL)  # Enter the email address
password_field = driver.find_element(by=By.ID, value="password")
password_field.send_keys(ACCOUNT_PASSWORD)  # Enter the password
password_field.send_keys(Keys.ENTER)  # Press Enter to submit the form

# CAPTCHA - Solve Puzzle Manually
input("Press Enter when you have solved the Captcha")  # Wait for user to manually solve the CAPTCHA

# Get Listings
time.sleep(5)  # Wait for 5 seconds before fetching job listings
all_listings = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")  # Find all job listings

# Apply for Jobs
for listing in all_listings:
    print("Opening Listing")
    listing.click()  # Click on a job listing to view details
    time.sleep(2)  # Wait for 2 seconds after clicking

    try:
        # Click Apply Button
        apply_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-s-apply button")
        apply_button.click()  # Click on the apply button

        # Insert Phone Number
        time.sleep(5)  # Wait for 5 seconds
        phone = driver.find_element(by=By.CSS_SELECTOR, value="input[id*=phoneNumber]")
        if phone.text == "":
            phone.send_keys(PHONE)  # Enter phone number

        # Check the Submit Button
        submit_button = driver.find_element(by=By.CSS_SELECTOR, value="footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            print("Complex application, skipped.")
            continue
        else:
            # Click Submit Button
            print("Submitting job application")
            submit_button.click()  # Click on the submit button

        time.sleep(2)  # Wait for 2 seconds
        # Click Close Button
        close_button = driver.find_element(by=By.CLASS_NAME, value="artdeco-modal__dismiss")
        close_button.click()  # Close the application modal

    except NoSuchElementException:
        print("No application button, skipped.")  # Print message if no apply button is found
        continue

time.sleep(5)  # Wait for 5 seconds before quitting the driver
driver.quit()  # Quit the WebDriver session



