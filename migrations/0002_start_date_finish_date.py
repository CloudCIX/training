# libs
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ('training', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cls',
            name='start_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='cls',
            name='finish_date',
            field=models.DateTimeField(null=True),
        ),
    ]
