from django.contrib import admin
from django.urls import path, include
from TFS import views

urlpatterns = [
    path('', views.Home),
    path('home', views.Home),
    path('customers', views.customers),
    path('trans', views.trans),
    path('admin/', admin.site.urls),
]
