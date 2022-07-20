# Generated by Django 4.0.3 on 2022-07-05 10:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_aboutus_contacts'),
        ('account', '0005_remove_profile_education_remove_profile_experience'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='district',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.district'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='posts.region'),
        ),
    ]