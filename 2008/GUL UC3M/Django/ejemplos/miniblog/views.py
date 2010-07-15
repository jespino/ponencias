from django.template import Context, loader
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render_to_response
from ejemplos.miniblog.models import Post
import time


def index(request):
	last_posts = Post.objects.all().order_by('-pub_date')[:5]
	t = loader.get_template('posts/index.html')
	c = Context({'posts':last_posts})
	return HttpResponse(t.render(c))

def index2(request):
	last_posts = Post.objects.all().order_by('-pub_date')[:5]
	context = {'posts':last_posts}
	
	return render_to_response('posts/index.html',context)

def delete(request,id):
	post = Post.objects.get(id=id)
	post.delete()
	return HttpResponseRedirect('/index')

def new(request):
	if request.method=='POST':
		post = Post(title=request.POST['title'],text=request.POST['text'])
		post.save()
		return HttpResponseRedirect('/index')
	else:
		return render_to_response('posts/new.html')
