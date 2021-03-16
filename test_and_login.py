from appium import webdriver
import pytest
from time import sleep


class TestAndLogin():

    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=
                                       {
                                           "platformName": "Android",
                                           "platformVersion": "9",
                                           "deviceName": "android",
                                           "automationName": "uiautomator2",
                                           "app": "/Users/username/Desktop/and/wordpress.apk",
                                           "appPackage": "org.wordpress.android",
                                           "appActivity": "org.wordpress.android.ui.WPLaunchActivity",
                                           "noReset": True,
                                       })

    def teardown(self):
        self.driver.quit()

    def test_and_login(self):
        self.driver.find_element_by_id('login_button').click()
        sleep(2)
        self.driver.find_element_by_id('input').send_keys('your_email')
        sleep(2)
        self.driver.find_element_by_id('primary_button').click()
        sleep(10)
        self.driver.find_element_by_id('login_enter_password').click()
        sleep(4)
        self.driver.find_element_by_id('input').send_keys('your_password')
        sleep(2)
        self.driver.find_element_by_id('primary_button').click()
        sleep(15)
        self.driver.find_element_by_id('primary_button').click()
        sleep(2)
        assert self.driver.find_element_by_id('my_site_title_label').text == 'your_blog_name'
