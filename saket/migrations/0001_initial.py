# Generated by Django 3.1.2 on 2020-11-06 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Couresea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pho', models.ImageField(upload_to='uploads/')),
                ('fid', models.CharField(max_length=100)),
                ('deg_name', models.CharField(max_length=100)),
                ('dis', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Couresec',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pho', models.ImageField(upload_to='uploads/')),
                ('fid', models.CharField(max_length=100)),
                ('deg_name', models.CharField(max_length=100)),
                ('dis', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Couresecs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pho', models.ImageField(upload_to='uploads/')),
                ('fid', models.CharField(max_length=100)),
                ('deg_name', models.CharField(max_length=100)),
                ('dis', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Coureses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pho', models.ImageField(upload_to='uploads/')),
                ('fid', models.CharField(max_length=100)),
                ('deg_name', models.CharField(max_length=100)),
                ('dis', models.TextField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='NewEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tit', models.CharField(max_length=50)),
                ('tim', models.TimeField(max_length=50)),
                ('dat', models.DateField(max_length=50)),
                ('sub', models.CharField(max_length=50)),
                ('dis', models.TextField(max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=50)),
                ('p_no', models.IntegerField()),
                ('email', models.EmailField(max_length=50, null=True)),
                ('persontage', models.IntegerField()),
                ('maths_marks', models.IntegerField()),
                ('subject', models.CharField(choices=[('SCIENCE', 'SCIENCE'), ('COMMERS', 'COMMERS'), ('COMMERS+MATHS', 'COMMERS+MATHS'), ('ARTS', 'ARTS')], max_length=50)),
                ('deg', models.CharField(choices=[('BscIT', 'BscIT'), ('BscCS', 'BscCS'), ('B.M.S', 'B.M.S'), ('B.COM', 'B.COM'), ('BscIT', 'BscIT'), ('B.M.S', 'B.M.S'), ('B.COM', 'B.COM'), ('B.A', 'B.A')], max_length=50)),
            ],
        ),
    ]
