from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

# Set Chrome options to use your personal profile
chrome_options = Options()
chrome_options.add_argument("--disable-extensions")
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")  # Useful for Linux/Mac
chrome_options.add_argument("--disable-dev-shm-usage")  # Prevent crashes

# Set the user data directory (where your Chrome profiles are stored)
chrome_options.add_argument("user-data-dir=/Users/kazi/Library/Application Support/Google/Chrome") 

# Set the profile directory (replace with your actual profile, in this case, Profile 2)
chrome_options.add_argument("profile-directory=Profile 2")

# Configure the WebDriver with the Service object
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open a test website
driver.get("https://www.google.com")
