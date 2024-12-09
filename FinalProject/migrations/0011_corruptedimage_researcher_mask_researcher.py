# Generated by Django 5.1.3 on 2024-12-07 07:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0010_imagegenerated_imputation_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='corruptedimage',
            name='researcher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FinalProject.researcher'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='mask',
            name='researcher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='FinalProject.researcher'),
            preserve_default=False,
        ),
    ]