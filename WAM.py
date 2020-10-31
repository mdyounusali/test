from selenium import webdriver
import pyautogui
from selenium.webdriver.common.keys import Keys
import time


browser = webdriver.Chrome()

# Open Whatsapp
browser.get('https://web.whatsapp.com')

print("Scan QR code from your phone.\nClick on person you want to send this message.\n\n")
messa = input("Enter the message:  ")
num_of_t = int(input("How many times you want to send message:  "))


elem = browser.find_element_by_css_selector('#main > footer > div.block-compose > div.input-container > div > div.input')
# click on message box
elem.click()

ini = time.time()

# Give user 10 sec to click on message box again
time.sleep(10)

for i in range(num_of_t):
        pyautogui.typewrite(messa)
        elem.send_keys(Keys.ENTER)


ou = time.time()

print("We have sent ", messa, " to person you selected " , num_of_t , " times.\n\nThis process took ", ou-ini, " secs.")
