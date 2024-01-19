from django.http import HttpResponse
from .models import Message
from django.shortcuts import get_object_or_404



# Create your views here.

def homePageView(request):
    message_id = request.GET.get('id')
    message = get_object_or_404(Message, pk=message_id)
    content = message.content if message else 'Hello Web!'
    
    return HttpResponse(content)