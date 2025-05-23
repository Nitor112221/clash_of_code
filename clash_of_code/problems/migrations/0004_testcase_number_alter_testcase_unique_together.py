# Generated by Django 5.2 on 2025-04-10 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_alter_problem_memory_limit_alter_problem_time_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcase',
            name='number',
            field=models.PositiveIntegerField(default=0, verbose_name='number of test'),
        ),
        migrations.AlterUniqueTogether(
            name='testcase',
            unique_together={('problem', 'number')},
        ),
    ]
