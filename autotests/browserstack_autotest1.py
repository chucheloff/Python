from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

userName = "chuchelov1"
accessKey = "pwg6H9cTDVMJ6RvSwjjp"
desired_cap = {
  'device': 'iPhone 11 Pro',
  'os_version': '13',
  'project' : 'My First Project',
  'build':'My First Build',
  'name' : 'Bstack-[Python] Sample Test',
  'app':'bs://4eb72b1848c085541c3d00febc193fae29e56bb6'
}

driver = webdriver.Remote("http://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_cap)



driver.quit()