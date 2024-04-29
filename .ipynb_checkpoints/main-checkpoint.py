import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd

# 目标网页的URL
url = 'https://www.amazon.com/Apple-MD564LL-A-USB-SuperDrive/dp/B011K4XZQ0/ref=sr_1_2?crid=39AGKX9274YDU&dib=eyJ2IjoiMSJ9.zaRQMQCbrq1hsfiYOZBDu-can6NXUihsapkQtitZawHa5HFYGzR4fhbGErcp4ZjmDZO--8_9fZRKbYcqpE8mE51Fvji1DuOA-Vpv0DyzYVqPLb6t5w6YyzEBVLsNXwkKRnQrtaUgzppqznXgepdSGLn56jMaSJpHP5P0v06WoO-d0vjDBgmAoT5DNF1X0MlhYyVluDZ8jlLEgsExpAxg2CLqBhfiFL_3oKjCCHAYMoY.awuE8Yr6OKTZxUhNd2TRt-2RRlHOkf74e5CcwzejYCM&dib_tag=se&keywords=Apple+USB+SuperDrive&qid=1712521644&sprefix=apple+usb+superdrive%2Caps%2C565&sr=8-2'

# 发起GET请求
response = requests.get(url)

# 检查请求是否成功
if response.status_code == 200:
    # 使用BeautifulSoup解析HTML内容
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # 从解析后的soup对象中提取你感兴趣的信息
    # 例如，提取所有的<a>标签
    for link in soup.find_all('a'):
        print(link.get('href'))
else:
    print('请求失败，状态码：', response.status_code)