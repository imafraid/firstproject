import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class Test1(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(30)
        self.driver.get(r"https://xyy-test.yiting.cloud/")
        time.sleep(1)

    def test_login(self):
        self.driver.find_element(by=By.ID, value='name').send_keys("114928")
        self.driver.find_element(By.ID, 'password').send_keys("123456")
        yuan = self.driver.find_element(By.ID, 'branch')
        action = ActionChains(self.driver)
        action.click(yuan).perform()
        action.move_by_offset(0, 50).click().perform()
        self.driver.find_element(By.XPATH, '//*[@id="root-master"]/section/div/div/div/button[1]').click()
        login_info = self.driver.find_element(By.XPATH, '//*[@id="root-master"]/section/header/div/div[2]/div[5]').text

        try:
            self.assertIn("退出", login_info)
        except AssertionError as e:
            print("失败")
            self.driver.get_screenshot_as_file("./images/%s.png" % str(time.time()).replace(".", "_"))
            raise
