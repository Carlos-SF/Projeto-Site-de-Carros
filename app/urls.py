
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from cars.views import car_view, new_car_view
from accounts.views import register_view, login_view,logout_view



urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',login_view, name='login'),
    path('logaut/',logout_view, name='Logout'),
    path('register/', register_view, name='register'),
    path('new_car/',new_car_view, name='new_car'),
    path('cars/', car_view, name='cars_list'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

