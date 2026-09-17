"""
URL configuration for Louis_Vuitton project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from LV import views

urlpatterns = [
    path('', views.LV.as_view(),name="dashboard"),
    path('men/', views.men.as_view(),name="men"),
    path('women/', views.women.as_view(),name="women"),
    path('construction/', views.construction.as_view(),name="construction"),
    
    path('seller/login/', views.seller_login, name="seller_login"),
    path('seller/register/', views.seller_register, name="seller_register"),
    path('seller/logout/', views.seller_logout, name="seller_logout"),
    path('seller/dashboard/', views.seller_dashboard, name="seller_dashboard"),
    path('seller/products/', views.seller_products, name="seller_products"),
    path('seller/products/add/', views.seller_add_product, name="seller_add_product"),
    path('seller/products/update/<int:pk>/', views.seller_update_product, name="seller_update_product"),
    
    path('admin/',admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
