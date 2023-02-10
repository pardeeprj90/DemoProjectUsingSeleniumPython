import time

import pytest

from Pages.LoginPage import Login
from TestCases.Base import BaseClass
from Utilities.CommonMethods import CommonMethods
from Utilities.Logs import Log


@pytest.mark.order(2)
@pytest.mark.parametrize('testData',
                         (CommonMethods.fetchTestDataRowWise('Login', 2, 1, r"./TestData/TestData.xlsx")))
class TestValidateCreateAccount(BaseClass):
    def test_createAccount(self, testData):

        _log = Log.logger()
        _log.info("Execution of Test case User Login started")
        _login = Login(self.driver)
        _login.login(testData[0], testData[1])
        _log.info(f"User {testData[0]} logged in successfully")

        _log.info("Execution of Test case User Login Successfuly completed")
