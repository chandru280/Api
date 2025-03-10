from django.urls import path
from myapp import views 
urlpatterns = [
    path('hello', views.helloworld),

    path("note/", views.Notes.as_view()),
    path("login/", views.Login.as_view()),
    path('logout/', views.Logout.as_view()),
    
]
