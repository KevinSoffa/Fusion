from .models import Servico, Funcionario, Features, Precos
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import ContatoForm


class IndexView(TemplateView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')


    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all()
        context['funcionarios'] = Funcionario.objects.order_by('?').all()
        context['features'] = Features.objects.order_by('?').all()
        context['preco'] = Precos.objects.order_by('id').all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.send_mail()
        messages.success(self.request, 'E-mail enviado com sucesso!')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    def form_invalid(self, form, *args, **kwargs):
        messages.error(self.request, 'Erro ao enviar o E-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)


class TesteView(TemplateView):
    template_name = '404.html'

class Erro500(TemplateView):
    template_name = '500.html'
