# Generated by Django 4.0.1 on 2022-02-20 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=30, verbose_name='재고'),
        ),
    ]
