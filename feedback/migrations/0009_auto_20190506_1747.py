# Generated by Django 2.2 on 2019-05-06 12:17

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('feedback', '0008_auto_20190506_1745'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentenrolled',
            name='id',
            field=models.AutoField(auto_created=True, default=django.utils.timezone.now, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='studentenrolled',
            name='course_id',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterModelTable(
            name='studentenrolled',
            table=None,
        ),
    ]
