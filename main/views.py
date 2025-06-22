from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

from goods.models import Categories



class IndexView(TemplateView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Магаззин - Главная'
        context['content'] = "ДП Фурман А.А. интернет - магазин мебели"
        return context


class AboutView(TemplateView):
    template_name = 'main/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Магазин - О нас'
        context['content'] = "О нас"
        context['text_on_page'] = "Работу выполнил Фурман А.А. 20-ЗКБ-ИВ1"
        return context
    

