# 本文件为项目的配置文件, 所有相关的参数都会存放在这里

# 请求的头部信息
COOKIE = 'Ecp_notFirstLogin=yl1EXP; Ecp_ClientId=4180115215603850117; cnkiUserKey=3a0268a3-5ac0-5e83-63f7-0a2a04d4d421; RsPerPage=50; UM_distinctid=161fe060715296-0181876bc005ee-3a76015a-100200-161fe060716b8b; amid=0bc38dc5-eb1f-4f23-ba1b-3f9d9863eeb5; KNS_DisplayModel=listmode@SCDB; ASP.NET_SessionId=bvbvavuxpuptphl1pjt53jmd; SID_kns=123117; SID_kinfo=125105; SID_klogin=125144; Ecp_lout=1; IsLogin=; SID_krsnew=125134; SID_kcms=124111; SID_knsdelivery=125123; SID_kxreader_new=011122; CNZZDATA3258975=cnzz_eid%3D1735332873-1520380496-http%253A%252F%252Fkns.cnki.net%252F%26ntime%3D1525522421; _pk_ref=%5B%22%22%2C%22%22%2C1525526200%2C%22http%3A%2F%2Fwww.cnki.net%2F%22%5D; _pk_ses=*; LID=; _pk_id=8d2f6d11-c9a5-4276-9cd4-512a4e6739da.1524187756.21.1525527127.1525526200.'
USER_AGENT_LIST = [
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; Linux i686; U;) Gecko/20070322 Kazehakase/0.4.5',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; SV1; QQDownload 732; .NET4.0C; .NET4.0E; 360SE)',
    'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; InfoPath.2; .NET CLR 3.0.04506.30)',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_3) AppleWebKit/535.20 (KHTML, like Gecko) Chrome/19.0.1036.7 Safari/535.20',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Fedora/1.9.0.8-1.fc10 Kazehakase/0.5.6',
    'Mozilla/5.0 (X11; U; Linux x86_64; zh-CN; rv:1.9.2.10) Gecko/20100922 Ubuntu/10.10 (maverick) Firefox/3.6.10',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.71 Safari/537.1 LBBROWSER',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Acoo Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.0.04506)',
    'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.0.12) Gecko/20070731 Ubuntu/dapper-security Firefox/1.5.0.12',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; QQDownload 732; .NET4.0C; .NET4.0E; LBBROWSER)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 10_3 like Mac OS X) AppleWebKit/603.1.30 (KHTML, like Gecko) Version/10.3 Mobile/14E277 Safari/603.1.30',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
]

# 代理池接口地址
PROXY_POOL_API = 'http://127.0.0.1:5001/random'

# SMTP邮件服务相关配置
FROM_ADDR = '13001250622@163.com'
FROM_PASSWORD = '13138586132Jx'
TO_ADDR = '13001250622@163.com'

# 数据库相关操作
MONGO_URL = 'localhost'
MONGO_DB = 'CnkiItem'
MONGO_TABLE = 'item'

