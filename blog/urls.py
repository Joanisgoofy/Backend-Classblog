from django.urls import path
from .views import main, detail, contact

# from . import views


urlpatterns = [
    path('', main, name='blog'),
    path('detail', detail, name='more info'),
    path("contact", contact, name="contact"),
]