from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('', views.home, name='home'),
    path('blog/', views.post_list, name='post_list'),
    path('blog/create/', views.post_create, name='post_create'),
    path('blog/<pk>/update/', views.post_update, name='post_update'),
    path('blog/<pk>/delete/', views.post_delete, name='post_delete'),
    path('blog/<pk>/', views.post_detail, name='post_detail'),
    path('post/<pk>/like/', views.like_post, name='like_post'),
]