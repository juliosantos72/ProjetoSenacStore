# Generated by Django 4.0.6 on 2022-07-14 00:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Produto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('descricao', models.TextField(max_length=8000)),
                ('imagem', models.ImageField(upload_to='imagem/')),
                ('preco', models.DecimalField(decimal_places=2, max_digits=10)),
                ('estoque', models.IntegerField()),
                ('lancamento', models.BooleanField()),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.categoria')),
            ],
        ),
        migrations.AddField(
            model_name='categoria',
            name='Departamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Store.departamento'),
        ),
    ]
