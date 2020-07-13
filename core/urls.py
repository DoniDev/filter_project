from django.urls import path
from . import views

urlpatterns = [
    path('', views.bootstrap_form_filter, name='bootstrap')
]

