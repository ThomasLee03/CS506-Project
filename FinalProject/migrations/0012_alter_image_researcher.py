# Generated by Django 5.1.3 on 2024-12-07 07:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0011_corruptedimage_researcher_mask_researcher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='researcher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='FinalProject.researcher'),
        ),
    ]
