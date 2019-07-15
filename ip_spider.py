#  _*_coding:utf-8_*_
import pymysql
import requests
from scrapy.selector import Selector
from fake_useragent import UserAgent



conn = pymysql.connect(host='127.0.0.1', user='root', passwd='q1w2e3r4t5', db='xc_proxy', charset='utf8')
cursor = conn.cursor()


def crawl_ips():
    headers = {
        "User-Agent": UserAgent().random}
    for i in range(1, 1001):
        url = 'http://www.xicidaili.com/nn/{0}'.format(i)
        req = requests.get(url=url, headers=headers)
        selector = Selector(text=req.text)
        all_trs = selector.xpath('//*[@id="ip_list"]//tr')

        ip_lists = []
        for tr in all_trs[1:]:
            speed_str = tr.xpath('td[7]/div/@title').extract()[0]
            if speed_str:
                speed = float(speed_str.split('秒')[0])
            else:
                speed = '?'
            ip = tr.xpath('td[2]/text()').extract()[0]
            port = tr.xpath('td[3]/text()').extract()[0]
            proxy_type = tr.xpath('td[6]/text()').extract()[0].lower()
            ip_lists.append((ip, port, speed, proxy_type))

        for ip_info in ip_lists:
            cursor.execute(
                f"INSERT into proxy_ip(ip,port,speed,proxy_type) VALUES('{ip_info[0]}','{ip_info[1]}',{ip_info[2]},"
                f"'{ip_info[3]}') "
            )
            conn.commit()
if __name__ == '__main__':
    crawl_ips()