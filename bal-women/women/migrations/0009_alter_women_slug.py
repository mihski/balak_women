# Generated by Django 4.1.2 on 2022-12-20 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("women", "0008_women_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="women",
            name="slug",
            field=models.SlugField(max_length=255, unique=True, verbose_name="URL"),
        ),
    ]