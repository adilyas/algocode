# Generated by Django 3.1.1 on 2021-08-09 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0027_auto_20210810_0109'),
    ]

    operations = [
        migrations.AddField(
            model_name='formbuilder',
            name='response_text',
            field=models.TextField(blank=True),
        ),
    ]
