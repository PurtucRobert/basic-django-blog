# Generated by Django 4.0.3 on 2022-04-01 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog_post', '0005_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='user',
            field=models.CharField(default='admin', max_length=255),
            preserve_default=False,
        ),
    ]
