from django.urls import path
from myapp import views 
urlpatterns = [
    path('hello', views.helloworld),

    path('user/', views.demo, name='get_user'),
    path('user/<int:pk>/', views.demo1, name='get_item'),
    path('user/create/', views.create_item, name='create_item'),
    path('user/update/<int:pk>/', views.update_item, name='update_item'),
    path('user/delete/<int:pk>/', views.delete_item, name='delete_item'),


]
