# project/urls.py
from django.contrib import admin
from django.urls import include, path




# Định nghĩa các handler lỗi
handler400 = 'project.views.custom_bad_request'
handler403 = 'project.views.custom_permission_denied'
handler404 = 'project.views.custom_page_not_found'
handler500 = 'project.views.custom_server_error'

from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('shop/', include('shop.urls')),  # Include the shop app URLs here
    path('credit/', include('credit.urls')),  # Other apps
]



