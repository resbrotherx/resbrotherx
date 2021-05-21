from django.urls import path
from . import views

app_name = 'graphics'

urlpatterns = [
    path('graphics/', views.graphics, name="graphics"),
    path('graphics_category/<slug>/', views.graphics_category, name="graphics_category"),
    path('graphics_details/<id>/' , views.graphic_details, name='graphic_details'),
    path('search/', views.search, name="search"),
    ]