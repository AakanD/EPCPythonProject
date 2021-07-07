import unittest
import HtmlTestRunner
from selenium import webdriver
import time
from pomEPC.Pages.EPCHomePage import EpcHomePage
from pomEPC.Pages.NaviageToEPChomepage import NavigateToEPChomepage

class MyTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.options = webdriver.ChromeOptions()
        cls.options.add_argument('--ignore-ssl-errors=yes')
        cls.options.add_argument('--ignore-certificate-errors')
        cls.options.add_argument("--start-maximized")
        cls.driver = webdriver.Chrome(options=cls.options)
        cls.driver.get("https://127.0.0.1:8084")
        cls.driver.implicitly_wait(15)
        # cls.time = time
        # cls.time.sleep(15)

    def test_clickCreateProjectHomePage(self):
        driver = self.driver
        # self.driver.find_element_by_xpath("//*[@id='child-btn']").click()
        # time.sleep(5)
        # self.driver.find_element_by_xpath("//*[@id='projectSlider']/div/div/img").click()
        # time.sleep(5)
        createNewProject = EpcHomePage(driver)
        createNewProject.CreateNewProject()
        time.sleep(5)
        createNewProject.ClickCloseSiteDetails()
        time.sleep(5)
    # def test_ClickOnEPCtext(self):
    #     # self.driver.find_element_by_xpath("//*[@id='projectpagebody']/div[1]/div/div[3]/h3/ecoreach-logo/a/img").click()
    #     # time.sleep(5)
    #     driver = self.driver
    #     driver.implicitly_wait(5)
        navigateTohomepage = NavigateToEPChomepage(driver)
        navigateTohomepage.navigatetoEPChomepage()
        time.sleep(5)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()


if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='C:/Users/SESA382675/PycharmProjects/my_workspace/EPC/EPCreports'))
