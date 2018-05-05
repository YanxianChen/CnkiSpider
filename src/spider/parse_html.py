import re
import sys
import time
from typing import Dict, Any, Union

import requests
from bs4 import BeautifulSoup

sys.path.append('/home/yanxianchen/PycharmProjects/CnkiScrapy/')
from src import spider_config as Config
from src.spider.item import CnkiSpiderItem
from src.utils.smtp_email import send_mail
from src.database.store_to_mongodb import MongodbClient


def parse_html(source_html):
    """
    用于解析获取到的页面
    :type source_html: str
    :return
    """
    # 创建一个CnkiSpiderItem对象, 用于存放一个item的信息
    item = CnkiSpiderItem()
    client = MongodbClient()
    # 详情页的基础url
    detail_url_base = 'http://kns.cnki.net/KCMS/detail/detail.aspx?dbcode=CJFQ&dbname=CJFDHIS2&filename='

    soup = BeautifulSoup(source_html, 'lxml')
    data = soup.select('.GridTableContent tr')

    # 解析网页获得数据
    for i in range(1, 51):
        # 最后一个页面里可能不满50条数据, 所以这里进行越界异常的捕获
        try:
            # 解析标题信息
            title = data[i].select('td')[1].select('a')[0]

            # 解析文章详情页url, 这里使用的是正则表达式
            filename = re.search('.*?filename=(.*?)&.*?', title['href']).group(1)

            # 解析作者信息
            author = data[i].select('.author_flag a')

            authors = []
            for a in author:
                authors.append(a.get_text())

            # 解析期刊名称
            journal = data[i].select('.cjfdyxyz a')[0].get_text()

            # 解析发表时间
            publish_time = data[i].select('td')[4].get_text().strip()[0:10]

            # 解析被引用次数
            cite_count = data[i].select('.KnowledgeNetcont')[0].get_text()
            if cite_count is None:
                cite_count = 0

            # 解析被下载次数
            download_count = data[i].select('.downloadCount')[0].get_text()
            if download_count is None:
                download_count = 0

            # 通过下一级页面, 解析作者所在机构
            detail_url = detail_url_base + str(filename)
            response = requests.get(detail_url)
            time.sleep(1)
            soup_detail = BeautifulSoup(response.text, 'lxml')
            institution = soup_detail.select('.wxTitle .orgn a')
            institutions = []
            for i in institution:
                institutions.append(i.get_text())

            # 将信息存入创建一个CnkiSpiderItem对象中
            item.authors = authors
            item.title = title.get_text()
            item.journal = journal
            item.publish_time = publish_time
            item.cite_count = cite_count
            item.download_count = download_count
            item.institution = institutions

            # 将对象字典化
            item_dict = item.to_dict()  # type: Dict[str, Union[int, Any]]

            # 存入数据库
            client.insert(item_dict)
        except IndexError:
            print(i, '解析页面过程中出现下标越界')
            # 发送邮件通知
            send_mail('解析页面过程中出现下标越界', Config.TO_ADDR)
            continue


if __name__ == '__main__':
    with open('/home/yanxianchen/PycharmProjects/CnkiScrapy/src/spider/sources.html') as f:
        parse_html(f)
