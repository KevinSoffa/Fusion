from .models import Servico, Funcionario, Features
from django.views.generic import TemplateView


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features'] = Features.objects.order_by('?').all()
        return context


class TesteView(TemplateView):
    template_name = '404.html'

class Erro500(TemplateView):
    template_name = '500.html'

# Retorno dos funcionários

