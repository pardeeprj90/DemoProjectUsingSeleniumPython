"""
Test Script Author:- Pardeep Kumar
Creation Date:- 08 Feb 2023
Last Updated By:-
Last Update Date:-
Revision History:-

Test Case Description:- Validate user should be able to add a course successfully.
Test Steps:-
    1) Launch browser and login the test app.
    2) Navigate to Manage Course and click on Add Course.
    3) upload the image file, enter course name, description, Instructor, Price, State and End date etc.
    4) Click on save button.
    5) Validate course addition in Manage course page.
"""

import pytest

from Pages.AddCoursePage import AddNewCourse
from Pages.LoginPage import Login
from TestCases.Base import BaseClass
from Utilities.CommonMethods import CommonMethods
from Utilities.Logs import Log


@pytest.mark.order(2)
@pytest.mark.parametrize('UserInfo',
                         (CommonMethods.fetchTestDataRowWise('Login', 2, 1, r"./TestData/TestData.xlsx")))
@pytest.mark.parametrize('AddCourseTestData',
                         (CommonMethods.fetchTestDataRowWise('AddCourse', 2, 1, r"./TestData/TestData.xlsx")))
class TestValidateAddCourse(BaseClass):
    def test_createAccount(self, UserInfo, AddCourseTestData):
        _log = Log.logger()
        _log.info("Execution of Test case Add Course started")

        _login = Login(self.driver)
        _log.info("login class object created successfully")

        _login.login(UserInfo[0], UserInfo[1])
        _log.info(f"User {UserInfo[0]} logged in successfully")

        add_course = AddNewCourse(self.driver)
        _log.info("AddNewCourse class object created successfully")

        add_course.clickManageCourse()
        _log.info(f"User clicked on ManageCourse module successfully")

        add_course.clickAddNewCourseBtn()
        _log.info(f"User clicked on Add New Course Button successfully")

        add_course.uploadFile("E:/recruitCRM/TestData/", "sampleTestFile.png")
        _log.info(f"User uploaded image file Successfully")

        add_course.enterCourseName(AddCourseTestData[0])
        _log.info(f"User enters {AddCourseTestData[0]} in Course Name input Field successfully")

        add_course.enterCourseDescription(AddCourseTestData[1])
        _log.info(f"User enters {AddCourseTestData[1]} in Course Description input Field successfully")

        add_course.selectInstructor(AddCourseTestData[2])
        _log.info(f"User enters {AddCourseTestData[2]} in Instructor input Field successfully")

        add_course.enterPrice(AddCourseTestData[3])
        _log.info(f"User enters {AddCourseTestData[3]} in Course Description input Field successfully")

        add_course.enterStartDate(AddCourseTestData[4])
        # print(AddCourseTestData[4])
        _log.info(f"User selected {AddCourseTestData[4]} in Start Date Field successfully")

        add_course.enterEndDate(AddCourseTestData[5])
        _log.info(f"User selected {AddCourseTestData[5]} in End Date Field successfully")

        add_course.selectCategory(AddCourseTestData[6])
        _log.info(f"User selected {AddCourseTestData[6]} Course successfully")

        add_course.clickSaveBtn()
        _log.info(f"User clicked Saved successfully")

        add_course.validateCourseAddition(AddCourseTestData[0])
        _log.info(f"Course {AddCourseTestData[0]} addition validated successfully")

        _log.info(f" Test Case Add Course executed Successfully")
