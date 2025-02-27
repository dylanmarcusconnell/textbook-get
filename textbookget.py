from urllib.request import urlretrieve
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time
import json

url1 = "LS0tLS1CRUdJTiBQR1AgTUVTU0FHRS0tLS0tCgpoRjRERHVHdVpRWEdZTzRTQVFkQVkxTCtYYkUyTUFjSW85UUFTQ3NQbmU4SnMySnNhTlc5c2F5Z2VlbnhRVEF3CjROdmRuTXZmc01xL2RqWHR5QTJlZEkrT1VHS3d1TlMvaTJIY3dRNmVpbGcvR2V3RkYrZXBzTnU0d1VhemF5dGkKMUtVQkNRSVE4VXV1Y3BpS2ljbE1sYm9EZ1VpS09FS3dzcjZnN3ZJTFhFeVduY092TU9PRldYT2RnRlVyVk1rawpTcWZlbi9wT2RLVnVQZTFJTEtISytyRjJrdnJlcXhwL1dsczBLQzJISk9LNTJBc0lVb0hNZ3hrT3JDVzM1Mml5CkgrTVkwT0FQaUUzcU0wdGJQWFljcWYyVjIzNWpLMjNnVFhhTy96b3lTREVYaTk4dnJYejlsT0ZoN3NicXdCQU4KR0RrL3dMeUFyc2paRFBTQjJuYWZnbWlDeXhjRmVhND0KPXlRMGoKLS0tLS1FTkQgUEdQIE1FU1NBR0UtLS0tLQo=d"
url2 = "LS0tLS1CRUdJTiBQR1AgTUVTU0FHRS0tLS0tCgpoRjRERHVHdVpRWEdZTzRTQVFkQXZ0VmtocWdSWXplM0dHS1pmN2tQY01lZTRIelQ5M21qemFVSlRGRldEUlV3CjhmWGRQbzRRNDQxUEoyRnhnUHc0a0xHa2xKNXNQYkUyYmxHQ241QmlzTDExNm02bXZDKy81SGJabSswQlVQOVkKMUpjQkNRSVFnUFlodGF6YTh6SGU5cnh0MFNGVHQ2WVFJTmNNYXRWRzJCZXBYdDFXcEVyaExWcW96b0hDQXkzVApqa04rUkwzOU1CWWo0d3RRV2NlTDBFUzUrT05UUHIwNjFPSkRMNytQOHRHZktKVkdEWmJxa0NuK2ViRHRwTmwwCkNYSEZkWVRRTEgzTElERFQ5b3JMaWFjQzA1bnVaOW9lQThSMG82MGVCYk5VY3hSaTBpSlpwWFMvTDB0R2Q1aE0KSmVqZWIxdHk5TjVwCj1iTzVuCi0tLS0tRU5EIFBHUCBNRVNTQUdFLS0tLS0K"
username = ""
unipassword = ""
password = ""
pages = 0


downloadDirectory = os.getcwd() + "/textbook"
os.makedirs(downloadDirectory, exist_ok = True)
params = {'username': username, 'lastname': unipassword}
baseurl = "LS0tLS1CRUdJTiBQR1AgTUVTU0FHRS0tLS0tCgpoRjRERHVHdVpRWEdZTzRTQVFkQW5XRSs5NGNtb0I3eGpSWDJXMEwxcVorTUlFZTAwVGhPcG9Md0t3d0d1QTh3CjY2dGdzTjFlOUJDQURGZU9hck1QOVBEYWFaRUZBVDBhc2RjaUlWTUk3U2U3SEhVUlJrNGphQUxwVG96UGlzWnYKMU1BUEFRa0NFS0tRYkxiWEFiSFMzMXVWbm5mVEFTR0xQRTZUUW5jSWxSZ3VaNTh0Y2N2NVErZGU1Vk1pWFdjSgo3SFBvTjg5V3djbjhXTHk3TGg5ZHRaeHFQOVBZemRicFJZeURhVWtUVTJpUTlaaU82SDZXZ1pBUDU4Wmk0dm9OCmVUenBQOEhxQ3M3Q2hXZ3lsUXRxcmNyamxkaElsSFJUaC91RDc5bXQ0NjJqKzJPc3doSTI0QUcyTWNLbUVoWjcKQ0RZTWpPVCtTRDNPbndhek05WTE4REtyQjN0VU56YXRLWlJBN01xTmVqaGlqYndBQ1JuZmFxVnM3dEgwKzZoUwo0QVlXSWxvWEVOQUJSYTArMGo5R09kZmUKPVJBSUIKLS0tLS1FTkQgUEdQIE1FU1NBR0UtLS0tLQo=i"

classurl = "LS0tLS1CRUdJTiBQR1AgTUVTU0FHRS0tLS0tCgpoRjRERHVHdVpRWEdZTzRTQVFkQW5qelRvVVNicVFXU1RDQzdIbHVubFlmcmRuY0oyMkJEUUszTzVobmFHbUl3CmZKMW9BeE11V0grditYMHlma1Bzb2swMUNIS25sckJVVll2UnFobThpSlV6bWo2OE1vc0JjTCtuY1E2S3lyd0QKMUg4QkNRSVFPTW9JcGFDOUx6RENXR0VZNkp4MkE5Y1dKNG1lVXpHbUlZTy9FMEU1bW9QL2FyZzh1VnRkMjhMdApNWWpnandwUHBrNWZxeU5PN09BZ3J3VTcweXc5ZlNNNXhuZkFUSWRLS1N1bXh0L0kvK3Y5TFZENmtwTmpKeS9oCnpnYWc3eE9MS2x5cWg1QVQ4UnRZQXFyZEM4ZDUvYjFwQ2Z3OXV2M0gyYzRICj1hS1EzCi0tLS0tRU5EIFBHUCBNRVNTQUdFLS0tLS0K"


os.environ["webdriver.chrome.driver"] = 'chromedriver'
chrome_options = Options()
prefs = {'profile.default_content_setting_values.automatic_downloads': 1}
chrome_options.add_experimental_option("prefs", prefs)
driver = webdriver.Chrome(chrome_options=chrome_options)

driver.get(baseurl)
time.sleep(10)
browserpromptX = driver.find_element(By.XPATH, '//button[@aria-label="Close dialog"]')
browserpromptX.click()
usernameprompt = driver.find_element(By.XPATH, '//input[@id="username"]')
passwordprompt = driver.find_element(By.XPATH, '//input[@id="password"]')
submitbutton = driver.find_element(By.XPATH, '//button[@id="mainButton"]')
usernameprompt.send_keys(username)
time.sleep(3)
passwordprompt.send_keys(password)
time.sleep(3)
submitbutton.click()
time.sleep(10)

def getbook():
    for x in range(pages):
        url = url1 + str(x) + url2
        driver.get(url)
        time.sleep(1)
    return 0


divider = driver.find_element(By.XPATH, '//div[@class="title-wrapper pointer"]')
driver.execute_script("arguments[0].click();", divider)
time.sleep(10)

#browserpromptX = driver.find_element(By.XPATH, '//button[@aria-label="Close dialog"]')
#browserpromptX.click()
