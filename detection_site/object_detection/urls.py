from django.urls import path
from .views import triangle_view

urlpatterns = [
    path('', triangle_view, name='triangle_view'),
]

# cd C:\Users\asus\PycharmProjects\SSD_HOME\Object-detection\detection_site
# python manage.py runserver
