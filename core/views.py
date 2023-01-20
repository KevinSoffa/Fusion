from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'


class TesteView(TemplateView):
    template_name = '404.html'

class Erro500(TemplateView):
    template_name = '500.html'
