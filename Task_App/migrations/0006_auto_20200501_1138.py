# Generated by Django 3.0.5 on 2020-05-01 06:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Task_App', '0005_tasklist_manage'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='tasklist',
            options={'ordering': ['-id']},
        ),
    ]
