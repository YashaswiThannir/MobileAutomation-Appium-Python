from appium import webdriver
import pytest
from time import sleep


class TestScroll():

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

    def test_scroll(self):
        el = self.driver.find_element_by_accessibility_id('Settings Row')
        self.driver.execute_script('mobile: scroll', {"element": el, "toVisible": True})
        el.click()
        assert self.driver.find_element_by_accessibility_id('your_blog_name').text == 'your_blog_name'