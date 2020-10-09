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
  'build':'My Second Build',
  'name' : 'Bstack-[Python] Sample Test',
  'app':'bs://4eb72b1848c085541c3d00febc193fae29e56bb6'
}
driver = webdriver.Remote("https://" + userName + ":" + accessKey + "@hub-cloud.browserstack.com/wd/hub", desired_cap)

text_button = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Button"))
)
text_button.click()

text_input = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Input"))
)
text_input.send_keys("hello@browserstack.com\n")

time.sleep(5)

text_output = WebDriverWait(driver, 30).until(
    EC.element_to_be_clickable((MobileBy.ACCESSIBILITY_ID, "Text Output"))
)

if text_output!=None and text_output.text=="hello@browserstack.com":
  assert True
else:
  assert False

driver.quit()