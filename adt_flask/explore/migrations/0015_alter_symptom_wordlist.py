# Generated by Django 4.1.2 on 2022-12-10 23:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0014_symptom_name_norm'),
    ]

    operations = [
        migrations.AlterField(
            model_name='symptom',
            name='wordlist',
            field=models.JSONField(null=True),
        ),
    ]
