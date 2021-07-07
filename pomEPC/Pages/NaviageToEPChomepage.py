class NavigateToEPChomepage():

    def __init__(self, driver):
        self.driver = driver
        self.ClicktoNavigateEPChomepage_button_xpath ="//*[@id='projectpagebody']/div[1]/div/div[3]/h3/ecoreach-logo/a/img"

    def navigatetoEPChomepage(self):
        self.driver.find_element_by_xpath(self.ClicktoNavigateEPChomepage_button_xpath).click()