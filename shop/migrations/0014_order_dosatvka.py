# Generated by Django 3.1.4 on 2023-06-05 18:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0013_auto_20230605_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='dosatvka',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
    ]
