# Generated by Django 2.2.5 on 2020-12-22 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_item'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='img',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
