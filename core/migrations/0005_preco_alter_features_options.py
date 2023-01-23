# Generated by Django 4.1.5 on 2023-01-23 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_alter_features_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Preco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('criados', models.DateField(auto_now_add=True, verbose_name='Criação')),
                ('modificado', models.DateField(auto_now=True, verbose_name='Atualização')),
                ('ativo', models.BooleanField(default=True, verbose_name='Ativo?')),
                ('preco', models.CharField(default=True, max_length=10, verbose_name='Preço')),
                ('plano', models.CharField(choices=[('pro', 'PRO'), ('plus', 'PLUS'), ('premium', 'PREMIUM')], default=True, max_length=40, verbose_name='Planos')),
                ('icone', models.CharField(choices=[('lni-package', 'Caixa'), ('lni-drop', 'Gota'), ('lni-star', 'Estrela')], default=True, max_length=25, verbose_name='Icone')),
                ('usuario', models.IntegerField(default=0, verbose_name='Número de Usuários')),
                ('capacidade_db', models.CharField(max_length=50, verbose_name='Capacidade Banco de Dados')),
                ('suporte', models.CharField(max_length=50, verbose_name='Suporte')),
                ('atualizacao', models.CharField(max_length=50, verbose_name='Atualizacao')),
            ],
            options={
                'verbose_name': 'Preço',
                'verbose_name_plural': 'Preços',
            },
        ),
        migrations.AlterModelOptions(
            name='features',
            options={'verbose_name': 'Features'},
        ),
    ]
