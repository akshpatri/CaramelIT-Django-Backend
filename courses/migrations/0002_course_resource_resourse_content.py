# Generated by Django 3.0.8 on 2020-07-30 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course_resource',
            name='resourse_content',
            field=models.TextField(default='NIL'),
        ),
    ]
