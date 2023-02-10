from selenium.webdriver.common.keys import Keys

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

from Utilities.CommonMethods import CommonMethods


class AddNewCourse:
    def __init__(self, driver):
        self.driver = driver

    def clickManageCourse(self):
        element = CommonMethods.getWebElement(self, 'AddCourse', 'manageBtn')
        actions = ActionChains(self.driver)
        actions.move_to_element(element).perform()
        element1 = CommonMethods.getWebElement(self, 'AddCourse', 'manageCourses')
        actions.move_to_element(element1).click(element1).perform()
        body = self.driver.find_element(By.XPATH, "//th[contains(.,'Course Name')]")
        body.click()

    def clickAddNewCourseBtn(self):
        add_newCourseBtn = CommonMethods.getWebElement(self, 'AddCourse', 'addNewCourseBtn')
        add_newCourseBtn.click()

    def uploadFile(self, baseFileDir, fileNameWithType):
        uploadFileBtn = CommonMethods.getWebElement(self, 'AddCourse', 'chooseFileBtn')
        file_path = CommonMethods.fileUpload(baseFileDir, fileNameWithType)
        uploadFileBtn.send_keys(file_path)

    def enterCourseName(self, nameOfCourse):
        elem = CommonMethods.getWebElement(self, 'AddCourse', 'courseName')
        elem.send_keys(nameOfCourse)

    def enterCourseDescription(self, courseDescription):
        elem = CommonMethods.getWebElement(self, 'AddCourse', 'description')
        elem.send_keys(courseDescription)

    def selectInstructor(self, instructorName):
        elem = CommonMethods.getWebElement(self, 'AddCourse', 'instructor_input')
        elem.send_keys(instructorName)
        elem_ = CommonMethods.getWebElement(self, 'AddCourse', 'instructor_list')
        elem_.click()

    def enterPrice(self, price):
        elem = CommonMethods.getWebElement(self, 'AddCourse', 'price')
        elem.send_keys(price)

    def enterStartDate(self, startDate):
        date = CommonMethods.dateFormatter(startDate)
        elem = CommonMethods.getWebElement(self, 'AddCourse', 'startDate')
        elem.send_keys(Keys.END)
        elem.send_keys(Keys.BACKSPACE)
        elem.send_keys(date)
        elem.send_keys(Keys.ENTER)

    def enterEndDate(self, endDate):
        date = CommonMethods.dateFormatter(endDate)
        elem = CommonMethods.getWebElement(self, 'AddCourse', 'endDate')
        elem.send_keys(Keys.END)
        elem.send_keys(Keys.BACKSPACE)

        elem.send_keys(date)
        elem.send_keys(Keys.ENTER)


    def selectCategory(self, categoryName):
        CommonMethods.scroll_page(self)
        elem = CommonMethods.getWebElement(self, 'AddCourse', 'selectCategory')
        elem.click()
        x = "// button[contains(text(), '"
        x1 = categoryName
        x2 = "')]"
        elem_ = self.driver.find_element(By.XPATH, x + x1 + x2)
        CommonMethods.scrollToElement(self, elem_)
        elem_.click()

    def clickSaveBtn(self):
        elem = CommonMethods.getWebElement(self, 'AddCourse', 'saveBtn')
        elem.click()

    def validateCourseAddition(self, expectedCourseName):
        elem = self.driver.find_elements(By.XPATH,
                                         "//td[contains(text(),'" + expectedCourseName + "')]")
        if len(elem) >= 1:
            print(f"{expectedCourseName} course exists {len(elem)} times in course grid")
            assert True
        else:
            print(f"{expectedCourseName} course doesn't exists")
            CommonMethods.captureScreenshot('AddCourse')
            assert False
