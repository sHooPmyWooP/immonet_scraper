# Generated by Django 3.1 on 2020-09-06 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scraper', '0012_auto_20200906_1838'),
    ]

    operations = [
        migrations.AddField(
            model_name='item_details',
            name='description',
            field=models.TextField(null=True),
        ),
    ]
