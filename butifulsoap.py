from bs4 import BeautifulSoup as bs4
import requests

url = 'https://jobinja.ir/jobs?filters%5Bkeywords%5D%5B%5D=%D8%AC%D9%86%DA%AF%D9%88&filters%5Blocations%5D%5B%5D=&filters%5Bjob_categories%5D%5B%5D=&b='
responce = requests.get(url)
content = bs4(responce.text, 'html.parser')

# print(content.find('a'))
# print(content.find('a').attrs)
# print(content.find('a').text)
# print(content.find('a').name)
# print(content.find_all(attrs={'class': 'c-jobListView__titleLink'}))
# print(content.find_all(class_='c-jobListView__titleLink'))
# print(content.find_all('a', class_='c-jobListView__titleLink'))
# print(len(content.find_all('a')))
# print(content.find_all('a', class_='c-jobListView__titleLink', limit=50))
# print(len(content.find_all('a', class_='c-jobListView__titleLink')))
# print(content.find('a').get('class'))
# print(content.select('a[class="c-jobListView__titleLink"]'))
