from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

PROMISED_DOWN = 150
PROMISED_UP = 10
TWITTER_EMAIL = "your email"
TWITTER_PASSWORD = "your password"
TWITTER_NAME = "your name"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0

        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)

        # Find cookie and accept
        self.driver.find_element(By.XPATH, '''//*[@id="onetrust-accept-btn-handler"]''').click()

        # Find Go button and click
        time.sleep(2)
        self.driver.find_element(By.XPATH, '''//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]''').click()

        # Find download speed and upload speed
        time.sleep(60)
        down_speed = self.driver.find_element(By.XPATH, '''//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span''')
        # print(f"down: {down_speed.text}")
        self.down = down_speed.text
        up_speed = self.driver.find_element(By.XPATH, '''//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span''')
        # print(f"up: {up_speed.text}")
        self.up = up_speed.text

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/")


        # Find sign in and click
        time.sleep(2)
        self.driver.find_element(By.XPATH, '''//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div[1]/div/div[3]/div[5]/a''').click()

        # Fill in email
        time.sleep(2)
        email = self.driver.find_element(By.XPATH, '''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input''')
        email.send_keys(TWITTER_EMAIL)

        time.sleep(1)
        self.driver.find_element(By.XPATH, '''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div''').click()

        # time.sleep(2)


        time.sleep(2)
        self.driver.find_element(By.XPATH, '''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input''').send_keys(TWITTER_PASSWORD)
        time.sleep(1)
        self.driver.find_element(By.XPATH, '''//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div''').click()

        time.sleep(3)
        content = self.driver.find_element(By.CSS_SELECTOR, '''br[data-text="true"]''')
        content.send_keys(f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for 100down/10up?")

        time.sleep(1)
        self.driver.find_element(By.XPATH, '''//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]/div''').click()

bot = InternetSpeedTwitterBot()

bot.get_internet_speed()
bot.tweet_at_provider()

time.sleep(20)
bot.driver.quit()
