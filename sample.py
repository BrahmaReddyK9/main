import time

#author name- sharad Tiwari

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()

#driver = webdriver.Firefox()
#driver = webdriver.Ie(executable_path=r"C:\Users\Sharad\Desktop\drivers\IEDriverServer.exe")
driver.get("https://www.amazon.com/")
print(driver.title)
driver.find_element_by_xpath("//*[@id='nav-link-accountList']/div").click()
time.sleep(5)
driver.close()    #currently focused browser
#driver.quit()     #closes all the browser
