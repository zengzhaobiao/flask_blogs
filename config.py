import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY','hard to guess')

    # 配置电子邮件
    MAIL_SERVER = os.environ.get('MAIL_SERVER','smtp.qq.com')
    MAIL_PORT = int(os.environ.get('MAIL_PORT','465'))
    # MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS','true').lower() in \
                   # ['true','on','1']
    MAIL_USE_SSL = True

    # 通过环境变量获取邮箱名和密码或授权码
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    # 配置邮件主题前缀和发件人的地址,收件人保存在环境变量FLASKY_ADMIN中
    FLASKY_MAIL_SUBJECT_PREFIX = '[FLASKY]'
    # 'Flasky Admin <flasky@example.com>'，传给send_email函数作为邮件发送者
    FLASKY_MAIL_SENDER = os.environ.get('MAIL_USERNAME')
    FLASKY_ADMIN = os.environ.get('FLASKY_ADMIN')

    # 配置SQLALCHEMY
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    @staticmethod
    def init_app(app):
        pass

# 开发环境配置
class DevelopmentConfig(Config):
    # 开启调试模式
    DEBUG = True
    # 设置数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
    # SQLALCHEMY_DATABASE_URI = \
    #     'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    TESTING = True
    # 设置数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('TEST_DATABASE_URL') or \
                              'sqlite://'

class ProductionConfig(Config):
    # 设置数据库
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                              'sqlite:///' + os.path.join(basedir, 'data.sqlite')
    # SQLALCHEMY_DATABASE_URI = \
    #     'sqlite:///' + os.path.join(basedir, 'data.sqlite')

config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}