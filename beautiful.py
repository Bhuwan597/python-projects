# from selenium.webdriver.chrome.service import Service
# from selenium import webdriver
# import time
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# path = 'C:/Program Files (x86)/chromedriver.exe'
# options = webdriver.ChromeOptions()
# options.add_experimental_option('detach',True)
# s = Service(path)
# driver = webdriver.Chrome(service=s,options=options)
# driver.get('https://facebook.com')
# time.sleep(2)


# for i in range(1,11):
#     time.sleep(2)
#     phone = driver.find_element(by=By.XPATH, value='//*[@id="email"]')
#     password = driver.find_element(by=By.XPATH, value='//*[@id="pass"]')
#     phone.send_keys('')
#     password.send_keys('')
#     loginButton = driver.find_element(by=By.CSS_SELECTOR, value="button[type='submit']")
#     loginButton.click()

#     # messages = driver.find_element(by=By.XPATH,value='//*[@id="mount_0_0_5H"]/div/div[1]/div/div[2]/div[5]/div[1]/div[2]/span/span/div/div[1]')
#     # print(messages)

# time.sleep(3)
# driver.close()
# import psutil
# print(psutil.sensors_battery().power_plugged)


# import speedtest,math
# st = speedtest.Speedtest()
# upload_speed = math.ceil(st.upload()/(1000000)) 
# download_speed =  math.ceil(st.download()/(1000000)) 
# ping = math.ceil(st.results.ping) 
# print(upload_speed)
# print(download_speed)
# print(ping)

import requests
from bs4 import BeautifulSoup

url = 'https://www.wunderground.com/forecast/np/dhangadhi'
r = requests.get(url)
soup = BeautifulSoup(r.text,'html.parser')
weather = soup.find_all('span', class_ = 'wx-value')
for i in weather:
    print(i.text)