from django.urls import path
from . import views


urlpatterns = [
    path('',views.index,name='index'),
    path('submit',views.submit,name='submit'),
    path('display',views.display,name='display'),
    path('search',views.search,name='search'),
    path('display/delete/<int:id>',views.delete_recipe,name='delete_recipe'),
]