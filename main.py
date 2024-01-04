import time
from selenium import webdriver
from selenium.webdriver.edge.options import Options
import Functions

try:
    Functions.getInputData()
    o = Options()
    o.add_experimental_option("detach", True)
    driver = webdriver.Edge(options=o)
    url = "https://thermofisher-asg.atlassian.net/servicedesk/customer/portal/2/group/25/create/89"

    if Functions.pageLoad(driver, url):
        Functions.autoFillingFields(driver)
    else:
        print("Check your internet connection")

except Exception as ex:
    print(ex)
#finally:
    #driver.close()
    #driver.quit()
