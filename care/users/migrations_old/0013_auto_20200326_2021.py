# Generated by Django 2.2.11 on 2020-03-26 20:21

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("users", "0012_auto_20200326_1752"),
    ]

    operations = [
        migrations.RenameField(
            model_name="localbody",
            old_name="type",
            new_name="body_type",
        ),
    ]