# Generated by Django 5.2 on 2025-04-25 00:08

import tinymce.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0011_alter_problem_status_alter_problem_test_error'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='description',
            field=tinymce.models.HTMLField(
                help_text='Explain the idea of the task',
                max_length=100000,
                verbose_name='description',
            ),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_format',
            field=tinymce.models.HTMLField(
                blank=True,
                help_text='Input data format',
                max_length=50000,
                null=True,
                verbose_name='input data format',
            ),
        ),
        migrations.AlterField(
            model_name='problem',
            name='output_format',
            field=tinymce.models.HTMLField(
                blank=True,
                help_text='Output data format',
                max_length=50000,
                null=True,
                verbose_name='output data format',
            ),
        ),
    ]
