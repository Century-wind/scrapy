# 导入库
from bs4 import BeautifulSoup # 网页解析模块
import requests # 网络请求模块
import csv # csv 文件
import lxml 
import re
import time

# 自如租房页面网址
url = 'http://hz.ziroom.com/z/p{page}/'
# 目标网址：http://hz.ziroom.com/x/807533232.html

# 初始化页码；页码网址：http://hz.ziroom.com/z/p2/
page = 0

# 设置存档文件
csv_file = open('zrrent.csv', 'w', encoding='utf-8')
# 文档写入
csv_writer = csv.writer(csv_file, dialect='excel', delimiter=',')

# 循环页面
while page<3:
    page += 1
    print("fetch: ", url.format(page=page))
    time.sleep(1) # 睡眠1s 防反爬

    # 抓取目标页面
    resp = requests.get(url.format(page=page))
    # 设置编码模式
    resp.encoding = 'utf-8'
    # 创建BS4对象，获取页面
    html = BeautifulSoup(resp.text, features='lxml')
    # 获取当前页面的房子信息 
    house_list = html.find_all('div', class_ = 'item')

    # 循环在读不到房源时结束
    if not house_list:
        print('终结！')
        break

    # 便历房子信息
    for house in house_list:
        # 排队广告
        house_ad = house.find_all('div', class_= 'banner-box')
        if  house_ad:
            print('广告')
            continue
        try:
            # 房子标题
            house_title = house.find('h5').get_text()
            # 房子链接地址
            house_url = house.select('h5 > a')[0]['href']
            house_url = 'https:'+ str(house_url)
            # 房子价格
            house_money = str(house.select('img')).split(' ')
            money = re.findall('\d+', house_money[1]).pop()
            # 标题整理 \W 非字母数字，下划线
            house_info_list = re.split('\W', house_title)
            house_location = house_info_list[1][0:-3]

            csv_writer.writerow([house_title, house_location, money, house_url]) 
        except EOFError as e:
            print(e)
        except AttributeError as ae:
            print(ae)
            
csv_file.close()

