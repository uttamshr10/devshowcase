# Generated by Django 5.0.4 on 2024-05-14 08:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_review_owner_alter_review_unique_together'),
        ('users', '0003_alter_profile_options'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='review',
            unique_together={('owner', 'project')},
        ),
    ]
