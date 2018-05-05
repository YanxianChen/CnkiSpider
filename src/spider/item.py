# 定义要爬取的数据项
class CnkiSpiderItem(object):

    def __init__(self):
        # 构造函数, 用于构造要抓取的item, 包括文章题目, 作者, 期刊名,
        # 出版时间, 作者所属机构, 被下载次数, 被引用次数
        self.title = None
        self.authors = None
        self.journal = None
        self.publish_time = None
        self.institution = None
        self.download_count = 0
        self.cite_count = 0

    def to_dict(self):
        # 把item对象转换为list, 方便插入mongodb数据库
        item_dict = {'title': self.title, 'authors': self.authors, 'journal': self.journal,
                     'publish_time': self.publish_time, 'institution': self.institution,
                     'download_count': self.download_count, 'cite_count': self.cite_count}
        return item_dict
