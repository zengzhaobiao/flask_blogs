# 主蓝图中定义的错误处理程序
from flask import render_template
from . import main

# 自定义错误页面
@main.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@main.app_errorhandler(500)
def page_not_found(e):
    return render_template('500.html'),500