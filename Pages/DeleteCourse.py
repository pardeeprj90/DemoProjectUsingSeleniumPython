"""
Test Script Author:- Pardeep Kumar
Creation Date:- 1o Feb 2023
Last Updated By:-
Last Update Date:-
Revision History:-

Test Case Description:- Validate user should be able to add a course successfully.
Test Steps:-
    1) Launch browser and login the test app.
    2) Navigate to Manage Course.
    3) click on Delete button.
    4) Validate course count.
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class DeleteCourse:
    def __init__(self, driver):
        self.driver = driver

    def deleteCourse(self):
        wait = WebDriverWait(self.driver, 15)

        rows = self.driver.find_elements(By.XPATH, '//tr')
        row_count = len(rows)
        istRow = self.driver.find_element(By.XPATH, "(//button[contains(.,'Delete')])[1]")
        istRow.click()
        rowsAfterDeletion = wait.until(ec.presence_of_all_elements_located(self.driver.find_elements(By.XPATH, '//tr')))
        rowCountAfterDelete = len(rowsAfterDeletion)
        if row_count > rowCountAfterDelete:
            assert True
        else:
            assert False
