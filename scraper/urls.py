from django.urls import path
from . import views

urlpatterns = [
    path('', views.scraper, name='scraper'),
    path('update_items', views.scraper_update, name='update_items')
]