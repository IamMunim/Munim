# Generated by Django 5.0.3 on 2024-03-13 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_endorsment'),
    ]

    operations = [
        migrations.AddField(
            model_name='endorsment',
            name='approved',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
