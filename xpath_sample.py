import requests
from lxml import etree

headers = {
    'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    'Accept-Encoding': "gzip, deflate, br",
    'Accept-Language': "zh-CN,zh;q=0.9",
    'Cache-Control': "no-cache",
    'Connection': "keep-alive",
    'Cookie': "ll=\"108288\"; bid=pauWbRbGayc; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1517212398%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DF8eVNDIeOQ9YHzpRmsVRpKZrTGc0oVs4eakLAd29sQF_s5huB9kYoSG9tHex5onq%26wd%3D%26eqid%3D88fe765600008488000000025a6ed2e5%22%5D; _pk_ses.100001.4cf6=*; __yadk_uid=RVGJOluRnhITfw9uEaLjiCN6fpgADGvJ; _vwo_uuid_v2=FD5119D17418A249BF9B9B618C07DF84|f762ca3cd3e0cba238a610ccaac3a20a; __utma=30149280.1920840573.1517213853.1517213853.1517213853.1; __utmc=30149280; __utmz=30149280.1517213853.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1654494793.1517213853.1517213853.1517213853.1; __utmb=223695111.0.10.1517213853; __utmc=223695111; __utmz=223695111.1517213853.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=30149280.1.10.1517213853; _pk_id.100001.4cf6=59bd63525e79da75.1517212398.1.1517216312.1517212398.",
    'Host': "movie.douban.com",
    'Referer': "https://movie.douban.com/",
    'Upgrade-Insecure-Requests': "1",
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
    'Postman-Token': "e1dd3f2a-bdc5-d577-eaf7-521cd71c8793"
    }

r = requests.get('http://movie.douban.com/', headers=headers)

s = selector = etree.HTML(r.text)

# 取出页面中所有的链接
links = s.xpath('//@href')
# print(type(links), len(links))

# 查找最近热门电影的名称
r = requests.get('https://movie.douban.com/subject/26611804/')
s = etree.HTML(r.text)

# 获取每个评论的节点
comments = s.xpath('//div[@class="comment"]')
for comment in comments:
    # 获取当前评论的用户名称
    username = comment.xpath('./h3/span[2]/a/text()')[0]
    # 获取当前评论的内容
    content = comment.xpath("./p/text()")[0]
    # 获取打分的星级
    stars = comment.xpath('./h3/span[2]/span[2]/@class')[0]
    # 评论发表时间
    comment_time = comment.xpath('./h3/span[2]/span[3]/@title')[0]
    comment_time = comment_time[0] if comment_time else ''
    print('%s: %s, %s, %s' % (username, content, comment_time, stars))

# hot_movies = s.xpath('//div[@class="slide-page"]/a/p/text()')
# for movie in hot_movies:
#     print(movie)

