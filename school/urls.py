from django.contrib import admin
from django.urls import path, include


admin.site.site_header = 'IIT Ropar - Admin Panel'
admin.site.index_title = 'Fees Management system'
admin.site.site_title = 'Admin Panel'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("home.urls")),
]
