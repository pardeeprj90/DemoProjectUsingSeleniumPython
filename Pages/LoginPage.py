from Utilities.CommonMethods import CommonMethods


class Login:
    def __init__(self, driver):
        self.driver = driver

    def login(self, _userEmailId, _userPassword):
        _eml = CommonMethods.getWebElement(self, 'LoginPage', 'email')
        _eml.click()
        _eml.send_keys(_userEmailId)
        _passWord = CommonMethods.getWebElement(self, 'LoginPage', 'password')
        _passWord.click()
        _passWord.send_keys(_userPassword)
        _button = CommonMethods.getWebElement(self, 'LoginPage', 'signInBtn')
        _button.click()
        # print("Sign In Button Clicked Successfully")
        btn = CommonMethods.getWebElement(self, 'LoginPage', 'signOutBtn')
        btn_text = btn.text
        if btn_text == 'Sign out':
            assert True
        else:
            CommonMethods.captureScreenshot(self, 'Login')
            assert False
