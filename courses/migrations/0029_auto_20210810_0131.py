# Generated by Django 3.1.1 on 2021-08-09 22:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0028_formbuilder_response_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formentry',
            name='form',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entries', to='courses.formbuilder'),
        ),
    ]
