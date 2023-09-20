from django.shortcuts import render
from rest_framework.views import APIView


# Create your views here.

class IndexView(APIView):
    """
        后台隐私政策
        """
    permission_classes = []

    def get(self, request, *args, **kwargs):
        return render(request,'星奇科技测试代码---Leo Hello World! I am django～')