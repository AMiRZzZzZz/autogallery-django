from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Home.views import homepage, carshow , singlecar
from Contact.views import contactus
# from Products.views import carslist , singlecar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', homepage),
    path('cars/', carshow),
    path('cars/singlecar/<int:car_id>', singlecar),
    path('contactus/' , contactus)
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL , document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)