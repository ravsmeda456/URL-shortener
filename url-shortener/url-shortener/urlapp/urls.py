from django.urls import path
from . import views

app_name = 'urlapp'
urlpatterns = [
    path('', views.shortUrl, name='shortUrl'),
    path('view/', views.view_urls, name='viewUrl'),
    path('url/<slug:id>/', views.redirect_urla, name='redirect'),
]
