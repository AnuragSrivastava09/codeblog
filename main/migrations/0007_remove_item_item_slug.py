# Generated by Django 2.2.5 on 2020-12-30 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_tutorial_tutorial_published'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='item_slug',
        ),
    ]
