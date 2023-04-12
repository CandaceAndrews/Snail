from django.db import models
from django.contrib.auth.models import User


class Creature(models.Model):
    # Model fields for Creature
    name = models.CharField(max_length=255)
    # ... other fields and methods specific to Creature


class TradeOffer(models.Model):
    # Model fields for TradeOffer
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    creature_to_trade = models.ForeignKey(
        Creature, related_name='creature_to_trade', on_delete=models.CASCADE)
    desired_creature = models.ForeignKey(
        Creature, related_name='desired_creature', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Trade Offer #{self.id}'

    # ... other methods or fields specific to TradeOffer
