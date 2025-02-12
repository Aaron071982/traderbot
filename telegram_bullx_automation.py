import time
import logging
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

import time
# Set Chrome options to use a specific user profile
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")  # Useful for Linux
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes on resource-limited systems
# Set the user data directory (where your Chrome profiles are stored)
chrome_options.add_argument("user-data-dir=/Users/kazi/Library/Application Support/Google/Chrome") 

# Set the profile directory (replace with your actual profile, in this case, Profile 2)
chrome_options.add_argument("profile-directory=Profile 2")

# Configure the WebDriver with the Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Set up logging
logging.basicConfig(
    filename='bullx_login.log',  # Save logs to a file
    level=logging.INFO,  # Log level
    format='%(asctime)s - %(levelname)s - %(message)s'  # Log format
)

logging.info("ChromeDriver initialized.")

# Open Telegram Web
try:
    driver.get('https://web.telegram.org/')  # Open Telegram Web
    logging.info("Opened Telegram Web.")



    # Step 1: Locate and click on the BullX chat
        # Wait for the BullX chat to appear in the chat list
    bullx_chat = driver.find_element(By.XPATH, '//*[@id="LeftColumn-main"]/div[2]/div/div/div/div/div[2]/div[1]/a')
    bullx_chat.click()
    logging.info("Clicked on BullX chat.")
   



    # Step 2: Type /start in the chat
    chat_input = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="editable-message-text"]'))  # Replace with actual chat input locator
    )
    chat_input.send_keys('/start')
    chat_input.send_keys(Keys.RETURN)
    logging.info("Sent /start command to BullX.")

    # Wait 30 seconds before checking for the login message
    logging.info("Waiting 5 seconds before proceeding...")
    time.sleep(5)

   

    # Step 4: Click the Login button in the BullX reply
    login_button = driver.find_element(By.XPATH, '//*[@id="message-271"]/div[3]/div[2]/div[1]/button/div')  # Replace with actual button locator
    login_button.click()
    logging.info("Clicked Login button.")

    # Step 5: Handle the "Open Link" pop-up
    # Wait for the pop-up to appear
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="portals"]/div[2]/div/div/div[2]/div[2]'))  # Replace with actual pop-up locator
    )
    logging.info("Pop-up appeared.")

    # Click the "Open Link" button in the pop-up
    open_link_button = driver.find_element(By.XPATH, '//*[@id="portals"]/div[2]/div/div/div[2]/div[2]/div/button[1]')  # Replace with actual button locator
    open_link_button.click()
    logging.info("Clicked Open Link button.")



    # Step 6: Wait for the login page to load
    try:
        # Wait for the 2FA passcode input field to appear
        password_input = WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[2]/main/div/div[2]/div[1]/div[3]/div[2]/input[1]"]'))  # Generic locator for better matching
        )
        logging.info("2FA Input field detected.")

        # Step 7: Click the input field before entering text
        password_input.click()
        time.sleep(1)  # Small delay to ensure it's ready

        # Enter the 2FA passcode
        password_input.send_keys('2')  # Replace with your 2FA passcode
        logging.info("Entered 2FA passcode.")

        # **Backup: JavaScript Input if Normal Input Fails**
        driver.execute_script("arguments[0].value = arguments[1];", password_input, '200507')
        time.sleep(1)  # Allow time for value to register

        # Step 8: Click the "Next" button
        next_button = driver.find_element(By.XPATH, '//button[contains(text(), "Next")]')  # Generic "Next" button locator
        next_button.click()
        logging.info("Clicked Next.")

    except Exception as error:
        logging.error(f"An error occurred during login: {error}")

    # Step 9: Wait for the trading page to load
    WebDriverWait(driver, 20).until(
        EC.url_contains('https://neo.bullx.io/')  # Replace with the expected URL after login
    )
    logging.info("BullX trading page loaded.")

except Exception as error:
    logging.error(f"An error occurred: {error}")

# Keep the browser open for manual inspection
logging.info("Login process completed. Keeping the browser open for inspection.")
input("Press Enter to close the browser...")  # Wait for user input before closing

# Close the browser
driver.quit()
logging.info("Browser closed.")