# Generated by Django 5.0.7 on 2024-07-13 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlineshop', '0002_alter_salesnetwork_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salesnetwork',
            name='level',
            field=models.CharField(choices=[('plant', 'завод'), ('shops', 'розничная сеть'), ('enterpreneur', 'индивидуальный предприниматель')], max_length=100, verbose_name='уровень'),
        ),
    ]
