# 主蓝图中定义的应用路由
from datetime import datetime

from flask import render_template, redirect, session, url_for
from flask import current_app as app
from . import main
from .forms import NameForm
from .. import db
from ..models import User
from app.email import send_email



@main.route("/",methods=['Get','Post'])
def index():
    # 最好别让web应用把POST请求作为浏览器的最后请求
    # 版本一：提交表单后，刷新浏览器会弹框询问是否重新提交表单
    # name = None
    # form = NameForm()
    # if form.validate_on_submit():
    #     name = form.name.data
    #     form.name.data = None
    # return render_template('index_bs3_wtf.html',name=name,form=form,current_time=datetime.utcnow())

    # # 版本二:添加闪现消息，以及通过session解决版本一的问题
    # form = NameForm()
    # if form.validate_on_submit():
    #     # 闪现消息：如果前后两次输入的信息不一样，就闪现消息
    #     old_name = session.get('name')
    #     if old_name is not None and old_name != form.name.data:
    #         flash('看起来你换了名字！！！')
    #     session['name'] = form.name.data
    #     return redirect(url_for('index'))
    # return render_template('index_bs3_wtf.html',form=form,name=session.get('name'),
    #                        current_time=datetime.utcnow())

    # 版本三：操作数据库
    form = NameForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.name.data).first()
        # print(User.query.all())
        # 如果是新名字，则添加到数据库并发送邮件给管理者
        if user is None:
            user = User(username=form.name.data)
            db.session.add(user)
            db.session.commit()
            session['known'] = False
            print(user.username)
            # 发送邮件给管理者
            if app.config['FLASKY_ADMIN']:
                send_email(app.config['FLASKY_ADMIN'],'New User',
                           'mail/new_user',user=user)
        else:
            session['known'] = True
        session['name'] = form.name.data
        form.name.data = ''
        return redirect(url_for('main.index'))
    return render_template('index_bs3_wtf_sql.html',form=form,
                           name=session.get('name'),
                           known=session.get('known'),
                           current_time=datetime.utcnow())

@main.route('/home')
def home():
    return redirect(url_for('main.index'))