from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Initialize logging
logging.basicConfig(level=logging.INFO)

# Initialize WebDriver (Make sure you have the ChromeDriver executable in your PATH or specify the path)
driver = webdriver.Chrome()

try:
    # Step 1: Open Telegram Web
    driver.get('https://web.telegram.org/')
    logging.info("Opened Telegram Web.")

    # Step 2: Click the "Log in by phone number" button
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="auth-or-form"]/div/button'))
    )
    login_by_phone = driver.find_element(By.XPATH, '//*[@id="auth-or-form"]/div/button')
    login_by_phone.click()
    logging.info("Clicked 'Log in by phone number'.")

    # Step 3: Wait for the phone input field to appear
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="sign-in-phone-number"]'))
    )
    phone_input = driver.find_element(By.XPATH, '//*[@id="sign-in-phone-number"]')
    phone_input.send_keys("YOUR_PHONE_NUMBER")  # Replace with your actual phone number
    logging.info("Entered phone number.")

    # Step 4: Click the "Next" button
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="phone-number-form"]/div/form/button[1]/div'))
    )
    next_button = driver.find_element(By.XPATH, '//*[@id="phone-number-form"]/div/form/button[1]/div')
    next_button.click()
    logging.info("Clicked 'Next' button.")

    # Step 5: Wait for the SMS code input field (if applicable)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="code-input"]'))  # Update this if different
    )
    logging.info("Waited for the SMS code input field.")

    # You may need to add further steps if there are additional verification steps
    # For example, entering the code received via SMS, etc.

except Exception as e:
    logging.error(f"Error during Telegram login process: {e}")
finally:
    driver.quit()
