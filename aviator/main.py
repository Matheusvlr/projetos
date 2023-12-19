from selenium import webdriver
from selenium.webdriver.common.by import By
import time


driver = webdriver.Firefox()
driver.get('https://br.betano.com/')

while len(driver.find_elements(By.XPATH, '/html/body/iframe[2]')) == 0:
    time.sleep(2)

iframe = driver.find_elements(By.XPATH, '/html/body/iframe[2]')

driver.switch_to.frame(iframe)

while len(driver.find_elements(By.XPATH, '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]')) == 0:
    time.sleep(2)

elemento = driver.find_elements(By.XPATH, '/html/body/app-root/app-game/div/div[1]/div[2]/div/div[2]/div[1]/app-stats-widget/div/div[1]').text

print(elemento)