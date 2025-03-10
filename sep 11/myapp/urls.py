from django.urls import path, include 
from myapp import views

from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'books', views.BookViewSet) 
router.register(r'authors', views.BookViewSet2)

urlpatterns = [

    path('', include(router.urls)),

    path('person/create/', views.PersonCreateView.as_view(), name='person-create'),
    path('person/list/', views.PersonListView.as_view(), name='person-list'),
    path('person/<int:id>/details/', views.PersonRetrieveView.as_view(), name='person-detail'),
    path('person/<int:id>/delete/', views.PersonDestroyView.as_view(), name='person-delete'),
    path('person/<int:id>/update/', views.PersonUpdateView.as_view(), name='person-update'),

    path('person/list_create/', views.PersonListCreateView.as_view(), name='person-list_create'),
    path('person/<int:id>/detail_update/', views.PersonRetrieveUpdateView.as_view(), name='person-detail-update'),
    path('person/<int:id>/detail_delete/', views.PersonRetrieveDestroyView.as_view(), name='person-detail-delete'),
    path('person/<int:id>/detail__update_delete/', views.PersonRetrieveUpdateDestroyAPIView.as_view(), name='person-detail-update-delete'),
    

]
