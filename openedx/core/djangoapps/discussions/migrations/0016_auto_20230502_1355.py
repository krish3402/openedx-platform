# Generated by Django 3.2.18 on 2023-05-02 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('discussions', '0015_discussiontopiclink_context'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussionsconfiguration',
            name='discussions_restrictions',
            field=models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('scheduled', 'Scheduled')], default='disabled', help_text='If disabled, posting in discussions will be indefinitely disabled.', max_length=20),
        ),
        migrations.AddField(
            model_name='historicaldiscussionsconfiguration',
            name='discussions_restrictions',
            field=models.CharField(choices=[('enabled', 'Enabled'), ('disabled', 'Disabled'), ('scheduled', 'Scheduled')], default='disabled', help_text='If disabled, posting in discussions will be indefinitely disabled.', max_length=20),
        ),
    ]
