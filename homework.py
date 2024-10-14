from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service_obj = Service('./chromedriver')
driver = webdriver.Chrome(service=service_obj)

#url = "https://hk.on.cc/hk/bkn/cnt/news/20240927/bkn-20240927080347712-0927_00822_001.html"
#url = "https://hk.on.cc/hk/bkn/cnt/finance/20241014/bkn-20241014092042691-1014_00842_001.html"
url = "https://hk.on.cc/hk/bkn/cnt/intnews/20241014/bkn-20241014092127253-1014_00992_001.html?refer=hn2"
driver.get(url)

# 使用 CSS 選擇器查找元素並獲取文本
try:
    #search = driver.find_element(by=By.CSS_SELECTOR, value="div[class='topHeadline'] h1").text
    #search1 = driver.find_element(by=By.CSS_SELECTOR, value="div[class='topHeadline'] h1").text
    search2 = driver.find_element(by=By.CSS_SELECTOR, value="div[class='topHeadline'] h1").text
    
    #print(search)
    #print(search1)
    print(search2)
    
        
except Exception as e:
    print(f"Error: {e}")

time.sleep(3)
driver.close()  
