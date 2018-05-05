import os
import sys
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
from email.mime.multipart import MIMEMultipart
sys.path.append('/home/yanxianchen/PycharmProjects/CnkiScrapy/')
from src import spider_config as Config


def _format_address(s):
    name, address = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), address))


def send_mail(text, address, have_att=False):
    """
    :type text: str
    :rtype: None
    """
    form_address = Config.FROM_ADDR
    password = Config.FROM_PASSWORD
    to_address = address
    smtp_server = 'smtp.163.com'

    msg = MIMEMultipart()
    msg['From'] = _format_address('知网爬虫 <%s>' % form_address)
    msg['To'] = _format_address('管理员<%s>' % to_address)
    msg['Subject'] = Header('爬虫运行状态', 'utf-8').encode()
    msg.attach(MIMEText(text, 'plain', 'utf-8'))

    if have_att:
        pass
        # if os.path.exists('BaiduMapData.xls'):
        #     print('有附件')
        #     att = MIMEText(open('BaiduMapData.xls', 'rb').read(), 'base64', 'utf-8')
        #     att["Content-Type"] = 'application/octet-stream'
        #     att["Content-Disposition"] = 'attachment; filename="BaiduMapData.xls"'
        #     msg.attach(att)
        #     print('已附带附件')

    try:
        server = smtplib.SMTP(smtp_server, 25)
        server.login(form_address, password)
        server.sendmail(form_address, [to_address], msg.as_string())
        print('发送成功')
        server.quit()
    except smtplib.SMTPException as e:
        print('发送邮件失败', e)


def main():
    text = '测试'
    send_mail(text, Config.TO_ADDR)


if __name__ == '__main__':
    main()
