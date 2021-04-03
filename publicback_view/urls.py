from django.urls import path
from publicback_view import views


app_name = 'publicback_view'

urlpatterns = [
    path('', views.login_view, name='login_view'),
    
]
