import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Utilities.CommonMethods import CommonMethods


class SignUp:
    def __init__(self, driver):
        self.driver = driver

    def clickSignUplink(self):
        _signup_link = CommonMethods.getWebElement(self, 'SignUpPage', 'signUpLink')
        _signup_link.click()

    def printBrokenLink(self):
        CommonMethods.findBrokenLinks(self)

    def enterName(self, _userName):
        name = CommonMethods.getWebElement(self, 'SignUpPage', 'name')
        name.send_keys(_userName)

    def enterEmail(self, _userEmail):
        name = CommonMethods.getWebElement(self, 'SignUpPage', 'email')
        name.send_keys(_userEmail)

    def enterPassword(self, _userPassword):
        name = CommonMethods.getWebElement(self, 'SignUpPage', 'password')
        name.send_keys(_userPassword)

    def chooseInterest(self, listOfInterest):
        interests = listOfInterest.split(',')
        # print(type(interests))
        for interest in interests:
            # print(interest)
            xpath1 = "//label[@class='interest' and contains(text(),'"
            xpath2 = interest
            xpath3 = "')]/preceding-sibling::input"
            xpath = xpath1 + xpath2 + xpath3
            # print(xpath)
            self.driver.find_element(By.XPATH, xpath).click()

    def chooseGender(self, Male_Or_Female):
        x1 = "//input[@value='"
        x2 = Male_Or_Female
        x3 = "']"
        xpath = x1 + x2 + x3
        # time.sleep(2)
        gender = self.driver.find_element(By.XPATH, xpath)
        CommonMethods.scroll_page(self)
        CommonMethods.clickUsingScript(self, gender)

    def selectState(self, stateName):
        state_drop_down = CommonMethods.getWebElement(self, 'SignUpPage', 'state')
        select = Select(state_drop_down)
        select.select_by_visible_text(stateName)

    def clickSignUpBtn(self):
        _signUpBtn = CommonMethods.getWebElement(self, 'SignUpPage', 'signUpBtn')
        CommonMethods.scrollToElement(self,_signUpBtn)
        CommonMethods.clickUsingScript(self, _signUpBtn)
        # _signUpBtn.click()

    def validateSignUp(self, expectedValidationText):

        url = self.driver.current_url
        if expectedValidationText in url:
            assert True
        else:
            print(url)
            CommonMethods.captureScreenshot(self, 'SignUpPage')
            assert False
