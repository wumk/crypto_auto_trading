# Generated by Django 2.0.5 on 2018-05-20 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('strategy', '0002_symbol'),
    ]

    operations = [
        migrations.AddField(
            model_name='symbol',
            name='base_asset',
            field=models.CharField(default='base_asset', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='symbol',
            name='quote_asset',
            field=models.CharField(default='quote_asset', max_length=15),
            preserve_default=False,
        ),
    ]