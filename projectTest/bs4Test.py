# coding = utf-8

from bs4 import BeautifulSoup
import requests
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection':'keep-alive',
    'Host': 'uadmintest.niceloo.com',
    # 'Content-type': 'text/html; charset=utf-8'
}
url = 'http://uadmintest.niceloo.com'
# response = requests.get(url,headers=head)
# html = response.content.decode('utf-8')
# bs = BeautifulSoup(html,'html.parser')
# print(bs)

from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument('--no-sandbox') #解决DevToolsActivePort文件不存在的报错
chrome_options.add_argument('window-size=1920x1080') #指定浏览器分辨率
chrome_options.add_argument('--disable-gpu') #谷歌文档提到需要加上这个属性来规避bug
chrome_options.add_argument('--hide-scrollbars') #隐藏滚动条, 应对一些特殊页面
chrome_options.add_argument('blink-settings=imagesEnabled=false') #不加载图片, 提升速度
chrome_options.add_argument('--headless') #浏览器不提供可视化页面. linux下如果系统不支持可视化不加这条会启动失败
driver = webdriver.Chrome(chrome_options=chrome_options)
# driver = webdriver.PhantomJS()
# driver = webdriver.Chrome()
# driver.get('http://www.baidu.com')
driver.get(url)
time.sleep(5)
response = driver.page_source
# print(response)
bs = BeautifulSoup(response,'lxml')
# print(bs.prettify())
# btn = bs.find("img",class_ = "loginTypeIcon")
# btn = bs.find_all("img")
dict_class = {}
# for link in btn:
#     list_class = link.get('class')
#     if list_class:
#         for i in range (len(list_class)):
#             dict_class['第%s个图标' % str(i+1)] = list_class[i]
#
# print(dict_class)

btns = bs.find_all("input")
i = 1
for links in btns:
    list_input = links.get('class')
    dict_class['第%s个输入框'% str(i)] = list_input[0]
    i +=1
print(dict_class)
# with open('web.txt','a') as f:
#     f.write(response)
#     f.close()
driver.close()
