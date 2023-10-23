from sqlalchemy.ext.declarative import declarative_base    #导入declarative_base()函数来创建基类
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker  #导入sessionmaker类函数
from dvadmin.system.util.sql_config import db_info

engine = create_engine(db_info)      #创建引擎
base = declarative_base(engine)     #使用declarative_base()函数来创建SQLORM基类
session = sessionmaker(engine)()    #构建session对象

class User(base):
    __tablename__ = 'user'
    id = Column(Integer(10), primary_key=True)
    nickname = Column(String(50))

base.metadata.create_all()
