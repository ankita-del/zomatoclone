# Generated by Django 3.1.5 on 2021-08-17 19:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('zomatoapp', '0011_auto_20210817_2033'),
    ]

    operations = [
        migrations.AddField(
            model_name='userproduct',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]