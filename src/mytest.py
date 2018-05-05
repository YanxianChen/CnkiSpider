from src.spider.item import CnkiSpiderItem


def mytest():
    item = CnkiSpiderItem()
    item.authors = '王东波'

    print(item.authors, item.cite_count, item.to_dict())


if __name__ == '__main__':
    mytest()