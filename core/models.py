from stdimage.models import StdImageField
from django.db import models
import uuid


# Gerando nomes únicos para arquivos de imagens
def get_file_path(_instace, filename):
    ext = filename.split('.')[-1]
    filename = f'{uuid.uuid4()}.{ext}'
    return filename


class Base(models.Model):
    criados = models.DateField(
        'Criação', 
        auto_now_add=True
    )
    modificado = models.DateField(
        'Atualização',
        auto_now=True
    )
    ativo = models.BooleanField(
        'Ativo?', 
        default=True
    )

    class Meta:
        abstract = True


class Servico(Base):
    ICONE_CHOICES = (
        ('lni-cog', 'Engrenagem'),
        ('lni-stats-up', 'Gráfico'),
        ('lni-users', 'Usuários'),
        ('lni-layers', 'Desing'),
        ('lni-mobile', 'Mobile'),
        ('lni-rocket', 'Foguete')
    )
    servico = models.CharField(
        'Serviço',
        max_length=100
    )
    descricao = models.TextField(
        'Descrição',
        max_length=200
    )
    icone = models.CharField(
        'Icone',
        max_length=25,
        choices=ICONE_CHOICES
    )

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'

    def __str__(self):
        return self.servico


class Cargo(Base):
    cargo = models.CharField(
        'Cargo', 
        max_length=100
    )

    class Meta:
        verbose_name = 'Cargo',
        verbose_name_plural = 'Cargos'

    def __str__(self):
        return self.cargo


class Funcionario(Base):
    nome = models.CharField(
        'Nome',
        max_length=100
    )
    cargo = models.ForeignKey(
        'core.Cargo',
        verbose_name='Cargo',
        on_delete=models.CASCADE
    )
    bio = models.TextField(
        'Bio', max_length=200
    )
    imagem = StdImageField(
        'Imagem',
        upload_to=get_file_path,
        variations={'thumb': {'width': 480, 'height':480, 'crop': True }}
    )
    facebook = models.CharField(
        'Facebook',
        max_length=100,
        default='#'
    )
    twitter = models.CharField(
        'Twitter',
        max_length=100,
        default='#'
    )
    intagram = models.CharField(
        'Instagram',
        max_length=100,
        default='#'
    )

    class Meta:
        verbose_name ='Funcionário',
        verbose_name_plural = 'Funcionários'

    def __str__(self):
        return self.nome


class Features(Base):
    ICONE_CHOICES = (
        ('lni-rocket', 'Fogete'),
        ('lni-laptop-phone', 'Laptop-Celular'),
        ('lni-cog', 'Engrenagem'),
        ('lni-leaf', 'Folha'),
        ('lni-layers', 'Papel')
    )

    nome = models.CharField(
        'Nome',
        max_length=100
    )
    descricao = models.CharField(
        'Descrição',
        max_length=250
    )
    icone = models.CharField(
        'Icone',
        max_length=25,
        choices= ICONE_CHOICES
    )

    class Meta:
        verbose_name = 'Features'

    def __str__(self):
        return self.nome


class Precos(Base):
    ICONE_CHOICES = (
        ('lni-package', 'Caixa'),
        ('lni-drop', 'Gota'),
        ('lni-star', 'Estrela')
    )
    PLANOS = (
        ('pro', 'PRO'),
        ('plus', 'PLUS'),
        ('premium', 'PREMIUM')
    )

    preco = models.CharField(
        'Preço',
        max_length=10,
        default=True
    )
    plano = models.CharField(
        'Planos',
        max_length=40,
        choices=PLANOS,
        default=True
    )
    icone = models.CharField(
        'Icone',
        max_length=25,
        choices= ICONE_CHOICES,
        default=True
    )
    usuario = models.IntegerField(
        'Número de Usuários',
        default=0
    )
    capacidade_db = models.CharField(
        'Capacidade Banco de Dados',
        max_length=50
    )
    suporte = models.CharField(
        'Suporte',
        max_length=50
    )
    atualizacao = models.CharField(
        'Atualizacao',
        max_length=55
    )

    class Meta:
        verbose_name = 'Preço'
        verbose_name_plural = 'Preços'

    def __str__(self):
        return self.plano
