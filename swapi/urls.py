from django.urls import path
from .views import GetFavChar, GetChar

urlpatterns = [
    path('', GetFavChar.as_view(template_name='index.html'), name='CharacterView'),
    path('details/', GetChar.as_view(template_name='single_char.html'), name='UserView')
]