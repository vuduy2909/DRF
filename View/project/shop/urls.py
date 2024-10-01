from django.urls import path

from . import views  # Import your views here
# urlpatterns = [
#     path('', product_list, name='product_list'),  # Đường dẫn cho danh sách sản phẩm
#     path('product/<int:pk>/', product_detail, name='product_detail'),  # Đường dẫn cho chi tiết sản phẩm
# ]



urlpatterns = [
    path('', views.product_list, name='product_list'),  # Root of shop
    path('<int:pk>/', views.product_detail, name='product_detail'),
    path('current-datetime/', views.current_datetime, name='current_datetime'),
     path('add-product/', views.add_product, name='add_product'),
]
