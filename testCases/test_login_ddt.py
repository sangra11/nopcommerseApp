import time

import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilites.readProperties import ReadConfig
from utilites.customLogger import LogGen
from utilites import XLUtils


class Test_002_DDT_Login:
    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/Login_Data.xlsx"


    logger=LogGen.loggen()




    def test_login_ddt(self,setup):
            self.logger.info("************Test_002_DDT_Login**************")
            self.logger.info("************Verifying Login DDT test**********")

            self.driver = setup
            self.driver.get(self.baseURL)
            self.lp=LoginPage(self.driver)

            self.rows=XLUtils.getRowCount(self.path,'Sheet1')
            print("number of Rows in Excel:",self.rows)

            lst_status=[]  #empty list variable

            for r in range(2,self.rows+1):
                self.user=XLUtils.readData(self.path,'Sheet1',r,1)
                self.password=XLUtils.readData(self.path,'sheet1',r,2)
                self.exp=XLUtils.readData(self.path,'sheet1',r,3)

                self.lp.setUserName(self.user)
                self.lp.setpassword(self.password)
                self.lp.clickLogin()
                time.sleep(5)

                act_title=self.driver.title
                exp_title = "Dashboard / nopCommerce administration"

                if act_title==exp_title:
                    if self.exp=='Pass':
                        self.logger.info("******Passed******")
                        self.lp.clickLogout();
                        lst_status.append("Pass")
                    elif self.exp=="Fail":
                        self.logger.info("******Failed****")
                        self.lp.clickLogout();
                        lst_status.append("Fail")
                    elif act_title !=exp_title:
                        if self.exp == 'Pass':
                            self.logger.info("******Failed******")
                            lst_status.append("Failed")
                        elif self.exp == "Fail":
                            self.logger.info("******Passed****")
                            lst_status.append("Pass")

                if "Fail" not in lst_status:
                    self.logger.info("******Login DDT test Passed****")
                    self.driver.close()
                    assert True
                else:
                    self.logger.info("******Log DDT test failed******")
                    self.driver.close()
                    assert False

                self.logger.info("******End of Login DDT Test*******")
                self.logger.info("******Completed Tc_LoginDDT_002*******")







