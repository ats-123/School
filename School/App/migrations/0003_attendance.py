# Generated by Django 5.0.2 on 2024-07-27 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_createattendance_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('roll_no', models.CharField(max_length=20)),
                ('subject', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=10)),
            ],
        ),
    ]
