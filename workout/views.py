from django.shortcuts import render
from django.http import HttpResponse, Http404, HttpResponseRedirect
from models import Writer
import pdb
from django.core.cache import cache


# Create your views here.
def bloglist(request):
	try:				
		all_blogs = get_from_cache() 
		all_list = all_blogs.order_by('?')[:5]
		context = {'latest_list': all_list, 'all_blogs': all_blogs,}
		return render(request, 'local/bloglist.html', context)
	except Writer.DoesNotExist:
		raise Http404

def blogdetail(request, list_id):
	try:
		blog = Writer.objects.get(pk = list_id)
		context = {'blog': blog, 'all_blogs': get_from_cache(),}
	except Writer.DoesNotExist:
		raise Http404
	return render(request,'local/blogdetails.html',context)

def get_from_cache():
	#pdb.set_trace()
	all_blogs = cache.get('all_blogs')
	if all_blogs is None:
		all_blogs = Writer.objects.order_by('?')
		cache.set('all_blogs', all_blogs)

	return all_blogs







