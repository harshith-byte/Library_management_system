# Generated by Django 3.2.15 on 2022-10-01 03:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_administrator_admin_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Book_name', models.CharField(max_length=100)),
                ('Book_author', models.CharField(max_length=100)),
                ('Book_prize', models.IntegerField()),
            ],
        ),
    ]