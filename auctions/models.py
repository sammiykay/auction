from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    pass

class auctionlist(models.Model):
    user = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    desc = models.TextField()           #CharField cannot be left without giving a max_length, Textfield can
    starting_bid = models.IntegerField()        
    image_url = models.CharField(max_length=228, default = None, blank = True, null = True)
    category = models.CharField(max_length=64)
    active_bool = models.BooleanField(default = True)

class bids(models.Model):
    user = models.CharField(max_length=30)
    listingid = models.IntegerField()
    bid = models.IntegerField()
    

class comments(models.Model):
    user = models.CharField(max_length=64)
    comment = models.TextField()
    listingid = models.IntegerField()
    

class watchlist(models.Model):
    watch_list = models.ForeignKey(auctionlist, on_delete=models.CASCADE)
    user = models.CharField(max_length=64)


class winner(models.Model):
    bid_win_list = models.ForeignKey(auctionlist, on_delete=models.CASCADE)
    user = models.CharField(max_length=64, default=None)
    paid = models.BooleanField(default=False)  # Tracks payment status
    address = models.CharField(max_length=255, blank=True, null=True)  # Stores the user's address
    price = models.IntegerField(default=0)
    def __str__(self):
        return f"{self.user} - {self.bid_win_list.title} - {'Paid' if self.paid else 'Unpaid'}"