# Generated by Django 5.1.4 on 2025-02-18 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_trip_location'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='location',
            options={'ordering': ['stop_order']},
        ),
        migrations.AddField(
            model_name='location',
            name='stop_order',
            field=models.PositiveIntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='location',
            unique_together={('trip', 'stop_order')},
        ),
    ]
