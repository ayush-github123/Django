from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    # path('post',views.post,name='post'),
    path('post/<str:pk>/',views.post,name='post'),
]