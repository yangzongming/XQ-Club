from sqlalchemy.ext.declarative import declarative_base    #导入declarative_base()函数来创建基类
from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.orm import sessionmaker  #导入sessionmaker类函数
from dvadmin.system.util.sql_config import db_info

engine = create_engine(db_info)      #创建引擎
base = declarative_base(engine)     #使用declarative_base()函数来创建SQLORM基类
session = sessionmaker(engine)()    #构建session对象


class Material(base):
    __tablename__ = 'material'
    material_id = Column(Integer, primary_key=True)
    material_number = Column(String(50))
    material_name = Column(String(50))
    material_mode = Column(String(50))
    material_brand = Column(String(50))
    creator = Column(String(50)) #创建者
    info = Column(String(50))
    xingqi_number = Column(String(50))
    create_time = Column(Date)
    modify_time = Column(Date)

base.metadata.create_all()

"""
DROP TABLE material
CREATE TABLE `material` (
  `material_id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `material_number` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `material_name` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `material_mode` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `material_brand` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `info` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `creator` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `xingqi_number` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`material_id`),
  UNIQUE KEY `material_number` (`material_number`)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
SHOW CREATE TABLE `material`;

"""