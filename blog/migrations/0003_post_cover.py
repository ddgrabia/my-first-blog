# Generated by Django 2.2.5 on 2019-09-08 14:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cover',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
