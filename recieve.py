import poplib
import base64
from email.parser import Parser
from email.header import decode_header
from email.utils import parseaddr

def get_email_content():
    useraccount = '1056095662@qq.com'
    psw = 'rdcpsrrfvoyibbaa'
    pop3_server = 'pop.qq.com'
    server = poplib.POP3(pop3_server)
    print(server.getwelcome().decode('utf8'))

    server.user(user=useraccount)
    server.pass_(pswd=psw)

    email_num,email_size = server.stat()
    print('消息数量：{}, 消息大小{}'.format(email_num,email_size))
    rsp, msg_list, rsp_siz = server.list()

    total_mail_numbers = len(msg_list)
    rsp, msglines, msgsiz = server.retr(total_mail_numbers)

    msg_content = b'\r\n'.join(msglines).decode('utf-8')

    msg = Parser().parsestr(text=msg_content)
    #print('解码后的信息：\n{}'.format(msg))
    server.close()
    return msg

get_email_content()
