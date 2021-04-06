# Generated by Django 3.1.7 on 2021-04-06 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
            ],
            options={
                'verbose_name': 'Категория магазина',
                'verbose_name_plural': 'Категории магазинов',
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('city', models.CharField(default='Kazan', max_length=60)),
                ('address', models.CharField(max_length=300)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_published', models.BooleanField(default=True)),
            ],
            options={
                'verbose_name': 'Магазин',
                'verbose_name_plural': 'Магазины',
                'ordering': ['created_at'],
            },
        ),
        migrations.CreateModel(
            name='ShopDescription',
            fields=[
                ('shop', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='shops.shop')),
                ('description', models.TextField(blank=True)),
                ('photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('email', models.EmailField(blank=True, max_length=250, unique=True)),
                ('url', models.URLField(blank=True, max_length=250)),
                ('telegram_url', models.URLField(blank=True, max_length=300)),
                ('pay_in_rub', models.BooleanField(default=True)),
                ('pay_in_btc', models.BooleanField(default=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shops.category')),
            ],
            options={
                'verbose_name': 'Описание магазина',
                'verbose_name_plural': 'Описание магазинов',
            },
        ),
    ]
