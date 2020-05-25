from random import random
from selenium import webdriver
from time import sleep

from credentials import phone_num, password

'''
parametrizing the paths for better configurability/change control
ideally one should move away from xPaths and use element_ids instead
'''
sign_in_bttn_path = '//*[@id="page"]/div/div/div[1]/div/div[2]/div/div/div/div[2]/div[1]/div/div[2]/a'
use_cell_bttn_path = '//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[3]/div/span/span'
phone_num_prompt_path = '//*[@id="phone"]'
continue_bttn_path = '//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[4]/button/span/span'
password_prompt_path = '//*[@id="pass"]'
sign_in_bttn_2_path = '//*[@id="main"]/div/div[1]/div[2]/main/div/div[2]/form/div[2]/button/span/span'
like_bttn_path = '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[3]/div/div[1]/span'
nah_pass_bttn_path = '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[1]/div/div[1]/span'
continue_bumbling_bttn_path = '//*[@id="main"]/div/div[1]/main/div[2]/article/div/footer/div/div[2]/div/span/span/span'
#super_swipe_bttn_path = '//*[@id="main"]/div/div[1]/main/div[2]/div/div/span/div[2]/div/div[2]/div/div[2]/div/span/span'

class BumbleBot(): 
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login_bumble(self):
        self.driver.get('https://bumble.com')

        sign_in_bttn = self.driver.find_element_by_xpath(sign_in_bttn_path)
        sign_in_bttn.click()

        sleep(2)

        use_cell_bttn = self.driver.find_element_by_xpath(use_cell_bttn_path)
        use_cell_bttn.click()

        sleep(2)

        phone_num_prompt = self.driver.find_element_by_xpath(phone_num_prompt_path)
        phone_num_prompt.send_keys(phone_num)
        continue_bttn = self.driver.find_element_by_xpath(continue_bttn_path)
        continue_bttn.click()

        sleep(2)

        password_prompt = self.driver.find_element_by_xpath(password_prompt_path)
        password_prompt.send_keys(password)
        sign_in_bttn_2 = self.driver.find_element_by_xpath(sign_in_bttn_2_path)
        sign_in_bttn_2.click()

        sleep(1)

    def swipe_right(self):
        like_bttn = self.driver.find_element_by_xpath(like_bttn_path)
        like_bttn.click()  

    def swipe_left(self):
        nah_pass_bttn = self.driver.find_element_by_xpath(nah_pass_bttn_path)
        nah_pass_bttn.click()

    def close_match(self):
        continue_bumbling_bttn = self.driver.find_element_by_xpath(continue_bumbling_bttn_path)
        continue_bumbling_bttn.click()

    def let_it_swipe(self):
        while True:
            sleep(2)
            try:
                rand = random()
                # swipe right 70% of the time
                if rand < 0.7:
                    self.swipe_right()
                else:
                    self.swipe_left()
            except Exception:
                self.close_match()

bot = BumbleBot()
bot.login_bumble()
bot.let_it_swipe()
