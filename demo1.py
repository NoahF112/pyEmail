import smtplib
from email.mime.text import MIMEText #用来包装内容的
from email.header import Header #包装头部信息
user = '1056095662@qq.com'
smtp_obj = smtplib.SMTP()
smtp_obj.connect('smtp.qq.com')
code = 'rdcpsrrfvoyibbaa'
smtp_obj.login(user, code)

# 发给谁
to_persoon = ["ligo125438@126.com"]

# 主题
theme = Header('Py邮件', 'utf-8')

#内容
content = MIMEText('<font color="red">fdsfa </font>', 'html', 'utf-8')

# 发邮件
smtp_obj.sendmail(user, to_persoon, content.as_string())

