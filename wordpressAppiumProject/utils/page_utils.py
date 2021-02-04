from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class PageUtils:

    def __init__(self, driver):
        self.driver = driver

    def wait_element_click(self, locator, locator_value):
        try:
            if locator == 'id':
                element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, locator_value)))
                element.click()

            elif locator == 'css selector':
                element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator_value)))
                element.click()

            elif locator == 'xpath':
                element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.XPATH, locator_value)))
                element.click()

            elif locator == 'link text':
                element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.LINK_TEXT, locator_value)))
                element.click()


        except NoSuchElementException:
            print("No element found")

    def wait_elements_click(self, locator, locator_value):
        try:
            if locator == 'id':
                elements = WebDriverWait(self.driver, 50).until(
                    EC.presence_of_all_elements_located((By.ID, locator_value)))
                ele_values = []
                for i in elements:
                    ele_values.append(i.text)
                return ele_values

        except NoSuchElementException:
            print("No element found")

    def wait_element_sendtext(self, locator, locator_value, text_value):
        try:
            if locator == 'id':
                element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, locator_value)))
                element.send_keys(text_value)

            elif locator == 'css selector':
                element = WebDriverWait(self.driver, 50).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, locator_value)))
                element.send_keys(text_value)

            elif locator == 'xpath':
                element = WebDriverWait(self.driver, 50).until(
                    EC.element_to_be_clickable((By.XPATH, locator_value)))
                element.send_keys(text_value)



        except NoSuchElementException:
            print("No element found")

    def wait_element_gettext(self, locator, locator_value):
        try:
            if locator == 'id':
                element = WebDriverWait(self.driver, 50).until(EC.presence_of_element_located((By.ID, locator_value)))
                return element.text

            elif locator == 'css selector':
                element = WebDriverWait(self.driver, 50).until(
                    EC.presence_of_element_located((By.CSS_SELECTOR, locator_value)))
                return element.text

            elif locator == 'xpath':
                element = WebDriverWait(self.driver, 50).until(
                    EC.presence_of_element_located((By.XPATH, locator_value)))
                return element.text

            elif locator == 'class name':
                element = WebDriverWait(self.driver, 50).until(
                    EC.presence_of_element_located((By.CLASS_NAME, locator_value)))
                return element.text

        except NoSuchElementException:
            print("No element found")

    def wait_element_isdisplayed(self, locator, locator_value):
        try:
            if locator == 'id':
                try:
                    element_displayed = WebDriverWait(self.driver, 50).until(
                        EC.element_to_be_clickable((By.ID, locator_value)))
                    return element_displayed.is_displayed()
                except:
                    return False
        except NoSuchElementException:
            print("No element found")

    def wait_element_clear(self, locator, locator_value):
        try:
            if locator == 'id':
                element = WebDriverWait(self.driver, 50).until(EC.element_to_be_clickable((By.ID, locator_value)))
                element.clear()

        except NoSuchElementException:
            print("No element found")
