import pytest
from selenium import webdriver
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen


class Test001Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUserName()
    password = ReadConfig.getPassword()

    logger = LogGen.Loggen()

    def test_HomePage(self, setup):

        self.logger.info("************ Test001Login *************")
        self.logger.info("**** Started Home page title test ****")
        self.driver = setup
        self.logger.info("**** Opening URL****")
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Your store. Login":
            self.logger.info("**** Home page title test passed ****")
            self.driver.close()
            assert True

        else:
            self.logger.info("************ Home Page Title is Failed *************")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_HomePage.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.logger.info("**** Started Login Test****")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        # self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            self.logger.info("**** Login test passed ****")
            self.driver.close()
            assert True
        else:
            self.logger.error("**** Login test failed ****")
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login.png")
            self.driver.close()
            assert False
