from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
import time
import os
 
env_dist = os.environ
position = dict({
        "latitude":  env_dist['latitude'],
        "longitude": env_dist['longitude'],
        "accuracy": 100
        })
        
print(position)
chrome_option = Options()

chrome_option.add_argument('--headless')
chrome_option.add_argument('--no-sandbox')
chrome_option.add_argument('window-size=1920x1080') # 指定浏览器分辨率
chrome_option.add_argument('--disable-gpu')
chrome_option.add_experimental_option('excludeSwitches', ['enable-automation'])
# action端
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_option)

driver.get("https://www.baidu.com/")
# 伪装地址
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
