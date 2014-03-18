from django.shortcuts import render
from mainserver import UserInfo, BattleSession

def index(request):
    if request.method == 'POST':
        form = BattleForm(request.POST)
	    if form.is_valid():
  	        battle_start = form.cleaned_data['battle_start']
		
