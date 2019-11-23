# Generated by Django 2.2 on 2019-11-20 11:25

from django.db import migrations, models

from courses.models import Contest as NewContest


def change_olymp_to_type(apps, schema_editor):
    Contest = apps.get_model('courses', 'Contest')
    for contest in Contest.objects.all():
        if contest.is_olymp:
            contest.contest_type = NewContest.OLYMP
        else:
            contest.contest_type = NewContest.ACM
        contest.save()


def revert_type_to_olymp(apps, schema_editor):
    Contest = apps.get_model('courses', 'Contest')
    for contest in Contest.objects.all():
        if contest.contest_type == NewContest.OLYMP:
            contest.is_olymp = True
        else:
            contest.is_olymp = False
        contest.save()


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_standings_groups'),
    ]

    operations = [
        migrations.AddField(
            model_name='contest',
            name='contest_type',
            field=models.CharField(choices=[('AC', 'Acm'), ('OL', 'Olympiad'), ('BS', 'Battleship'), ('BT', 'Blitz')], default='AC', max_length=2),
        ),
        migrations.RunPython(change_olymp_to_type, revert_type_to_olymp)
    ]