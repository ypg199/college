# Generated by Django 3.1.2 on 2020-11-08 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saket', '0004_auto_20201108_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses_for_sci',
            name='pho',
            field=models.ImageField(upload_to='gallery'),
        ),
    ]
