import sys
import pymongo
import pymongo.errors

sys.path.append('/home/yanxianchen/PycharmProjects/CnkiScrapy/')
from src import spider_config as Config
from src.utils.smtp_email import send_mail


# 使用mongodb进行数据的持久化
class MongodbClient(object):

    def __init__(self):
        self.mongodb_client = pymongo.MongoClient(Config.MONGO_URL)
        self.db = self.mongodb_client[Config.MONGO_DB]

    def insert(self, data):
        try:
            if self.db[Config.MONGO_TABLE].insert(data):
                return True
            return False
        except pymongo.errors as e:
            send_mail(e, Config.TO_ADDR)
            print('发送成功')


if __name__ == '__main__':
    item = {'a': 1}

    client = MongodbClient()
    if client.insert(item):
        print('插入数据成功')
