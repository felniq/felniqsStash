# Generated by Django 3.0.4 on 2020-03-10 22:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AvailableImages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_path', models.CharField(max_length=300)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
    ]
