from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db import transaction
from .models import Account

@transaction.atomic
@login_required  
def transferView(request):
    if request.method == 'POST':
        to_username = request.POST.get('to')
        amount = int(request.POST.get('amount', 0))  #default 0 if nont provided

        try:
            to_user = User.objects.get(username=to_username)
            rcv_acc = Account.objects.get(user=to_user)
            snd_acc = Account.objects.get(user=request.user)

            if snd_acc.balance >= amount > 0:
                rcv_acc.balance += amount
                snd_acc.balance -= amount
                rcv_acc.save()
                snd_acc.save()
            else:
                return HttpResponseBadRequest
                
        except User.DoesNotExist:
            return HttpResponseBadRequest
        except Account.DoesNotExist:
            return HttpResponseBadRequest
    return redirect('/')

@login_required
def homePageView(request):
    accounts = Account.objects.exclude(user_id=request.user.id)
    return render(request, 'pages/index.html', {'accounts': accounts})
