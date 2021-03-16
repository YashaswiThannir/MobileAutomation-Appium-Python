from appium import webdriver
import pytest
from time import sleep


class TestLogin():

    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities={
                                           "platformName": "iOS",
                                           "platformVersion": "13.5",
                                           "deviceName": "iPhone 11 Pro MT",
                                           "automationName": "XCUITest",
                                           "app": "/Users/username/Library/Developer/Xcode/DerivedData/WordPress-bgxbidnfcsphaffyuskxfnuixlek/Build/Products/Debug-iphonesimulator/WordPress.app",
                                           "noReset": True,
                                           "autoAcceptAlerts": False
                                       })

    def teardown(self):
        self.driver.quit()
    
    def test_login(self):
        self.driver.find_element_by_accessibility_id('Prologue Log In Button').click()
        sleep(2)
        self.driver.find_element_by_accessibility_id('Log in with Email Button').click()
        sleep(2)
        self.driver.find_element_by_accessibility_id('Login Email Address').send_keys('your_email')
        sleep(2)
        self.driver.find_element_by_accessibility_id('Login Email Next Button').click()
        sleep(2)
        self.driver.find_element_by_accessibility_id('Enter your password instead.').click()
        sleep(2)
        self.driver.find_element_by_accessibility_id('Password').send_keys('your_password')
        sleep(2)
        self.driver.find_element_by_accessibility_id('Password Next Button').click()
        sleep(5)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Done"]').click()
        sleep(2)
        assert self.driver.find_element_by_xpath('(//XCUIElementTypeStaticText[@name="your_blog_name"])[1]').text == 'your_blog_name'

    def test_logout(self):
        self.driver.find_element_by_accessibility_id('meBarButton').click()
        sleep(1)
        self.driver.find_element_by_accessibility_id('Log Out').click()
        sleep(2)
        self.driver.find_element_by_xpath('//XCUIElementTypeButton[@name="Log Out"]').click()  # popup logout
        sleep(3)
        assert self.driver.find_element_by_accessibility_id('Log In').text == 'Log In'
