from lxml import etree
import requests

# headers = {
#     'Accept': "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     'Accept-Encoding': "gzip, deflate, br",
#     'Accept-Language': "zh-CN,zh;q=0.9",
#     'Cache-Control': "no-cache",
#     'Connection': "keep-alive",
#     'Cookie': "ll=\"108288\"; bid=pauWbRbGayc; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1517212398%2C%22https%3A%2F%2Fwww.baidu.com%2Flink%3Furl%3DF8eVNDIeOQ9YHzpRmsVRpKZrTGc0oVs4eakLAd29sQF_s5huB9kYoSG9tHex5onq%26wd%3D%26eqid%3D88fe765600008488000000025a6ed2e5%22%5D; _pk_ses.100001.4cf6=*; __yadk_uid=RVGJOluRnhITfw9uEaLjiCN6fpgADGvJ; _vwo_uuid_v2=FD5119D17418A249BF9B9B618C07DF84|f762ca3cd3e0cba238a610ccaac3a20a; __utma=30149280.1920840573.1517213853.1517213853.1517213853.1; __utmc=30149280; __utmz=30149280.1517213853.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utma=223695111.1654494793.1517213853.1517213853.1517213853.1; __utmb=223695111.0.10.1517213853; __utmc=223695111; __utmz=223695111.1517213853.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmb=30149280.1.10.1517213853; _pk_id.100001.4cf6=59bd63525e79da75.1517212398.1.1517216312.1517212398.",
#     'Host': "movie.douban.com",
#     'Referer': "https://movie.douban.com/",
#     'Upgrade-Insecure-Requests': "1",
#     'User-Agent': "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36",
#
#     }


r = requests.get("http://pip.iguye.com")
s = selector = etree.HTML(r.text)

# 取出页面中所有连接
links = s.xpath("//@href")

# 查找最近热门电影的名称，动态加载，无法抓取
# hot_movie = s.xpath('//div[@class="slide-page"]/a/p/text()')
# for movie in hot_movie:
#     print(movie)


# 抓取电影评论
r = requests.get("http://pip.iguye.com/m.htm")
s = etree.HTML(r.text)

# 获取评论人和评论
comments = s.xpath('//div[@class="comment234567890-="]')
for comment in comments:
    username = comment.xpath('./h3/span[2]/a/text()')[0]
    content = comment.xpath('./p/text()')[0]
    stars = comment.xpath('./h3/span[2]/span[2]/@class')[0]
    comment_time = comment.xpath('./h3/span[2]/span[3]/@title')
    comment_time = comment_time[0] if comment_time else ""
    print("%s %s %s : \n%s" % (username, stars, comment_time, content))
    # print(comment)
