import sys
import requests
from urllib import request
from http import cookiejar

sys.path.append('/home/yanxianchen/PycharmProjects/CnkiScrapy/')

url = 'http://kns.cnki.net/kns/brief/brief.aspx?curpage=3&RecordsPerPage=50&QueryID=18&ID=&turnpage=1&tpagemode=L&dbPrefix=CJFQ&Fields=&DisplayMode=listmode&PageName=ASP.brief_result_aspx'
# 知网的cookie会定期刷新, 如果过期了就通过requests库获取新的cookie
def get_cookie():
    cookie = cookiejar.CookieJar()
    handler = request.HTTPCookieProcessor(cookie)
    opener = request.build_opener(handler)
    response = opener.open(url)
    r = requests.get(url)

    print(r.cookies)
    print('-------------------------------')

    print(cookie)
    cookies = requests.utils.dict_from_cookiejar(cookie)
    print('-------------------------------')
    print(cookies)

    return cookie


if __name__ == '__main__':
    get_cookie()
