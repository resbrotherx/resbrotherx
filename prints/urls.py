from django.urls import path
from django.urls.conf import include
from . import views

app_name = 'prints'

urlpatterns = [
    path('prints/', views.prints, name="prints"),
    path('art_category/<slug>/', views.art_category, name="art_category"),
    path('print_details/<id>/' , views.print_details, name='print_details'),
    ]