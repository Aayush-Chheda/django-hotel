# Generated by Django 3.2 on 2021-05-07 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0007_reserve'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, upload_to='Property/images/'),
        ),
    ]
