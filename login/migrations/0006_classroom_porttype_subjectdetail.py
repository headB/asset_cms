# Generated by Django 2.0.4 on 2018-05-08 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0005_auto_20180506_2229'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClassRoom',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_number', models.IntegerField()),
                ('block_number', models.IntegerField()),
                ('ip_addr', models.CharField(max_length=80)),
                ('ACL', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='PortType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('type', models.CharField(max_length=50)),
                ('port', models.IntegerField()),
                ('rname', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='SubjectDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tid', models.IntegerField()),
                ('subject_name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]
