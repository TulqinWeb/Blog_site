from django.urls import path
from .views import PostListView, post_detail

urlpatterns = [
    path('',PostListView.as_view()),
    path('',post_detail,  name='post_detail')
]