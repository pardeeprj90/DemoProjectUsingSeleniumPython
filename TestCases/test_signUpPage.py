"""
Test Script Author:- Pardeep Kumar
Creation Date:- 09 Feb 2023
Last Updated By:-
Last Update Date:-
Revision History:-

Test Case Description:- Validate user should be able to Sign Up successfully.
Test Steps:-
    1) Launch browser and click on Sign Up link.
    2) Enter Name, Email and Password.
    3) Select Interest checkbox.
    4) Choose gender.
    5) Select state and click on Sign Up button.
    6) Validate Sign up success.
"""
import time

import pytest

from Pages.SignUpPage import SignUp
from TestCases.Base import BaseClass
from Utilities.CommonMethods import CommonMethods
from Utilities.Logs import Log


@pytest.mark.order(1)
@pytest.mark.parametrize('testData',
                         (CommonMethods.fetchTestDataRowWise('SignUpPage', 2, 1, r"./TestData/TestData.xlsx")))
class TestValidateSignUp(BaseClass):
    def test_signUp(self, testData):
        _log = Log.logger()
        _log.info("Execution of Test case User Sign Up started")
        # print(testData)
        signup = SignUp(self.driver)
        _log.info("SignUp class object created successfully")

        signup.clickSignUplink()
        _log.info("SignUp link clicked successfully")

        signup.enterName(testData[0])
        _log.info(f"User entered {testData[0]} in Name input field")

        signup.enterEmail(testData[1])
        _log.info(f"User entered {testData[1]} in Email input field")

        signup.enterPassword(testData[2])
        _log.info(f"User entered {testData[2]} in Password input field")

        signup.chooseInterest(testData[3])
        _log.info(f"User Chosed {testData[3]} in Interest successfully")

        signup.chooseGender(testData[4])
        _log.info(f"User Chosed {testData[4]} in Gender successfully")

        signup.selectState(testData[5])
        _log.info(f"User selected {testData[5]} state successfully")

        signup.clickSignUpBtn()
        _log.info(f"User clicked sign up button successfully")
        time.sleep(5)

        signup.validateSignUp('login')
        _log.info(f"Sign up validated successfully")
        _log.info(f"Test case Sign up executed successfully")

