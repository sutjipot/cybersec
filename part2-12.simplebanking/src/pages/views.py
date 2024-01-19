from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .models import Account
from django.db.models import Q
import json
 
 
 
@login_required
def addView(request):
	numb = request.POST.get('iban')
	user = request.user
	Account.objects.create(owner=user, iban=numb)
	return redirect('/')
 
 
@login_required

def homePageView(request):
    user = request.user
    accounts_owned_by_user = Account.objects.filter(owner=user)
    accounts = list(accounts_owned_by_user.values('iban'))
    return render(request, 'pages/index.html', {'accounts': accounts})
