from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# from selenium.webdriver.support.wait import WebDriverWait 
from selenium.common.exceptions import ElementClickInterceptedException
import time
import os

USER = 'Neptune_Ctg'
PASSWORD = os.environ.get('PASSWORD_CRYPTO')
SIMILAR_ACCOUNT = 'danielavalondo'


class InstaFollower:
    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver= webdriver.Chrome(options=self.chrome_options)
        
        
    def login(self):
        self.driver.get('https://www.instagram.com/')
        time.sleep(2)
        name = self.driver.find_element(By.NAME, 'username')
        name.send_keys(USER)
        password = self.driver.find_element(By.NAME, value='password')
        password.send_keys(PASSWORD)
        time.sleep(2)
        enter = self.driver.find_element(By.XPATH, value='//*[@id="loginForm"]/div/div[3]/button')
        enter.click()
        time.sleep(3)
        try :
            not_remember = self.driver.find_element(By.XPATH, value='//div[contains(text(), "Ahora no")]')
            not_remember.click()
            time.sleep(3)
        except:
            pass
        
        not_noti = self.driver.find_element(By.XPATH, value='/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
        not_noti.click()
        time.sleep(2)
        
        pass
    
    
    def find_followeres(self):
        self.driver.get(f'https://www.instagram.com/{SIMILAR_ACCOUNT}/followers/')        
        
        time.sleep(5)
        pop_up_window = self.driver.find_element(By.CLASS_NAME, value='_aano')       

        for i in range(3):          
            self.driver.execute_script('arguments[0].scrollTop = arguments[0].scrollHeight', pop_up_window)
            print('yes')
            time.sleep(2)        
        pass
    
    def follow(self):
        all_button = self.driver.find_elements(By.CSS_SELECTOR, value='._aano button')
        
        for button in all_button:
            try:
                button.click()
                time.sleep(1)
                    
            except ElementClickInterceptedException:
                cancel = self.driver.find_element(By.XPATH, value='/html/body/div[8]/div[1]/div/div[2]/div/div/div/div/div/div/button[2]')
                cancel.click()
                time.sleep(2)
    
    

bot = InstaFollower()
bot.login()
bot.find_followeres()
bot.follow()


    
