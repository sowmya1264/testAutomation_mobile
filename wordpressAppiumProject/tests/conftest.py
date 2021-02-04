import pytest
from appium import webdriver


@pytest.fixture()
def setup(request):
    request.instance.driver = webdriver.Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                                               desired_capabilities=
                                               {
                                                   "platformName": "Android",
                                                   "platformVersion": "11.0",
                                                   "deviceName": "myandroid",
                                                   "automationName": "uiautomator2",
                                                   "app": "/Users/sowmya/Desktop/apps/wordpress-16-4.apk",
                                                   "appPackage": "org.wordpress.android",
                                                   "appActivity": "org.wordpress.android.ui.WPLaunchActivity",
                                                   "noReset": False

                                               }
                                               )

    return request.instance.driver

    def teardown():
        request.instance.driver.quit()

    request.addfinalizer(teardown)
