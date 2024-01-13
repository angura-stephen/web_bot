from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep



def relax():
    sleep(0)

def restart_mifi():
    """
    Simply goes through the tedious process of restarting a MIFI when there are internet issues
    """
    # Initialize a web browser (in this case, Chrome)
    browser = webdriver.Chrome()

    # URL to open
    url = "http://jazz.wifi/index.html#home"  # Replace with the URL you want to visit

    print("accessing MIFI control panel")
    # Open the URL
    browser.get(url)

    # Wait for the page to load completely (adjust the timeout as needed)
    wait = WebDriverWait(browser, 10)  # Timeout of 10 seconds
    #element = wait.until(EC.presence_of_element_located((By.ID, "element_id")))  # Replace 'element_id' with the ID of the element you want to interact with
    print("MIFI control panel accessed successfully")
    print("Attempting to restart")

    try:
        wait.until(EC.presence_of_element_located(("xpath","//a[@href='#setting']"))).click()
        relax()
        try:
            input_element = wait.until(EC.presence_of_element_located((By.ID,"txtPwd")))
            # Input text into the input element
            input_element.send_keys("1245")
            # Press Enter key
            input_element.send_keys(Keys.ENTER)
            relax()
        except:
            pass

        wait.until(EC.presence_of_element_located(("xpath","//a[@href='#setting']"))).click()
        wait.until(EC.presence_of_element_located(("xpath","//a[@href='#device_setting']"))).click()
        wait.until(EC.element_to_be_clickable(("xpath","//a[@href='#restart']"))).click()
        sleep(0.1)
        wait.until(EC.element_to_be_clickable(("xpath", "//input[@type='submit']"))).click()
        wait.until(EC.presence_of_element_located((By.ID,"nobtn"))).click()

        # Close the browser window when done
        browser.quit()
        print("MIFI restart successful")
        print("webpage successfully closed")
    except Exception as e:
        print("AN ERROR OCCURRED")
        print(e)


