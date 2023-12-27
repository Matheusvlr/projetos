from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
#from senhas import *

webdriver_service = service.Service(OperaDriverManager().install())
webdriver_service.start()
options = webdriver.ChromeOptions()
#options.add_argument('--headless')
options.add_argument('--disable-logging')
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--start-maximized")
options.add_argument('--disable-extensions')
options.add_argument('--disable-popup-blocking')
options.add_argument('--disable-gpu')
options.add_argument('--disable-infobars')
options.add_argument('--disable-blink-features=AutomationControlled')
options.add_experimental_option('w3c', True)

driver = webdriver.Remote(webdriver_service.service_url,options=options)

driver.maximize_window()

usuario = '//*[@id="email"]'
senha = '//*[@id="txtPassword"]'
botao = '//*[@id="loginModal"]/div/div/div/div/app-loginform/div/div[4]/div/div/div[3]/form/div[4]'