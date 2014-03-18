from django import forms
from mainserver.models import UserInfo, BattleSession

class BattleForm(forms.Form):
    battle_start = forms.CharField(max_length=1, required=False)
