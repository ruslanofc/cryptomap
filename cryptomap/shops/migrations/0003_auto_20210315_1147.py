# Generated by Django 3.1.7 on 2021-03-15 08:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shops', '0002_auto_20210309_1741'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='shop',
            options={'ordering': ['created_at'], 'verbose_name': 'Магазин', 'verbose_name_plural': 'Магазины'},
        ),
    ]
