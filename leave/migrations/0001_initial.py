# Generated by Django 3.2.9 on 2024-03-25 03:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='leave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('leave_id', models.CharField(max_length=10, null=True)),
                ('leave_name', models.CharField(max_length=10, null=True)),
                ('leave_statu_reason', models.CharField(choices=[('因私请假', 'Option 1'), ('因公请假', 'Option 2')], max_length=10, null=True)),
                ('leave_statu', models.CharField(choices=[('已请假', 'Option 1'), ('已销假', 'Option 2')], max_length=10, null=True)),
                ('leave_reason', models.CharField(max_length=255, null=True)),
                ('leave_stime', models.DateTimeField(null=True)),
                ('leave_etime', models.DateTimeField(null=True)),
            ],
        ),
    ]
