from django.urls import path
from myapp import views 
urlpatterns = [
    path('hello', views.helloworld),

    path('user/', views.UserView.as_view(), name='get_user'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='get_item'),

]
