# Generated by Django 4.0.4 on 2022-05-09 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dado', '0002_alter_paciente_cpf_alter_paciente_endereco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='endereco',
            field=models.CharField(max_length=200),
        ),
    ]
