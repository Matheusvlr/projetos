from selenium import webdriver
from selenium.webdriver.chrome import service
from webdriver_manager.opera import OperaDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
#from senhas import *

usuario = '//*[@id="email"]'
senha = '//*[@id="txtPassword"]'
botao = '//*[@id="loginModal"]/div/div/div/div/app-loginform/div/div[4]/div/div/div[3]/form/div[4]'

