#-*-coding:utf-8-*-
#Author:raychou
# 'mysql+pymysql://用户名称:密码@localhost:端口/数据库名称'

from pathlib import Path

import os

SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@localhost:3306/osfile'
# 设置是否跟踪数据库的修改情况，一般不跟踪
SQLALCHEMY_TRACK_MODIFICATIONS = False
# 数据库操作时是否显示原始SQL语句，一般都是打开的，因为我们后台要日志
SQLALCHEMY_ECHO = True
