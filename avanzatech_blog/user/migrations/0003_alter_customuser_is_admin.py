# Generated by Django 5.0.2 on 2024-02-29 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_customuser_created_date_customuser_is_admin_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='is_admin',
            field=models.BooleanField(default=False, verbose_name='is admin or blogger'),
        ),
    ]