# Generated by Django 3.1.7 on 2021-03-29 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
