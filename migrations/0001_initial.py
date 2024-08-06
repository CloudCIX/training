# stdlib
from typing import List
# libs
import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies: List[str] = []

    operations = [
        migrations.CreateModel(
            name='Cls',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateTimeField()),
                ('finish_date', models.DateTimeField(null=True)),
                ('trainer', models.CharField(max_length=50)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True)),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
            options={
                'db_table': 'cls',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('notes', models.TextField(null=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True)),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
            options={
                'db_table': 'student',
            },
        ),
        migrations.CreateModel(
            name='Syllabus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('member_id', models.IntegerField()),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('deleted', models.DateTimeField(null=True)),
                ('extra', django.contrib.postgres.fields.jsonb.JSONField(default=dict)),
            ],
            options={
                'db_table': 'syllabus',
            },
        ),
        migrations.AddField(
            model_name='cls',
            name='syllabus',
            field=models.ForeignKey(
                to='training.Syllabus',
                on_delete=django.db.models.deletion.CASCADE),
        ),
        migrations.AddField(
            model_name='student',
            name='cls',
            field=models.ForeignKey(
                to='training.Cls',
                on_delete=django.db.models.deletion.CASCADE,
            ),
        ),

        migrations.AddIndex(
            model_name='cls',
            index=models.Index(fields=['id'], name='cls_id'),
        ),
        migrations.AddIndex(
            model_name='cls',
            index=models.Index(fields=['start_date'], name='cls_start_date'),
        ),
        migrations.AddIndex(
            model_name='cls',
            index=models.Index(fields=['finish_date'], name='cls_finish_date'),
        ),
        migrations.AddIndex(
            model_name='cls',
            index=models.Index(fields=['trainer'], name='cls_trainer'),
        ),
        migrations.AddIndex(
            model_name='syllabus',
            index=models.Index(fields=['id'], name='syllabus_id'),
        ),
        migrations.AddIndex(
            model_name='syllabus',
            index=models.Index(fields=['name'], name='syllabus_name'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['id'], name='student_id'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['notes'], name='student_notes'),
        ),
        migrations.AddIndex(
            model_name='student',
            index=models.Index(fields=['user_id'], name='student_user_id'),
        ),
    ]
