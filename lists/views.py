from django.shortcuts import render
from django.http import HttpResponse
from lists.models import Item 

# Create your views here.
#home_page = None
def home_page(request):
	#return HttpResponse('<html><title>To-Do lists</title></html>')
	#if request.method == 'POST':
	#	return HttpResponse(request.POST['item_text'])
	item = Item()
	item.text = request.POST.get('item_text', '')
	item.save()
	
	return render(request, 'home.html',
		{'new_item_text': item.text,
	})
	
