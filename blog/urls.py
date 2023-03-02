from django.urls import path

from . import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('category/<str:slug>/', views.show_cat, name='cat'),
    path('post/<str:slug>/', views.PostView.as_view(), name='post'),
]
