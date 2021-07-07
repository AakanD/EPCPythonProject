class EpcHomePage():

    def __init__(self, driver):
        self.driver = driver
        self.createproject_button_xpath = "//*[@id='child-btn']"
        self.clickcloseprojectinformation_button_xpath="//*[@id='projectSlider']/div/div/img"

    def CreateNewProject(self):
        self.driver.find_element_by_xpath(self.createproject_button_xpath).click()

    def ClickCloseSiteDetails(self):
        self.driver.find_element_by_xpath(self.clickcloseprojectinformation_button_xpath).click()

