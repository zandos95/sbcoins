# Generated by Django 4.1.5 on 2023-02-23 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sbcoins', '0002_post_cprice_post_ycoin'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
