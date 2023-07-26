import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen


class Test_001_Login:
    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUseremail()
    password=ReadConfig.getPassword()

    logger=LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression

    def test_homepageTitle(self,setup):

        self.logger.info("************Test_001_Login**********")
        self.logger.info("************Verifying Home Page Title***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title

        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("************Home page title is passd ***********")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("************Home page title is Failed ***********")
            assert False


    @pytest.mark.regression
    def test_login(self,setup):
            self.logger.info("************Verifying Login test**********")

            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp=LoginPage(self.driver)
            self.lp.setUserName(self.username)
            self.lp.setpassword(self.password)
            self.lp.clickLogin()
            act_title=self.driver.title

            if act_title == "Dashboard / nopCommerce administration":
                assert True
            else:
                self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
                self.driver.close()
                self.logger.error("************Login Test is Failed**********")
                assert False
