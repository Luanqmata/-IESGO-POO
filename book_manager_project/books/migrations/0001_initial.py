# Generated by Django 5.0.6 on 2024-05-30 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=200)),
                ('publication_date', models.DateField()),
                ('cover_image', models.ImageField(blank=True, null=True, upload_to='book_covers/')),
            ],
        ),
    ]
