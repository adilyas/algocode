# Generated by Django 2.1.5 on 2019-04-14 12:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_global_person_model'),
    ]

    operations = [
        migrations.CreateModel(
            name='InformaticsToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contest_ids', models.TextField()),
                ('group_id', models.TextField()),
                ('token', models.TextField()),
            ],
        ),
        migrations.AlterIndexTogether(
            name='informaticstoken',
            index_together={('contest_ids', 'group_id')},
        ),
    ]
