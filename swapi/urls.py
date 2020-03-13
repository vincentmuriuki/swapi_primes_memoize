from django.urls import path
from .views import GetFavChar, GetChar

# app_name = 'view'
urlpatterns = [
    path('', GetFavChar.as_view(template_name='index.html'), name='view-all'),
    path('details/', GetChar.as_view(template_name='single_char.html'), name='view-one')
]
