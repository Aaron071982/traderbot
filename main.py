# Import necessary libraries
import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")  # Useful for Linux
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes on resource-limited systems

# Configure the WebDriver with the Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
# Example: Open a webpage
driver.get("https://web.telegram.org/")
print(driver.title)

input("Press Enter to close the browser...")
driver.quit()

# Step 1: Set up logging
logging.basicConfig(
    filename='bullx_login.log',  # Save logs to a file
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

# Step 2: Set up ChromeDriver (visible browser)
#driver = webdriver.Chrome(ChromeDriverManager().install())
logging.info("ChromeDriver initialized.")

# Step 3: Open Telegram Web
try:
    driver.get('https://web.telegram.org/')  # Open Telegram Web
    logging.info("Opened Telegram Web.")


    # LINES 55 - 96 Aare the authentication for telegram

    # Step 2.1: Log in to Telegram
    # Click the "Log in by phone number" button
    login_by_phone = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="auth-qr-form"]/div/button'))  # Replace with actual button locator
    )
    login_by_phone.click()
    logging.info("Clicked 'Log in by phone number'.")

    # Step 2.2: Enter the phone number
    # Wait for the phone number input field to appear
    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="sign-in-phone-number"]'))  # Replace with actual field locator
    )
    phone_input.send_keys('')  # Replace with your phone number
    logging.info("3473090431")

    # Click the "Next" button
    next_button = driver.find_element(By.XPATH, '//*[@id="auth-phone-number-form"]/div/form/button[1]/div')  # Replace with actual button locator
    next_button.click()
    logging.info("Clicked Next.")

    # Step 2.3: Wait for the SMS code input field
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//input[@name="code"]'))  # Replace with actual field locator
    )
    logging.info("SMS code input field appeared.")

    # Step 2.4: Manually enter the SMS code
    print("Please check your phone for the SMS code and enter it below:")
    sms_code = input("Enter the SMS code: ")  # Wait for manual input
    logging.info("SMS code entered manually.")

    # Enter the SMS code
    code_input = driver.find_element(By.XPATH, '//input[@name="code"]')  # Replace with actual field locator
    code_input.send_keys(sms_code)
    logging.info("Entered SMS code.")

    # Step 2.5: Wait for Telegram to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//div[contains(text(), "Chats")]'))  # Wait for chats to load
    )
    logging.info("Telegram is ready.")

    # Step 5: Open BullX Chat
    # Search for the BullX chat
    search_box = driver.find_element(By.XPATH, '//*[@id="telegram-search-input"]')  # Replace with actual search box locator
    search_box.send_keys('BullX')
    time.sleep(2)  # Wait for search results
    logging.info("Searched for BullX chat.")

    # Click on the BullX chat
    bullx_chat = driver.find_element(By.XPATH, '//*[@id="LeftColumn-main"]/div[2]/div[2]/div/div[2]/div/div[2]/div/div/div/div[2]/div')  # Replace with actual chat locator
    bullx_chat.click()
    logging.info("Opened BullX chat.")

    # Step 6: Type /start in the chat
    chat_input = driver.find_element(By.XPATH, '//*[@id="editable-message-text"]')  # Replace with actual chat input locator
    chat_input.send_keys('/start')
    chat_input.send_keys(Keys.RETURN)
    logging.info("Sent /start command to BullX.")

    # Step 7: Wait for BullX to reply with the login message
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="message-212"]/div[3]/div[1]/div[1]/div'))  # Replace with actual message locator
    )
    logging.info("BullX replied with the login message.")

    # Step 8: Click the Login button in the BullX reply
    login_button = driver.find_element(By.XPATH, '//*[@id="message-212"]/div[3]/div[2]/div[1]/button')  # Replace with actual button locator
    login_button.click()
    logging.info("Clicked Login button.")

    # Step 8.25: Handle the "Open Link" pop-up
    # Wait for the pop-up to appear
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="portals"]/div[2]/div/div/div[2]/div[2]'))  # Replace with actual pop-up locator
    )
    logging.info("Pop-up appeared.")

    # Click the "Open Link" button in the pop-up
    open_link_button = driver.find_element(By.XPATH, '//*[@id="portals"]/div[2]/div/div/div[2]/div[2]/div/button[1]')  # Replace with actual button locator
    open_link_button.click()
    logging.info("Clicked Open Link button.")

    # Step 8.5: Wait for the login page to load
    try:
        # Wait for the 2FA passcode input field to appear
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/main/div/div[2]/div[1]/div[2]/h4'))  # Replace with actual locator
        )
        logging.info("Login page loaded.")

        # Step 9: Log in to BullX
        # Enter the 2FA passcode
        password_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div/div[2]/div[1]/div[3]/div[2]')  # Replace with actual field name
        password_input.send_keys('200507')  # Replace with your 2FA passcode
        logging.info("Entered 2FA passcode.")

        # Click the "Next" button
        next_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[2]/main/div/div[2]/div[1]/div[3]/div[3]/button')  # Replace with actual button locator
        next_button.click()
        logging.info("Clicked Next.")

    except Exception as error:
        logging.error(f"An error occurred during login: {error}")

    # Step 10: Wait for the trading page to load
    WebDriverWait(driver, 10).until(
        EC.url_contains('https://neo.bullx.io/')  # Replace with the expected URL after login
    )
    logging.info("BullX trading page loaded.")

except Exception as error:
    logging.error(f"An error occurred: {error}")

# Step 11: Keep the browser open for manual inspection
logging.info("Login process completed. Keeping the browser open for inspection.")
input("Press Enter to close the browser...")  # Wait for user input before closing

# Step 12: Close the browser
driver.quit()
logging.info("Browser closed.")