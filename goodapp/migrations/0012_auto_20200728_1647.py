# Generated by Django 3.0.7 on 2020-07-28 11:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goodapp', '0011_auto_20200728_1638'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sahitya',
            old_name='sahity_information',
            new_name='sahitya_information',
        ),
        migrations.RenameField(
            model_name='sahitya',
            old_name='sahity_wiki',
            new_name='sahitya_wiki',
        ),
    ]