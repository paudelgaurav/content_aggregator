# Generated by Django 3.1.6 on 2021-02-08 08:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('news', '0012_auto_20210208_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='subscriber',
            field=models.ManyToManyField(blank=True, related_name='topics', to=settings.AUTH_USER_MODEL),
        ),
    ]
