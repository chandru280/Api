from django.urls import path 
from myapp import views

urlpatterns = [

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
