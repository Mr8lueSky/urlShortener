# Generated by Django 2.2.7 on 2020-08-04 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prefix', models.CharField(max_length=6)),
                ('link', models.CharField(max_length=100)),
            ],
        ),
    ]
