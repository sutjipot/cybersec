from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.

def addPageView(request):
    items = request.session.get('items', [])
    if request.method == 'POST':
        item = request.POST.get('content', '').strip()
        if item:
            items.append(item)
            request.session['items'] = items

            # Keep only the ten most recent notes
            if len(items) > 10:
                request.session['items'] = items[-10:]
                return JsonResponse({'items': items[-10:]})

    return render(request, 'pages/index.html', {'items' : items})


def erasePageView(request):
    items = request.session['items'] = []
    return render(request, 'pages/index.html', {'items' : items})
	

def homePageView(request):
	# use sessions (the data is stored in a database db.sqlite that is then accessed using a cookie)
	items = request.session.get('items', [])

	# shorter way of writing instead of loader
	return render(request, 'pages/index.html', {'items' : items})
