# Generated by Django 2.0.4 on 2018-05-15 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0009_auto_20180511_1801'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstimateHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sid', models.IntegerField()),
                ('who', models.CharField(max_length=20)),
                ('who_id', models.IntegerField(default=-1)),
                ('port', models.IntegerField()),
                ('type_detail', models.IntegerField()),
                ('setting_time', models.DateTimeField()),
                ('expired_time', models.DateTimeField()),
                ('class_info_id', models.CharField(max_length=200)),
                ('class_room_name', models.CharField(max_length=100)),
                ('teacher_name', models.CharField(max_length=100)),
                ('class_name', models.CharField(max_length=100)),
                ('total', models.CharField(max_length=20)),
            ],
        ),
    ]