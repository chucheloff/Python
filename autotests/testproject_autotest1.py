# from selenium import webdriver  <-- replace this import
from src.testproject.sdk.drivers import webdriver

def test_create_a_chrome_driver_instance():
    driver = webdriver.Chrome()
    # Your test code goes here
    driver.quit()
