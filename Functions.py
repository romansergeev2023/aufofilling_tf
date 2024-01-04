from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from os import system, name
import AccessToFields
import InputData
import re

regexEmail = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@thermofisher.com')


def pageLoad(driver, url):
    driver.maximize_window()
    driver.get(url)
    try:
        ele = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, AccessToFields.XPATH.logoTF)))
        return True
    except:
        print("Timeout Exception: Page did not load within 10 seconds.")
        return False


def fillingTextFields(wait, xpath, data):
    textField = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    textField.send_keys(data)


def fillingDropDownMenu(wait, xpath, data):
    dropDownMenu = wait.until(EC.presence_of_element_located((By.XPATH, xpath)))
    dropDownMenu.click()
    chooseFromDropDownMenu = wait.until(EC.presence_of_element_located((By.XPATH, data)))
    chooseFromDropDownMenu.click()


def autoFillingFields(driver):
    wait = WebDriverWait(driver, 5)

    fillingTextFields(wait, AccessToFields.XPATH.email, InputData.Data.email)
    fillingDropDownMenu(wait, AccessToFields.XPATH.group, AccessToFields.XPATH.dropMenuGroup)
    fillingTextFields(wait, AccessToFields.XPATH.connectionRequest, InputData.Data.connectionRequest)
    fillingTextFields(wait, AccessToFields.XPATH.describe, InputData.Data.describe)
    fillingDropDownMenu(wait, AccessToFields.XPATH.entitlementType, AccessToFields.XPATH.dropMenuEntitlementType)
    fillingDropDownMenu(wait, AccessToFields.XPATH.customerType, AccessToFields.XPATH.dropMenuCustomerType)
    fillingDropDownMenu(wait, AccessToFields.XPATH.isSystemNew, AccessToFields.XPATH.dropMenuIsSystemNew)
    fillingDropDownMenu(wait, AccessToFields.XPATH.region, AccessToFields.XPATH.dropMenuRegion)
    fillingDropDownMenu(wait, AccessToFields.XPATH.customer, AccessToFields.XPATH.dropMenuCustomer)
    fillingDropDownMenu(wait, AccessToFields.XPATH.fleet, AccessToFields.XPATH.dropMenuFleet)
    fillingDropDownMenu(wait, AccessToFields.XPATH.systemType, AccessToFields.XPATH.dropMenuSystemType)
    fillingTextFields(wait, AccessToFields.XPATH.systemModel, InputData.Data.systemModel)
    fillingDropDownMenu(wait, AccessToFields.XPATH.nameCSM, AccessToFields.XPATH.dropMenuCSM)
    fillingDropDownMenu(wait, AccessToFields.XPATH.nameDSE, AccessToFields.XPATH.dropMenuDSE)


def clear():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')


def isValidEmail(email):
    if re.fullmatch(regexEmail, email):
        print("Valid email\n")
        return True
    else:
        print("Invalid email")
        return False


def getInputEmail():
    while True:
        print("Enter your email: ")
        email = input()
        if isValidEmail(email):
            InputData.Data.email = email
            clear()
            break


def getInputSN():
    while True:
        print("Do not fill the 99 serial number at this point!\nUse CRM Slot Number!\nEnter SN of system:")
        serialNum = input()
        if serialNum.isalnum():
            InputData.Data.systemSN = serialNum
            clear()
            break


def getInputPN():
    while True:
        print("Enter PN of system: ")
        partNum = input()
        if partNum.isalnum():
            InputData.Data.systemPN = partNum
            clear()
            break


def getInputSystemType():
    print("Choose your system from the list:\n1.Glacios\n2.Talos\n3.Talos Arctica\n4.Titan Krios\n5.Metrios\n6.Tundra")
    while True:
        print("Your system: ")
        systemType = input()
        if systemType.isdigit():
            match systemType:
                case "1":
                    AccessToFields.XPATH.inputSystemType = systemType
                case "2":
                    AccessToFields.XPATH.inputSystemType = systemType
                case "3":
                    AccessToFields.XPATH.inputSystemType = systemType
                case "4":
                    AccessToFields.XPATH.inputSystemType = systemType
                case "5":
                    AccessToFields.XPATH.inputSystemType = systemType
                case "6":
                    AccessToFields.XPATH.inputSystemType = systemType
                case _:
                    print("Incorrect input")
                    continue
            clear()
            break


def getInputData():
    getInputSystemType()
    getInputSN()
    getInputPN()
    getInputEmail()
