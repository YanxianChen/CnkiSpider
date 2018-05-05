import sys
import random
import requests
from urllib.parse import urlencode
from requests.exceptions import ConnectionError

sys.path.append('/home/yanxianchen/PycharmProjects/CnkiScrapy/')
from src import spider_config as Config
from src.ip_proxy.get_proxy import get_proxy
from src.spider.parse_html import parse_html

# 设置全局变量proxy, 初始使用本地地址, 被封禁后更换为用代理池中的ip地址
proxy = None
# 设置对页面的最多请求次数
max_count = 5
# 基础请求url
base_url = 'http://kns.cnki.net/kns/brief/brief.aspx?RecordsPerPage=50&QueryID=1&ID=&turnpage=1&tpagemode=L&dbPrefix=CJFQ&Fields=&DisplayMode=listmode&PageName=ASP.brief_result_aspx&'
# 知网爬虫请求头部信息, 必须包含cookie
headers = {
    'Cookie': str(Config.COOKIE),
    'User-Agent': str(random.choice(Config.USER_AGENT_LIST))
}


# curpage=3


def get_html(url, count=1):
    print('Crawling', url)
    print('Trying Count', count)
    global proxy
    # 如果请求次数超过5次, 则放弃对页面的请求
    if count >= max_count:
        print('Tried Too Many Counts')
        return None
    try:
        # 判断是否使用了代理, 使用了则需重新构造requests请求
        if proxy:
            proxies = {
                'http': 'http://' + proxy
            }
            response = requests.get(url, headers=headers, allow_redirects=False, proxies=proxies)
        else:
            response = requests.get(url, headers=headers, allow_redirects=False)
        # 判断请求状态码:
        # 200表示请求成功,返回请求结果;
        # 302表示请求失败, 可能是代理使用过多被封禁, 使用代理池的代理进行更换
        if response.status_code == 200:
            print('Crawl Success')
            return response.text
        if response.status_code == 302:
            print(response.status_code)
            print('This IP Has Been Disabled, Please Replace The Proxy')
            # 从代理池中获取评分高的代理
            proxy = get_proxy()
            if proxy:
                print('Using Proxy:', proxy)
                # 使用代理, 递归调用get_html函数
                return get_html(url)
            else:
                print('Get Proxy Failed')
                return None
    except ConnectionError as e:
        print('Error Occurred', e)
        proxy = get_proxy()
        count += 1
        return get_html(url, count)


# 获取搜索结果页
def get_page_index(page, keyword=None):
    data = {
        'curpage': page,
        # 'keyword': keyword
    }

    # url = 'http://nvsm.cnki.net/kns/brief/brief.aspx?curpage=3&RecordsPerPage=20&QueryID=0&ID=&turnpage=1&tpagemode=L&dbPrefix=CJFQ&Fields=&DisplayMode=listmode&PageName=ASP.brief_result_aspx&isinEn=1'
    url = base_url + urlencode(data)
    index_page = get_html(url)
    return index_page


def parse_page_index(response):
    pass


def main():
    result = get_page_index(3)
    print(result)
    res = parse_html(result)
    print(res)


if __name__ == '__main__':
    main()
