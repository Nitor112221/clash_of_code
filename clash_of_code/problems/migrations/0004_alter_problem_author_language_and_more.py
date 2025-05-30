# Generated by Django 5.2 on 2025-04-11 12:22

import tinymce.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('problems', '0003_rename_auther_language_problem_author_language_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problem',
            name='author_language',
            field=models.TextField(
                blank=True,
                choices=[('Py3.11', 'Python 3.11')],
                null=True,
                verbose_name='author language',
            ),
        ),
        migrations.AlterField(
            model_name='problem',
            name='author_solution',
            field=models.TextField(
                blank=True,
                help_text="The author's solution is to take a long time to pass all the tests",
                max_length=8000,
                null=True,
                verbose_name='author solution',
            ),
        ),
        migrations.AlterField(
            model_name='problem',
            name='input_format',
            field=tinymce.models.HTMLField(
                blank=True,
                help_text='Input data format',
                max_length=1000,
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
                max_length=1000,
                null=True,
                verbose_name='output data format',
            ),
        ),
        migrations.AlterField(
            model_name='problem',
            name='tags',
            field=models.ManyToManyField(
                blank=True,
                null=True,
                related_name='tasks',
                to='problems.tag',
                verbose_name='tags',
            ),
        ),
    ]
