# Generated by Django 3.2.15 on 2022-10-01 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='administrator',
            name='Admin_email',
            field=models.EmailField(error_messages={'unique': 'This email has already been registered.'}, max_length=254, unique=True),
        ),
    ]
