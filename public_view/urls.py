from django.urls import path
from public_view import views

app_name = 'public_view'

urlpatterns = [
    path('about-page/', views.about, name='about'),
    path('detail/<int:abt_id>/', views.about_detail, name = 'about_detail'),
    path('rent-page/', views.rent, name='rent'),
    path('sale-page/', views.sale, name='sale'),
    path('offer-page/', views.sale, name='offer'),
    path('agent-page/', views.agent, name='agent'),
    path('request-page/', views.request, name='request'),
    path('register-page/', views.register, name='register'),
    
]