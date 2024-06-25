from django.urls import path
from myapp import views 
urlpatterns = [
    path('hello', views.helloworld),

    path('user/', views.demo, name='get_user'),
    path('user/<int:pk>/', views.demo1, name='get_item'),

]
