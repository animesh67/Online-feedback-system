# Generated by Django 2.2 on 2019-04-18 08:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feedback', '0002_delete_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('SID', models.PositiveIntegerField()),
                ('pswd', models.CharField(max_length=50)),
                ('branch', models.CharField(max_length=3)),
                ('address', models.CharField(max_length=100)),
            ],
        ),
    ]