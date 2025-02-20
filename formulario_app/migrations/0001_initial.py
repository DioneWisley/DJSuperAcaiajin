# Generated by Django 5.0.6 on 2024-06-14 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('idade', models.IntegerField()),
                ('telefone', models.CharField(max_length=20)),
                ('endereco', models.CharField(max_length=200)),
                ('planeta_origem', models.CharField(choices=[('Terra', 'Planeta Terra'), ('Namek', 'Planeta Namek'), ('Vegeta', 'Planeta Vegeta'), ('Outros', 'Outros')], max_length=20)),
                ('raca_preferida', models.CharField(choices=[('Terráqueo', 'Terráqueo'), ('Sayajin', 'Sayajin'), ('Namekuseijin', 'Namekuseijin'), ('Androide', 'Androide'), ('Outros', 'Outros')], max_length=20)),
                ('trabalho', models.CharField(choices=[('Autonomo', 'Autonomo'), ('Empregado CLT', 'Empregado CLT'), ('Empresario', 'Empresario'), ('Tipo Goku', 'Tipo Goku')], max_length=20)),
                ('acai_preferido', models.CharField(choices=[('Puro', 'Puro'), ('Com Banana', 'Com Banana'), ('Com Morango', 'Com Morango'), ('Com Granola', 'Com Granola'), ('Tem gosto de Terra', 'Tem gosto de Terra')], max_length=20)),
                ('tamanho_preferido', models.CharField(choices=[('500ml', '500ml'), ('300ml', '300ml'), ('100ml', '100ml'), ('Casquinha', 'Casquinha'), ('Qual parte do gosto de terra voce nao entendeu?', 'Qual parte do gosto de terra voce nao entendeu?')], max_length=100)),
                ('observacoes', models.TextField()),
            ],
        ),
    ]
