from django.db import models
import datetime
from django.utils import timezone

class UserInfo(models.Model):
    user_name = models.CharField(max_length=25)
    user_level = models.CharField(max_length=15) 
    user_exp = models.CharField(max_length=25)
    user_battle_count = models.CharField(max_length=200)
class BattleSession(models.Model):
    user_info = models.ForeignKey(UserInfo)
    battle_session_start = models.DateTimeField('date published')
    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)
