# Generated by Django 5.0.6 on 2024-07-01 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_customuser_babybirth_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='babyBirth',
            new_name='baby_birtday',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='babyGender',
            new_name='baby_gender',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='babyNickname',
            new_name='baby_nickname',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='motherBirth',
            new_name='mother_birthday',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='motherNickname',
            new_name='mother_nickname',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='profileImage',
            new_name='profile_image',
        ),
    ]
