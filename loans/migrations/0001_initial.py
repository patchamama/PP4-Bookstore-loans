# Generated by Django 3.2.19 on 2023-06-22 23:04

import cloudinary.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import loans.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('slug', models.SlugField(max_length=155, unique=True)),
                ('author', models.CharField(max_length=150)),
                ('number_of_items', models.IntegerField(default=1)),
                ('items_to_loan', models.IntegerField(default=0)),
                ('pub_year', models.DateTimeField(blank=True, null=True)),
                ('publisher', models.CharField(blank=True, max_length=100)),
                ('pages', models.IntegerField(default=0)),
                ('isbn', models.CharField(blank=True, max_length=13)),
                ('language', models.CharField(default='eng', max_length=3)),
                ('translators', models.CharField(blank=True, max_length=200)),
                ('description', models.TextField(blank=True)),
                ('cover', cloudinary.models.CloudinaryField(default='notimage', max_length=255, verbose_name='image')),
                ('features', models.TextField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-created_on'],
            },
        ),
        migrations.CreateModel(
            name='Lendingtest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire', models.DateTimeField(blank=True, default=loans.models.add_one_month_at_today)),
                ('number_renowals', models.IntegerField(default=1)),
                ('returned_on', models.DateTimeField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['created_on'],
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('expire', models.DateTimeField(blank=True, default=loans.models.add_one_month_at_today)),
                ('number_renowals', models.IntegerField(default=1)),
                ('status', models.IntegerField(blank=True, choices=[(0, 'Returned'), (1, 'Loaned')], default=1)),
                ('returned_on', models.DateTimeField(blank=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_loans', to='loans.book')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_loans', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('comment', models.TextField()),
                ('approved', models.BooleanField(default=False)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='book_comments', to='loans.book')),
            ],
            options={
                'ordering': ['created_on'],
            },
        ),
    ]
