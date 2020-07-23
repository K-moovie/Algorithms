# 라이브러리 불러오기
import requests
from bs4 import BeautifulSoup

# 검색 키워드
search_word = '삼성전자'

# 해당 url의 html문서를 soup 객체로 저장
url = f'https://m.search.naver.com/search.naver?where=m_news&sm=mtb_jum&query={search_word}'
req = requests.get(url)
html = req.text
soup = BeautifulSoup(html, 'html.parser')
search_result = soup.select_one('#news_result_list')
news_links = search_result.select('.bx > .news_wrap > a')

for i in news_links:
    print(i.get_text())