from django.db import models
from datetime import datetime


class Dashboard(models.Model):
    game_id = models.BigIntegerField()
    game_type = models.IntegerField()
    store_front_id = models.IntegerField()
    unit_id = models.IntegerField()
    level_id = models.IntegerField(blank=True)
    insert_date = models.DateTimeField(default = datetime.now, blank=True)
    max_score = models.BigIntegerField( blank=True)
    min_score = models.BigIntegerField( blank=True)
    merchant_id = models.BigIntegerField()
    status = models.IntegerField()


