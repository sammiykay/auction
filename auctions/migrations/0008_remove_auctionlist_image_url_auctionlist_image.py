# Generated by Django 5.0.7 on 2024-11-04 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0007_winner_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auctionlist',
            name='image_url',
        ),
        migrations.AddField(
            model_name='auctionlist',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]
