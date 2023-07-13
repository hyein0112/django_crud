from django.contrib import admin
from django.urls import path, include
from addresses import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('addresses/', views.address_list),
    path('addresses/<int:id>', views.address),
]
