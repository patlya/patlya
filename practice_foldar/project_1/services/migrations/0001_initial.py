# Generated by Django 3.2.13 on 2022-06-09 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serv_icon', models.CharField(max_length=200)),
                ('serv_title', models.CharField(max_length=50)),
                ('serv_dis', models.TextField()),
            ],
        ),
    ]
