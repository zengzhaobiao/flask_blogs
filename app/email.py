from threading import Thread
from flask import render_template
# from flask import current_app as app
from flask_mail import Message
from . import mail

import os
from . import create_app
app = create_app(os.getenv('FLASK_CONFIG') or 'default')

# # 版本一
# # 发送电子邮件的函数,发送电子邮件时会有延迟，可用多线程处理发送邮件的请求
# def send_email(to,subject,template,**kwargs):
#     msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
#                   sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
#     msg.body = render_template(template + '.txt',**kwargs)
#     msg.html = render_template(template + '.html',**kwargs)
#     mail.send(msg)


# 版本二：异步发送电子邮件
# Flask_Mail中的send函数使用current_app,需使用应用上下文；
# 在不同线程中，执行mail.send()函数需要用app.app_context()人工创建应用上下文。
def send_anync_email(app,msg):
    with app.app_context():
        mail.send(msg)

def send_email(to,subject,template,**kwargs):
    msg = Message(app.config['FLASKY_MAIL_SUBJECT_PREFIX'] + subject,
                  sender=app.config['FLASKY_MAIL_SENDER'],recipients=[to])
    msg.body = render_template(template + '.txt',**kwargs)
    msg.html = render_template(template + '.html',**kwargs)
    thr = Thread(target=send_anync_email,args=[app,msg])
    thr.start()
    return thr