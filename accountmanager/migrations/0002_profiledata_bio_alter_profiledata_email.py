# Generated by Django 5.1.1 on 2024-09-25 06:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountmanager', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profiledata',
            name='bio',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
        migrations.AlterField(
            model_name='profiledata',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
    ]
