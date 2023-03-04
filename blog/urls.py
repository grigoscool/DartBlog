from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<str:slug>/', views.PostsByCategory.as_view(),
         name='posts_by_cat'),
    path('post/<str:slug>/', views.PostView.as_view(), name='post-detail'),
    path('tag/<str:slug>/', views.PostsByTag.as_view(), name='post_by_tag'),
    path('search/', views.Search.as_view(), name='search'),
    # auth
    path('login/', views.login, name='login'),
    # path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
]
