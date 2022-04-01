from django.urls import path

from .views import index, watch_list, brand_detail

urlpatterns = [
    path('', index, name='home'),
    path('<str:slug>/', watch_list, name='watch-list'),
    path('brand/<int:pk>/', brand_detail, name='brand-detail'),

]