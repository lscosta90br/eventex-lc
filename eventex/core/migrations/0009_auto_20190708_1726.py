# Generated by Django 2.2.3 on 2019-07-08 20:26

from django.db import migrations


class Migration(migrations.Migration):
    atomic = False # <<<< THIS LINE

    dependencies = [
        ('core', '0008_course'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Course',
            new_name='CourseOld',
        ),
        migrations.AlterModelOptions(
            name='courseold',
            options={'verbose_name': 'curso', 'verbose_name_plural': 'cursos'},
        ),
    ]
