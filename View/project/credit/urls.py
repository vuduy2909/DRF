# credit/urls.py
from django.urls import path
from . import views

app_name = 'credit'

urlpatterns = [
    path('', views.credit_home, name='credit_home'),
    path('reports/', views.report, name='report'),
    path('reports/<int:id>/', views.report_detail, name='report_detail'),
    path('charge/', views.charge, name='charge'),
]
