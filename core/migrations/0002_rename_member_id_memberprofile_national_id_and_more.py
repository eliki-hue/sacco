# Generated by Django 5.2.4 on 2025-07-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='memberprofile',
            old_name='member_id',
            new_name='national_id',
        ),
        migrations.AddField(
            model_name='memberprofile',
            name='middle_name',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='memberprofile',
            name='phone',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
