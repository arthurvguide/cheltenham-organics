# Generated by Django 3.2 on 2022-06-22 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0006_orderfeedback_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='exist_feedback',
            field=models.BooleanField(default=False),
        ),
    ]
