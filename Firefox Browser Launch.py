from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get("https://auth.hollandandbarrett.com/u/login")
driver.maximize_window()
time.sleep(8)

actual_title = driver.title
expect_title = "Sign in - to your account, for the best experience"

if actual_title == expect_title:
    print("Login is Successful ...... Well done Python")
else:
    print("Login UnSuccessful  ...... Very good my boy!")