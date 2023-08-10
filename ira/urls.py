from django.urls import path
from django.views.generic.base import RedirectView
from . import views

app_name = 'ira'

urlpatterns = [
    path('favicon.ico/', RedirectView.as_view(url='/static/img/favicon.ico', permanent=True), name='favicon'),
    path('', views.index, name='index'),
    path('add-week/', views.add_week, name='add-week'),
]