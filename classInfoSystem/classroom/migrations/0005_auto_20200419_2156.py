# Generated by Django 3.0.5 on 2020-04-19 18:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lecture', '0003_auto_20200419_2156'),
        ('department', '0006_auto_20200419_2156'),
        ('classroom', '0004_remove_classroom_field'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='classroom_name',
            field=models.CharField(max_length=50, unique=True, verbose_name='Classroom Name'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='department_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='department.Department', verbose_name='Department Name'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='lecture_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lecture.Lecture', verbose_name='Lecture Name'),
        ),
    ]
