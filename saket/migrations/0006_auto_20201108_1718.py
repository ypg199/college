# Generated by Django 3.1.2 on 2020-11-08 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('saket', '0005_auto_20201108_1710'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courses_for_sci',
            name='pho',
            field=models.ImageField(upload_to=''),
        ),
    ]
