# Generated by Django 5.0.6 on 2024-06-24 11:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee_profile', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='employeeprofile',
            name='profile_picture',
            field=models.ImageField(default='avatar.png', upload_to='profile_pictures/'),
            preserve_default=False,
        ),
    ]
