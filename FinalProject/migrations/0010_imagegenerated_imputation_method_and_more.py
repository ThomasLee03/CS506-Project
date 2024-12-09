# Generated by Django 5.1.3 on 2024-12-07 06:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FinalProject', '0009_remove_imagegenerated_imputation_method_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='imagegenerated',
            name='imputation_method',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imagegenerated',
            name='researcher',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='generated_images', to='FinalProject.researcher'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imagegenerated',
            name='image_file',
            field=models.ImageField(upload_to='images/generated/'),
        ),
    ]