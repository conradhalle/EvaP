# Generated by Django 2.0.2 on 2018-02-27 21:19

from django.db import migrations, models


def populate_semester_short_names(apps, _schema_editor):
    Semester = apps.get_model('evaluation', 'Semester')

    for semester in Semester.objects.all():
        if semester.name_de.startswith("Sommersemester"):
            semester.short_name_de = "SS {}".format(semester.name_de[-2:])
            semester.short_name_en = "ST {}".format(semester.name_de[-2:])
        elif semester.name_de.startswith("Wintersemester"):
            semester.short_name_de = "WS {}/{}".format(semester.name_de[-7:-5], semester.name_de[-2:])
            semester.short_name_en = "WT {}/{}".format(semester.name_de[-7:-5], semester.name_de[-2:])
        else:
            semester.short_name_de = semester.name_de[-20:]
            semester.short_name_en = semester.name_en[-20:]
        semester.save()


class Migration(migrations.Migration):

    dependencies = [
        ('evaluation', '0075_semester_results_are_archived'),
    ]

    operations = [
        migrations.AddField(
            model_name='semester',
            name='short_name_de',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='short name (german)'),
        ),
        migrations.AddField(
            model_name='semester',
            name='short_name_en',
            field=models.CharField(default='', max_length=20, null=True, verbose_name='short name (english)'),
        ),
        migrations.RunPython(
            populate_semester_short_names,
            reverse_code=migrations.RunPython.noop
        ),
        migrations.AlterField(
            model_name='semester',
            name='short_name_de',
            field=models.CharField(max_length=20, unique=True, verbose_name='short name (german)'),
        ),
        migrations.AlterField(
            model_name='semester',
            name='short_name_en',
            field=models.CharField(max_length=20, unique=True, verbose_name='short name (english)'),
        ),
    ]