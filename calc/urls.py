from django.urls import path
from .import views
urlpatterns = [
    path('', views.home ,name="home"),
    path('customer',views.customer , name = "customer"),
    path('transfer',views.transfer, name="tranfer"),
    path('transactions',views.transactions, name="transactions"),
    path('help',views.help,name='help')
]
