import requests
from bs4 import BeautifulSoup

r = requests.get("http://httpbin.org/xml")
soup = BeautifulSoup(r.text, 'lxml')
# prin(soup.prettify())
# 获取title节点
print(soup.title)
# 获取title节点的名字
print(soup.title.name)
# 获取title节点的内容
print(soup.title.string)
# 获取title节点的父节点
print(soup.title.parent)
print(soup.slide)
print(soup.slide['type'])

# 找出所有的item节点
print(soup.find_all('item'))

# 获取文档中所有的文字内容
print(soup.get_text())

r = requests.get('http://httpbin.org')
soup = BeautifulSoup(r.text, 'lxml')
links = soup.find_all('a')
for link in links:
    print(link.get('href'))


