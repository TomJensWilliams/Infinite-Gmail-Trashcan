from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select 
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException



driver = webdriver.Firefox()
driver.get("http://www.gmail.com")
driver.maximize_window()

def try_wait(input):
    try:
        WebDriverWait(driver, 3).until(EC.presence_of_element_located(input))
    except TimeoutException:
        print ("Loading took too much time!")

def create_user(user_json_data) :

    driver.find_element(By.XPATH, '//span[text()="Create account"]').click()
    driver.find_element(By.XPATH, '//span[text()="For my personal use"]').click()

    driver.find_element(By.NAME, "firstName").send_keys(user_json_data["first_name"])
    driver.find_element(By.NAME, "lastName").send_keys(user_json_data["last_name"])
    driver.find_element(By.XPATH, '//span[text()="Next"]').click()

    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, f'#month'))).click()
    except:
        print("Took to long to find month")
    try:
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, f'#month.option:nth-child({user_json_data["month"]})'))).click()
    except:
        print("Took to long to find particular month")

tom_williams = {"first_name": "Tom", "last_name": "Williams", "month": 2, "day": 3, "year": 4, "gender": 2}
create_user(tom_williams)

"""
assert "Python" in driver.title
elem = driver.find_element(By.NAME, "q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
assert "No results found." not in driver.page_source
"""

# driver.close()