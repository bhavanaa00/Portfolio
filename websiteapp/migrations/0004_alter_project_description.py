# Generated by Django 5.0.4 on 2024-05-01 08:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('websiteapp', '0003_about_contact_home_project_skills_work'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(max_length=110),
        ),
    ]