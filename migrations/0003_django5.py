# Generated by Django 5.0.10 on 2025-01-03 18:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training', '0002_start_date_finish_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cls',
            name='extra',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='cls',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='cls',
            name='syllabus',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name='classes',
                to='training.syllabus',
            ),
        ),
        migrations.AlterField(
            model_name='student',
            name='extra',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='extra',
            field=models.JSONField(default=dict),
        ),
        migrations.AlterField(
            model_name='syllabus',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AddIndex(
            model_name='cls',
            index=models.Index(fields=['deleted'], name='cls_deleted'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['deleted'], name='student_deleted'),
        ),
        migrations.AddIndex(
            model_name='syllabus',
            index=models.Index(fields=['deleted'], name='syllabus_deleted'),
        ),
    ]
