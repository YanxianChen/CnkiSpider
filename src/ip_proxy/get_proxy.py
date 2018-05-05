import json
import requests
import sys
from requests.exceptions import RequestException

sys.path.append('/home/yanxianchen/PycharmProjects/CnkiScrapy/')
from src import spider_config as Config

# 代理池地址
proxy_pool_url = Config.PROXY_POOL_API


def get_proxy():
    # 使用requests库从代理池中获取新的代理ip地址
    try:
        response = requests.get(proxy_pool_url)
        # 判断请求是否成功, 成功则状态码为200. 成功时返回代理地址, 失败时返回None
        if response.status_code == 200:
            result_str = response.text
            result_dict = json.loads(result_str)
            return result_dict['proxy']
        return None
    except RequestException:
        return None


if __name__ == '__main__':
    proxy = get_proxy()
    print(proxy)
