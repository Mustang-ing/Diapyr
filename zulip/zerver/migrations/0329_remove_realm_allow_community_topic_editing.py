# Generated by Django 3.2.2 on 2021-05-26 09:48

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("zerver", "0328_migrate_to_edit_topic_policy"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="realm",
            name="allow_community_topic_editing",
        ),
    ]
