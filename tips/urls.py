from django.urls import path, include


from . import views


app_name = 'tips'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    path('rule/', views.RuleView.as_view(), name="rule"),
    path('home/thread/', include('thread.urls', namespace='thread')),
    path('create/', views.Create_account.as_view(), name="create_account"),
    path('login/', views.Account_login.as_view(), name="login"),
]
