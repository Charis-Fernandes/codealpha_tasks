from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from datetime import date
import json
import os

driver = webdriver.Chrome()
driver.maximize_window()

def login():
    with open('config.json') as configFile:
        credentials=json.load(configFile)
        time.sleep(1)
        driver.find_element(
            By.CSS_SELECTOR, value="div[class='position-relative HeaderMenu-link-wrap d-lg-inline-block']").click()
        time.sleep(3)
        username = driver.find_element(
            By.CSS_SELECTOR, value="input[name='login']")
        username.clear()
        username.send_keys(credentials["USERNAME"])  
        time.sleep(1)      
        password = driver.find_element(
            By.CSS_SELECTOR, value="input[name='password']")
        password.clear()
        password.send_keys(credentials["PASSWORD"])
        submit=driver.find_element(By.CSS_SELECTOR, value="input[type='submit']").click()
        time.sleep(3)
        
    
def addtask():
        repo= driver.find_element(
            By.CSS_SELECTOR, value="input[placeholder='name your new repository...']")
        
        repo.send_keys("CodeAlpha7")
        
        add=driver.find_element(By.CSS_SELECTOR, value="button[name='submit']").click()
        time.sleep(3)

def delete_repo():
    setings=driver.find_element(
            By.CSS_SELECTOR, value="a[id='settings-tab']").click()
    time.sleep(3)
    delete=driver.find_element(By.CSS_SELECTOR, value="button[id='dialog-show-repo-delete-menu-dialog']").click()
    time.sleep(2)
    confirm=driver.find_element(By.CSS_SELECTOR, value="button[id='repo-delete-proceed-button']").click()
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, value="button[id='repo-delete-proceed-button']").click()
    
    type=driver.find_element(
            By.CSS_SELECTOR, value="input[id='verification_field']")
    time.sleep(1)    
    type.send_keys("Charis-Fernandes/CodeAlpha7")
    time.sleep(2)
    driver.find_element(By.CSS_SELECTOR, value="button[id='repo-delete-proceed-button']").click()
    time.sleep(5)

def main():
    try:
        driver.get("https://github.com")
        login()
        addtask()
        delete_repo()
        input("Bot Operation Completed. Press any key...")
        driver.close()
    except Exception as e:
        print(e)
        driver.close()
        
if __name__ == "__main__":
    main()