# Generated by Django 2.2.13 on 2022-03-13 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='people',
            name='eye_color',
            field=models.CharField(blank=True, choices=[('black', 'Black'), ('brown', 'Brown'), ('yellow', 'Yellow'), ('red', 'Red'), ('green', 'Green'), ('purple', 'Purple'), ('unknown', 'Unknown')], max_length=32),
        ),
        migrations.AlterField(
            model_name='people',
            name='hair_color',
            field=models.CharField(blank=True, choices=[('black', 'Black'), ('brown', 'Brown'), ('blonde', 'Blonde'), ('red', 'Red'), ('white', 'White'), ('bald', 'Bald')], max_length=32),
        ),
    ]