import streamlit as st
import time

from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.firefox import GeckoDriverManager

# URL = "http://github.com"


st.title("Test Selenium")
st.markdown("You should see some random Football match text below in about 21 seconds")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")

firefoxOptions.add_argument("--disable-gpu")


service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)

driver.get(st.secrets["URL"])

time.sleep(3)

# 清除所有cookies
driver.delete_all_cookies()

#添加cookies
time.sleep(2)
for key, value in st.secrets["cookies_dict"].items():
    driver.add_cookie({'name': key, 'value': value})

time.sleep(2)
driver.refresh()

#尝试寻找登录后存在的字符，如果找到则登录成功。
time.sleep(5)
try:
    logininfo = driver.find_element('xpath', '//*[@id="sidebar-section-header-files"]/div/span[1]')    
    print(logininfo.text)
    print("找到 Files，已成功登录")
except NoSuchElementException:
    print("未找到 Files，未登录")


def check_running():
    checkrun = driver.find_element('xpath', '//*[@id="__next"]/div[1]/div[1]/div[2]/header/div[2]/button/span') 
    if checkrun.text == "Run":
        print("当前没有运行，正在点击重启")
        checkrun.click()
    else:
        print("当前正在运行")

time.sleep(2)
check_running()

time.sleep(10)
driver.refresh()

time.sleep(10)
check_running()

# 清除所有cookies
driver.delete_all_cookies()
time.sleep(2)
driver.refresh()

#退出窗口
time.sleep(5)
driver.close()

