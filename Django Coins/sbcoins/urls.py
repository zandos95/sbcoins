from django.urls import path
from . import views


urlpatterns = [
    path('',views.post_list, name='post_list'),
    path('login/',views.login_func, name='login'),
    path('logout/',views.user_log_out, name='logout'),
    path('register',views.user_register, name='register'),
    path('post/<int:pk>/', views.get_post, name='post'),
    path('newpost/',views.new_post, name='new_post')
]