# Generated by Django 3.2.5 on 2021-07-30 07:12

from django.db import migrations, models
import student.defaults


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0012_teacher_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='teacher_course',
            name='Year_Of_Admission',
            field=models.IntegerField(default=student.defaults.Year_Admission),
        ),
    ]
