from django.urls import path
from . import views

app_name = 'services'

urlpatterns = [
    path('', views.service_list, name='service_list'),
    path('<int:service_id>/', views.service_detail, name='service_detail'),
    path('request/<int:service_id>/', views.request_service, name='request_service'),
    path('my-requests/', views.my_requests, name='my_requests'),
]
