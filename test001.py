from selenium import webdriver
import time


class TestSelenium():

    def setup(self):
        print("setup".center(40,"-"))

    def test_demo1(self):
        driver = webdriver.Chrome(r"C:\testTools\webdriver\chromedriver.exe")

        driver.get("https://www.baidu.com")

        time.sleep(5)

        driver.close()


if __name__ == '__main__':
    t = TestSelenium()
    t.test_demo1()
