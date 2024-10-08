# Generated by Django 5.0.2 on 2024-07-25 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Announcement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('announcement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='createAttendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.IntegerField()),
                ('studName', models.CharField(max_length=50)),
                ('studDept', models.CharField(max_length=50)),
                ('studPeriod', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('Present', 'Present'), ('Absent', 'Absent')], default='Present', max_length=50)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('percentage', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Motivate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('motivate', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Sregister',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sname', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('stuid', models.CharField(max_length=10)),
                ('passw', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='StuMark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('S_name', models.CharField(max_length=30)),
                ('S_roll', models.CharField(max_length=30)),
                ('S_dep', models.CharField(max_length=30)),
                ('tamil', models.IntegerField()),
                ('english', models.IntegerField()),
                ('maths', models.IntegerField()),
                ('science', models.IntegerField()),
                ('social', models.IntegerField()),
                ('total', models.IntegerField()),
                ('per', models.FloatField()),
                ('grade', models.CharField(max_length=30)),
                ('staffid', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='techlog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('staffid', models.CharField(max_length=30)),
                ('password', models.CharField(max_length=30)),
            ],
        ),
    ]
