from django.shortcuts import render
from django.template import loader
from django.db import transaction
from .models import Account


# Create your views here.

def transfer(sender, receiver, amount):
	if amount < 0 or sender == receiver:
		return
	else:
		with transaction.atomic():
			acc1 = Account.objects.select_for_update().get(iban=sender)
			acc2 = Account.objects.select_for_update().get(iban=receiver)
			
			if acc1.balance < amount:
				return
			acc1.balance -= amount
			acc2.balance += amount

			acc1.save()
			acc2.save()
 


def homePageView(request):
	if request.method == 'POST':
		sender = request.POST.get('from')
		receiver = request.POST.get('to')
		amount = int(request.POST.get('amount'))
		transfer(sender, receiver, amount)

	accounts = Account.objects.all()
	context = {'accounts': accounts}
	return render(request, 'pages/index.html', context)
