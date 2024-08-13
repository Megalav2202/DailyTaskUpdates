import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

serviceobj=Service("C:/bin/chromedriver-win64/chromedriver-win64/chromedriver.exe")
driver = webdriver.Chrome(service=serviceobj)

driver.maximize_window()
driver.implicitly_wait(5)



def negativeflows():
        driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index")
        driver.find_element(By.NAME,"username").send_keys("admin")
        driver.find_element(By.NAME,"password").send_keys("Admin123")
        driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        time.sleep(2)
        try:
            error_message = driver.find_element(By.XPATH, "//p[@class='oxd-text oxd-text--p oxd-alert-content-text']")
            assert "Invalid credentials" in error_message.text
            print("Negative test case passed: Error message displayed as expected.")
        except AssertionError:
            print("Negative test case failed: Error message did not appear or was incorrect.")


def positiveflows():
        driver.find_element(By.NAME,"username").send_keys("Admin")
        driver.find_element(By.NAME,"password").send_keys("admin123")
        driver.find_element(By.XPATH,"//button[normalize-space()='Login']").click()
        time.sleep(2)
        try:
            dashboard_element = driver.find_element(By.XPATH, "//div[@class='oxd-topbar-header-title']")
            assert "Dashboard" in dashboard_element.text
            print("Positive test case passed: Successfully logged in.")
        except AssertionError:
            print("Positive test case failed: Login was not successful.")

negativeflows()
positiveflows()


driver.quit()