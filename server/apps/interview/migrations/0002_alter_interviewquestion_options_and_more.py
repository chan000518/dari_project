# Generated by Django 5.0.4 on 2024-05-03 16:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='interviewquestion',
            options={},
        ),
        migrations.RemoveField(
            model_name='interviewquestion',
            name='order',
        ),
    ]
