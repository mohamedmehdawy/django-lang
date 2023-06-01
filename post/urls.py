from django.urls import path, include
from .views import PostList
app_name = "post"

urlpatterns = [
    path('', PostList.as_view(), name='post')
]