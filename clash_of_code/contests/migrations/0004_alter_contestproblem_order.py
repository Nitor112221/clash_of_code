# Generated by Django 5.2 on 2025-04-08 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contests', '0003_contest_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contestproblem',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
