# Generated by Django 3.2 on 2021-05-05 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='Property',
            name='image',
            field=models.ImageField(default=1, upload_to='Property/images/'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='Property',
            name='area',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
