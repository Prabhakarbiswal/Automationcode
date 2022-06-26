from selenium import webdriver
import pytest
from pages.loginpage import LoginPage
from pages.homepage import HomePage
class TestLogin():
    @pytest.fixture(scope="class")
    def test_setup(self):
        global driver
        driver = webdriver.Chrome(executable_path="C://Users//mepra//PycharmProjects//Automation end to end//drivers//chromedriver.exe")
        driver.implicitly_wait(5)
        driver.maximize_window()

        yield
        driver.close()
        driver.quit()
        print("Test Completed")

    def test_login(self, test_setup):
        driver.get("https://opensource-demo.orangehrmlive.com/")
        login = LoginPage(driver)
        login.enter_username("Admin")
        login.enter_password("admin123")
        login.click_login()
       # driver.find_element_by_id("txtUsername").send_keys("Admin")
       # driver.find_element_by_id("txtPassword").send_keys("admin123")
       # driver.find_element_by_id("btnLogin").click()

    def test_logout(self, test_setup):
        homepage = HomePage(driver)
        homepage.click_welcome()
        homepage.click_logout()
       # driver.find_element_by_id("welcome").click()
      #  driver.find_element_by_link_text("Logout").click()
