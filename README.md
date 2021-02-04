# testAutomation_mobile

**Prerequisites**

- Python3
- PyCharm
- Selenium
- Appium server and Appium desktop tool
- Android Studio
- Java

**Test Environment**

- Tested on : Android Platform via emulator
- Sample Application used for the test : WordPress

**Framework**

- Page Object Model with Pytest

**Framework folder structure**

- _Pages :_ This contains the elements of all the pages. Each class file will contain only corresponding page elements and actions.
- _Actions:_ This has the functions which are frequently used. E.g. Login action , Logout action
- _Tests :_ Tests folder contains the actual tests.
- _Utils:_ This contains Page utils file , Excel utils file , log file
- _Reports :_ This is to store the generated reports.
- _Test data:_ This contains the test data needed for test cases.
- _Conftest.py :_ This file contains the setup and teardown functions
- _Pytest.ini:_ This contains user defined pytest markers like regression, sanity and smoke

**Test Cases details**

- _test\_01blogstats.py:_ This test case is to verify if the posts count displayed in the Stats page is correct and is matching with the Blogs page
- _test\_02blogtitle\_webview.py_: This test case is to verify if the blog web view displays the correct blog title when it is updated from the app
- _test\_03editname.py:_ This text case is to verify the edit function of the display name under my profile page
- _test\_04login\_scenarios.py_: This test case is to verify the valid and invalid login scenarios
- _test\_05postBlog.py:_ This test case is to verify the publish posts function

**Running Test Suites**

- Start Appium Server and start the device from emulator.
- Install the WordPress app
- Open the terminal and run the below commands

1. To run a single test case from terminal:

_pytest tests/test\_01blogstats.py_

1. To run any specific test cases based on markers

_pytest -m &quot;regression&quot; –html=reports/report.html tests_

_pytest -m &quot;sanity&quot; –html=reports/report.html tests_

_pytest -m &quot;smoke&quot; –html=reports/report.html tests_
