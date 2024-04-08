# 종목들 = ['005930', '066575', '005380', '035720', '034220', '003490']

import requests as req
from bs4 import BeautifulSoup

def 현재가(구멍) :
   데이터 =  req.get(f'https://finance.naver.com/item/sise.nhn?code={구멍}')
   soup = BeautifulSoup(데이터.content, 'html.parser')
   return soup.find_all('strong', id="_nowVal")[0].text

price = 현재가('005930')
f.write(price)