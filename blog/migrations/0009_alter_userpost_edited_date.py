# Generated by Django 5.1.4 on 2025-05-17 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_userpost_edited_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userpost',
            name='edited_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
