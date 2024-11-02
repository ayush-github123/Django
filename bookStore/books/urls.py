from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/',views.login,name='login'),
    path('register/',views.register,name='register'),
    path('logout',views.logout,name='logout'),
    path('favourites/',views.favourites,name='favourites'),
    path('add_fav/<int:book_id>/', views.add_fav, name='add_fav'),
    path('del_fav/<int:book_id>/', views.del_fav, name='del_fav'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
