from django.urls import path
from .views import CommentCreate


from . import views


app_name = 'thread'


urlpatterns = [
    path('list/detail/<int:pk>/',views.detail, name='detail'),
    path('list/', views.list, name='list'),
    path('new/', views.new, name='new'),  
    path('list/detail/<int:pk>/create/', views.CommentCreate.as_view(), name='comment_create'),
]
