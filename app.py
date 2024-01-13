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
URL = "https://replit.com/"



st.title("Test Selenium")
st.markdown("You should see some random Football match text below in about 21 seconds")

firefoxOptions = Options()
firefoxOptions.add_argument("--headless")

firefoxOptions.add_argument("--disable-gpu")
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 S```afari/537.36'
firefoxOptionss.add_argument(f'user-agent={user_agent}')
firefoxOptions.add_experimental_option("excludeSwitches",['enable-automation'])
firefoxOptions.add_experimental_option('useAutomationExtension', False)

service = Service(GeckoDriverManager().install())
driver = webdriver.Firefox(
    options=firefoxOptions,
    service=service,
)
driver.get(URL)

time.sleep(3)

st.write(driver.title)

