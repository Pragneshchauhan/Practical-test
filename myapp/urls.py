from django.urls import path
from .import views
urlpatterns = [
    path('',views.index,name='index'),
    path('save_data',views.save_data,name='save_data'),
    path('order_list',views.order_list,name='order_list'),
    path('search',views.search,name='search'),
]