# Generated by Django 3.2 on 2021-05-07 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Property', '0006_auto_20210507_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reserve',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('notes', models.TextField()),
            ],
        ),
    ]
