host = 'localhost'
port = 3306
username = 'root'
password = 'xingqi123'
db = 'django_vue_admin'

db_info = f'mysql+pymysql://{username}:{password}@{host}:{port}/{db}'

#品牌
brand_dic = {
    'Fujikin': '日本',
    'Tk-fujikin': '日本',
    'Swagelok': '美国',
    'Fitok': '中国',
    'Unilok': '韩国',
    'Dk-lok': '韩国',
    'Super-lok': '韩国',
    'Horiba': '日本',
    'Brooks': '美国',
    'Tem-tech': '日本',
    'CKD': '日本',
    'Festo': '德国',
    'Parker': '美国',
    'SMC': '日本',
    'Omron': '美国',
    '星奇': '中国',
    '皓固': '中国',
    'Azibil': '日本',
    '科百特': '中国',
    '方顿': '中国',
    '创源': '中国',
    '洁安': '中国',
    'Pall': '中国',
    'Entegris': '美国',
    'IFM': '德国',
    'Wika': '德国',
    'UE': '美国',
    'Pureron': '日本',
    'Nagano': '日本',
    'Hamlet': '以色列',
    'Truck': '美国'
}

mode_dic = {
    '球阀': 'ball valve',
    'VCR-隔膜阀': '',
    'VCR-减压阀'
    '接头': '',
    'MFC': '',
    '过滤器': '',
    'Gasket': '',
    'igs-block': '',
    'igs-隔膜阀': '',
    'PT': '',
    '未知': '',
}

