# Generated by Django 2.2.3 on 2019-07-29 06:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('mainPage', '0002_auto_20190727_0704'),
    ]

    operations = [
        migrations.AddField(
            model_name='financialratio',
            name='dateCreated',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
