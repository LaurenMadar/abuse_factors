# Generated by Django 4.1.2 on 2022-12-09 04:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('explore', '0009_alter_medication_brand_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medication',
            name='compound_norm',
            field=models.TextField(default='N/A'),
        ),
    ]