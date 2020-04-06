from urllib.request import urlopen
from bs4 import BeautifulSoup, SoupStrainer
import random, requests
import discord, asyncio
from discord.ext import commands
ctx= input()
num = input()
try:
    num=int(num)
except:
    print('숫자가 입력되지 않았습니다')
try:
    url= 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query='+ctx
    params = {'query' : '파이썬'}
    header_info={'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    response = requests.get(url, headers=header_info, params=params) 
    images = BeautifulSoup(response.content, 'lxml')
    images = images.find_all('img', class_='_img')
    data_images=[]
    for link in images:
        data_images.append(link.get('data-source'))
    print(data_images[num])
except:
    print('작동이 되지 않습니다')