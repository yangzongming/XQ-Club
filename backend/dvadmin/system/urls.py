from django.urls import path
from rest_framework import routers

from dvadmin.system.views.api_white_list import ApiWhiteListViewSet
from dvadmin.system.views.area import AreaViewSet
from dvadmin.system.views.clause import PrivacyView, TermsServiceView
from dvadmin.system.views.datav import DataVViewSet
from dvadmin.system.views.dept import DeptViewSet
from dvadmin.system.views.dictionary import DictionaryViewSet
from dvadmin.system.views.file_list import FileViewSet
from dvadmin.system.views.login_log import LoginLogViewSet
from dvadmin.system.views.menu import MenuViewSet
from dvadmin.system.views.menu_button import MenuButtonViewSet
from dvadmin.system.views.message_center import MessageCenterViewSet
from dvadmin.system.views.operation_log import OperationLogViewSet
from dvadmin.system.views.role import RoleViewSet
from dvadmin.system.views.system_config import SystemConfigViewSet
from dvadmin.system.views.user import UserViewSet
from dvadmin.system.views.xingqi import xingqi_erp

system_url = routers.SimpleRouter()
system_url.register(r'menu', MenuViewSet)
system_url.register(r'menu_button', MenuButtonViewSet)
system_url.register(r'role', RoleViewSet)
system_url.register(r'dept', DeptViewSet)
system_url.register(r'user', UserViewSet)
system_url.register(r'operation_log', OperationLogViewSet)
system_url.register(r'dictionary', DictionaryViewSet)
system_url.register(r'area', AreaViewSet)
system_url.register(r'file', FileViewSet)
system_url.register(r'api_white_list', ApiWhiteListViewSet)
system_url.register(r'system_config', SystemConfigViewSet)
system_url.register(r'message_center', MessageCenterViewSet)
system_url.register(r'datav', DataVViewSet)

urlpatterns = [
    path('system_config/save_content/', SystemConfigViewSet.as_view({'put': 'save_content'})),
    path('system_config/get_association_table/', SystemConfigViewSet.as_view({'get': 'get_association_table'})),
    path('system_config/get_table_data/<int:pk>/', SystemConfigViewSet.as_view({'get': 'get_table_data'})),
    path('system_config/get_relation_info/', SystemConfigViewSet.as_view({'get': 'get_relation_info'})),
    path('login_log/', LoginLogViewSet.as_view({'get': 'list'})),
    path('login_log/<int:pk>/', LoginLogViewSet.as_view({'get': 'retrieve'})),
    path('dept_lazy_tree/', DeptViewSet.as_view({'get': 'dept_lazy_tree'})),
    path('clause/privacy.html', PrivacyView.as_view()),
    path('clause/terms_service.html', TermsServiceView.as_view()),

    #星奇测试
    path('xingqi/index', xingqi_erp.index, name="index"),
    path('xingqi/testJson', xingqi_erp.testJson, name="testJson"),
    #获取采购数据
    path('xingqi/get_purcharse_track_detail',xingqi_erp.get_purcharse_track_detail,name="get_purcharse_track_detail"),
    #获取项目列表
    path('xingqi/get_project_list',xingqi_erp.get_project_list,name="get_project_list"),

    #ERP报价文件上传
    path('xingqi/upload_file',xingqi_erp.upload_file,name="upload_file"),

    #Material报价文件上传
    path('xingqi/upload_material_price_file',xingqi_erp.upload_material_price_file,name="upload_material_price_file"),
]
urlpatterns += system_url.urls
