import time
import os
import requests
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


env_dist = os.environ
position = dict({
        "latitude":  float(env_dist['latitude']),
        "longitude": float(env_dist['longitude']),
        "accuracy": 100
        })
username = env_dist['username']
password = env_dist['password']
# print(username)
# print(password)
print(position)
chrome_option = Options()

chrome_option.add_argument('--headless')
chrome_option.add_argument('--no-sandbox')
# chrome_option.add_argument('window-size=1920x1080') # 指定浏览器分辨率
chrome_option.add_argument('--disable-gpu')
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])
# action端
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_option)
#登录
output_data = ""
url_login='https://ids.chd.edu.cn/authserver/login?service=http%3A%2F%2Fcdjk.chd.edu.cn%2FhealthPunch%2Findex%2Flogin'
flag = True
while flag:
    
    driver.get(url_login)
    time.sleep(2)
    driver.find_element(By.XPATH, '//*[@id="username"]').send_keys(username)
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(password,Keys.ENTER)
    time.sleep(3)
    cur_title = driver.title
    print(cur_title)
    if cur_title == "每日健康打卡":
        print(cur_title)
        flag = False
        break
    print("成功") 
driver.command_executor._commands['set_permission'] = (
'POST', '/session/$sessionId/permissions')
print("driver.command_executor._commands is successful")
driver.execute(
    'set_permission',
    {
        'descriptor': { 'name': 'geolocation' },
        'state': 'granted'
    }
)

print("driver.execute is successful")
driver.execute_cdp_cmd(
    'Emulation.setGeolocationOverride', {
    "latitude": position['latitude'],
    "longitude": position['longitude'],
    "accuracy": position['accuracy']
})

print("driver.execute_cdp_cmd is successful")
time.sleep(2)

print("test ok")
