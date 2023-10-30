from sqlalchemy.ext.declarative import declarative_base    #导入declarative_base()函数来创建基类
from sqlalchemy import create_engine, Column, Integer, String, Date, Float
from sqlalchemy.orm import sessionmaker  #导入sessionmaker类函数
from dvadmin.system.util.sql_config import db_info

engine = create_engine(db_info)      #创建引擎
base = declarative_base(engine)     #使用declarative_base()函数来创建SQLORM基类
session = sessionmaker(engine)()    #构建session对象

#报价汇总
class MaterialPriceSummary(base):
    __tablename__ = 'material_price_summary'
    id = Column(Integer, primary_key=True)
    supplier = Column(String(50))
    creator = Column(String(50))  # 创建者
    info = Column(String(50))
    filename = Column(String(50)) #存储的报价文件路径
    file_md5 = Column(String(50)) #文件的md5
    create_time = Column(Date)
    modify_time = Column(Date)

base.metadata.create_all()

"""
DROP TABLE material_price_summary
CREATE TABLE `material_price_summary` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `supplier` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `creator` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `info` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `filename` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `file_md5` varchar(50) COLLATE utf8mb4_bin NOT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`),
  UNIQUE KEY `file_md5` (`file_md5`)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
SHOW CREATE TABLE `material_price_summary`;

"""
