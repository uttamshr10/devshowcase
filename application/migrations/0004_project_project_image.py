# Generated by Django 4.2.1 on 2023-06-07 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_remove_review_tags_remove_review_vote_ratio_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_image',
            field=models.ImageField(blank=True, default='default.jpg', null=True, upload_to=''),
        ),
    ]
