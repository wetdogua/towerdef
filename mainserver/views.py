from django.shortcuts import render
from mainserver import UserInfo, BattleSession
from mainserver.forms import BattleForm

def index(request, onsuccess='/', onfail='/login/'):
    if not request.user.is_authenticated():
        return redirect(onfail)
    else:
        print "login successful"
    if request.method == 'POST':
        form = BattleForm(request.POST)
	    if form.is_valid():
  	        battle_start = form.cleaned_data['battle_start']	
		    if battle_start == "1":

