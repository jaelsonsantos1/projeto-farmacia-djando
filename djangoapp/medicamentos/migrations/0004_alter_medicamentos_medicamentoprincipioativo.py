# Generated by Django 4.2.3 on 2023-07-21 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicamentos', '0003_alter_medicamentos_medicamentoprincipioativo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicamentos',
            name='MedicamentoPrincipioAtivo',
            field=models.CharField(db_column='principio_ativo', max_length=400),
        ),
    ]