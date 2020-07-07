# Generated by Django 2.2.13 on 2020-07-07 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_todomodel_duedate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todomodel',
            name='priority',
            field=models.CharField(choices=[('danger', 'high'), ('info', 'normal'), ('success', 'low')], max_length=50),
        ),
    ]