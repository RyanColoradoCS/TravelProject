# Generated by Django 5.1.4 on 2025-03-15 23:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='car_type',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
