# Generated by Django 4.1.2 on 2022-12-20 13:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("women", "0006_remove_women_cat"),
    ]

    operations = [
        migrations.AddField(
            model_name="women",
            name="cat",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.PROTECT,
                to="women.category",
            ),
        ),
    ]
