# Generated by Django 3.1.2 on 2020-11-30 15:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saket', '0014_auto_20201130_1950'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('message', models.TextField(max_length=2000)),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
    ]
