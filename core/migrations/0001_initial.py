# Generated by Django 5.0.3 on 2024-05-12 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Work',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='my_works_images')),
                ('name', models.CharField(max_length=100)),
                ('link', models.CharField(max_length=2083)),
                ('type', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
