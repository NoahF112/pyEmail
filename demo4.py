import poplib
from email.parser import Parser
import lxml.etree as et


def get_email(email, password, host="pop.qq.com"):
    # connect to pop3 server
    server = poplib.POP3(host)
    # open debug
    server.set_debuglevel(1)

    # 身份验证
    server.user(email)
    server.pass_(password)

    # 返回邮件总数目和占用服务器的空间大小（字节数）， 通过stat()方法即可
    # print("Mail counts: {0}, Storage Size: {0}".format(server.stat()))

    # 使用list()返回所有邮件的编号，默认为字节类型的串
    resp, mails, octets = server.list()
    # print("响应信息： ", resp)
    # print("所有邮件简要信息： ", mails)
    # print("list方法返回数据大小（字节）： ", octets)

    # get the latest, index from 1:
    index = len(mails)
    if index < 1:
        return None
    resp, lines, octets = server.retr(index)

    # 可以获得整个邮件的原始文本:
    msg_content = b'\r\n'.join(lines).decode('gbk')
    # 解析出邮件:
    msg = Parser().parsestr(msg_content)
    # print(msg)
    #print("解码后的邮件信息:\r\n"+str(msg))

    # close
    server.close()
    return msg


def get_mail_content(msg):
    if msg == None:
        return None
    for part in msg.walk():
        if not part.is_multipart():
            data = part.get_payload(decode=True)
            #print("emailcontent:\r\n"+data.decode())
    return data.decode('gbk')

email = "1056095662@qq.com"
psw = 'rdcpsrrfvoyibbaa'
msg = get_email(email, psw)
html = et.HTML(get_mail_content(msg))
with open('email.html', 'w', encoding='gbk') as f:
    f.write(get_mail_content(msg))
#print(html.xpath('//div/text()'))