# Generated by Django 3.0.3 on 2020-07-25 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modules', '0002_task_checkcomplete'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='checkComplete',
            field=models.BooleanField(default=False, verbose_name=''),
        ),
    ]
