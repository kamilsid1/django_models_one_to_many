# Generated by Django 5.0.4 on 2024-04-04 07:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DepartmentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=200, verbose_name='Name')),
                ('description', models.CharField(max_length=500, verbose_name='Desc')),
            ],
        ),
        migrations.CreateModel(
            name='StudentModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=100, verbose_name='Name')),
                ('stu_class', models.CharField(max_length=100, verbose_name='Class')),
                ('stu_email', models.EmailField(max_length=254)),
                ('stu_mobile', models.IntegerField()),
                ('stu_department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='app.departmentmodel')),
            ],
        ),
    ]
