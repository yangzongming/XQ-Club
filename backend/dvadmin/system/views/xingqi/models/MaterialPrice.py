from sqlalchemy import create_engine, Column, Integer, String, Date, Double
from User import base

class MaterialPrice(base):
    __tablename__ = 'material_price'
    id = Column(Integer, primary_key=True)
    material_id = Column(Integer)
    price = Column(Double)
    amount = Column(Integer)
    supplier = Column(String(50))
    creator = Column(String(50))  # 创建者
    info = Column(String(50))
    xingqi_number = Column(String(50))
    create_time = Column(Date)
    modify_time = Column(Date)


"""
DROP TABLE material_price
CREATE TABLE `material_price` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `material_id` int(10) unsigned NOT NULL,
  `price` double unsigned DEFAULT '0',
  `amount` int(10) unsigned NOT NULL,
  `supplier` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `creator` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `xingqi_number` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `info` varchar(50) COLLATE utf8mb4_bin DEFAULT NULL,
  `create_time` timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `modify_time` timestamp NOT NULL DEFAULT '0000-00-00 00:00:00',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10000 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;
SHOW CREATE TABLE `material_price`;

"""