# Generated by Django 3.0.7 on 2020-07-28 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goodapp', '0009_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sahitya',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sahitya_year', models.CharField(max_length=5)),
                ('sahitya_author', models.CharField(max_length=50)),
                ('sahitya_work_title', models.CharField(max_length=1000)),
                ('sahitya_Genre', models.CharField(max_length=50)),
                ('sahity_information', models.CharField(max_length=1000)),
                ('sahity_wiki', models.CharField(max_length=200)),
            ],
        ),
    ]
