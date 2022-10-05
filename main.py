from pprint import pprint
import bs4
import requests
from bs4.diagnose import diagnose
from fake_useragent import UserAgent
import re

ua = UserAgent()

URL = "https://habr.com/ru/all/"

headers = {
    "User-Agent": ua.random
}

KEYWORDS = ['дизайн', 'фото', 'web', 'python']

res = requests.get(URL, headers=headers)
text = res.text
soup = bs4.BeautifulSoup(text, features="html.parser")

pattern1 = r'дизайн'
pattern2 = r'фото'
pattern3 = r'web'
pattern4 = r'python'

keywords = [pattern1, pattern2, pattern3, pattern4]

h2_class = "tm-article-snippet__title tm-article-snippet__title_h2"
tag_div_p = "article-formatted-body article-formatted-body article-formatted-body_version-2"
time_data = "tm-article-snippet__datetime-published"

for k in keywords:
    tag_h2 = soup.find_all("h2", class_=h2_class, text=re.compile(pattern=k, flags=re.IGNORECASE))
    tag_div_p = soup.find_all("div", class_=tag_div_p, text=re.compile(pattern=k, flags=re.IGNORECASE))
    time_data_article = soup.find("span", class_=time_data).find("time")
    article_link = soup.find("a", class_='tm-article-snippet__readmore').get('href')

    if tag_h2 != 0 or tag_div_p != 0:
        for i in tag_h2:
            print(
                f'Время выхода: {time_data_article.text}, Название статьи: {i.text}, ссылка: {article_link}')
            for n in tag_div_p:
                print(
                    f'Время выхода: {time_data_article.text}, Название статьи: {i.text}, ссылка: {article_link}')
