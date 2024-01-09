from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from time import sleep

# Initialize a web browser (in this case, Chrome)
browser = webdriver.Chrome()  # Make sure to have the appropriate webdriver for your browser

# URL to open
url = "http://jazz.wifi/index.html#setting"  # Replace with the URL you want to visit

# Open the URL
browser.get(url)

# Wait for the page to load completely (adjust the timeout as needed)
wait = WebDriverWait(browser, 10)  # Timeout of 10 seconds
element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))  # Replace 'element_id' with the ID of the element you want to interact with

# Perform clicks or other actions after the page has loaded
# Example: Clicking a button
button = browser.find_element(By.XPATH, "//button[@id='button_id']")  # Replace 'button_id' with the ID of the button
button.click()

#sleep for 5 seconds
sleep(5)

# Close the browser window when done
browser.quit()
