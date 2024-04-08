import requests
from bs4 import BeautifulSoup

데이터 = requests.get('https://finance.naver.com/item/sise.nhn?code=005930')

soup = BeautifulSoup(데이터.content, 'html.parser')
# print(soup.find_all('strong', id="nowVal")[0].text)

#class는 . // id는 # // 띄어쓰기는 ~의 내부 // 태그명은 그냥 이름만 쓰면된다 // 둘다 만족하는 조건이 필요하면 붙여쓰기
soup.select('.gray .f_up em')[0].text