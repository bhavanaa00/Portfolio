# Generated by Django 5.0.4 on 2024-04-30 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0002_formdata_email_formdata_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='about',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.TextField()),
                ('p2', models.TextField(default='null')),
                ('p3', models.TextField(default='null')),
            ],
        ),
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('description', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('sr', models.IntegerField()),
                ('title', models.TextField()),
                ('description', models.TextField(max_length=500)),
                ('link', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('icon', models.TextField()),
                ('name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('heading', models.TextField()),
                ('status', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
    ]
