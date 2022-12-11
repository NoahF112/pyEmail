import smtplib
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.header import Header

sender = '1056095662@qq.com'
reciever = ['ligo125438@126.com']
with open(r'C:\Users\ligo1\Desktop\lizi2\1111.html', 'r', encoding='utf-8') as f:
    content = f.read()

msg = MIMEText(content, 'html', 'utf-8')#邮件正文
msg['Subject'] = Header('hello')#邮件主题


#msg = MIMEMultipart('mixed')
#with open(r'C:\Users\ligo1\Desktop\IMG_9830.JPG', 'rb') as fhandle:
    #att_img = MIMEText(fhandle.read(), 'base64', 'utf-8')
    #att_img['Content-disposition'] = 'attachment;filename="myphoto.jpg"'
#msg.attach(att_img)



# 针对问题：Erro10061 计算机积极拒绝的解决方案 https://www.cnblogs.com/QianyuQian/p/12420406.html
mail = smtplib.SMTP_SSL('smtp.qq.com', 465)
#mail = smtplib.SMTP()
#mail.connect('smtp.qq.com'，)
mail.login(sender, 'rdcpsrrfvoyibbaa')
mail.sendmail(sender, reciever, msg.as_string())
mail.quit()