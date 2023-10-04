from selenium import webdriver
from selenium.webdriver.common.by import By
import time

email="qa.rakamin.jubelio@gmail.com"
password="jubelio123!"

url="https://app.jubelio.com/login"


driver = webdriver.Chrome()
driver.get(url)


driver.find_element(By.XPATH, "//input[@name='email']").send_keys('qa.rakamin.jubelio@gmail.com')
driver.find_element(By.XPATH, "//input[@name='password']").send_keys('Jubelio123!')

driver.find_element(By.XPATH, "//button[@type='submit']").click()
print("Logged In Successfully")
time.sleep(5)
driver.save_screenshot("C:\\Users\\dsugi\\Downloads\\JubelioSelenium\\test.png")
driver.quit()

