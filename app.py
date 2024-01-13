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

driver.get(st.secrets[URL])

time.sleep(3)

st.write(driver.title)

