# Generated by Django 4.2.6 on 2023-10-18 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='choice',
            old_name='Choice_text',
            new_name='choice_text',
        ),
        migrations.RenameField(
            model_name='choice',
            old_name='Question',
            new_name='question',
        ),
    ]