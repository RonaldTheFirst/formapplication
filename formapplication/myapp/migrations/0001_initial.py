# Generated by Django 4.2.5 on 2024-06-26 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_no', models.CharField(max_length=20)),
                ('customer_name', models.CharField(max_length=100)),
                ('customer_surname', models.CharField(max_length=100)),
                ('customer_dob', models.CharField(max_length=20)),
                ('customer_occupation', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_no', models.CharField(max_length=20)),
                ('user_name', models.CharField(max_length=100)),
                ('user_surname', models.CharField(max_length=100)),
                ('user_dob', models.CharField(max_length=20)),
                ('user_role', models.CharField(max_length=100)),
            ],
        ),
    ]
