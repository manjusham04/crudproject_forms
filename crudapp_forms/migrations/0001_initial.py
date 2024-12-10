# Generated by Django 5.1.3 on 2024-12-02 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_id', models.IntegerField(null=True)),
                ('emp_name', models.CharField(max_length=255, null=True)),
                ('emp_address', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
