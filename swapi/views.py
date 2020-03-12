from django.shortcuts import render
import requests
from .services import get_characters
from django.views.generic import TemplateView


class GetFavChar(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = {
            'fav_chars': get_characters()
        }
        # print(context)
        return context


class GetChar(TemplateView):
    template_name = 'single_char.html'

    def get_context_data(self, *args, **kwargs):
        context = {}
        # print(context)
        return context
