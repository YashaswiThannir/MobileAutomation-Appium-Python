from appium import webdriver
import pytest
from time import sleep


class TestScroll():

    def setup(self):
        self.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                       desired_capabilities=
                                       {
                                           "platformName": "Android",
                                           "platformVersion": "9",
                                           "deviceName": "android",
                                           "automationName": "uiautomator2",
                                           "app": "/Users/akvenk/Desktop/and/wordpress.apk",
                                           "appPackage": "org.wordpress.android",
                                           "appActivity": "org.wordpress.android.ui.WPLaunchActivity",
                                           "noReset": True,
                                       })

    def teardown(self):
        self.driver.quit()

    def test_scroll(self):
        sleep(3)
        for _ in range(15):
            print(_)
            end_y = 800
            try:
                value = self.driver.find_element_by_id("row_settings").is_displayed()
                if value is True:
                    break
            except:
                self.driver.swipe(470, 1460, 470, end_y, 300)
                self.driver.implicitly_wait(2)
                continue
        sleep(3)
        self.driver.find_element_by_id("row_settings").click()
        sleep(2)
        assert self.driver.find_element_by_xpath('//android.widget.TextView[@text="akmobiletesting"]').text == 'akmobiletesting'



# start x
# start y
# end x
# end y
# duration