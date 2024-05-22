# Generated by Django 5.0.6 on 2024-05-21 13:26

import wagtail.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("wagtail_fastoche", "0028_remove_wagtailfastocheconfig_footer_description_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="wagtailfastocheconfig",
            name="footer_description_wagtail",
            field=wagtail.fields.RichTextField(blank=True, default="", verbose_name="Description"),
        ),
    ]