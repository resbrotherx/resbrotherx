from django.db.models import Q
import speech_recognition as sr
import os
import requests
from .models import Item, Tags, picture
from .models import Category as categor
from django.views.generic import ListView, DetailView, View, CreateView
from blog.models import Post, Category, PostView
from magazin.models import Post as mag
from jobs.models import Studios, Jobs
from podcast.models import Podcast
import datetime
from django.http import JsonResponse
from django.urls import reverse
from blog.forms import CommentForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from .code_base import get
from django.http import JsonResponse
import math

def prepare_json(code, data, passed_message=None):
    message = "Action Successful"
    if code < 0:
        message = "An error occured."
    if passed_message:
        message = passed_message
    status = True
    if code < 0:
        status = False,
    return JsonResponse({
        "status": status,
        "code": code,
        "data": data,
        "message": message
    })


# 
def homer(): print("a")

# Create your views here.
def home(request):
    min_max = get.get_max_min_prices();
    return render(request, 'items/index.html', {"min": math.floor(min_max["min_price"]), "max": math.floor(min_max["max_price"])})


def test(request):
    pictures = picture.objects.all()
    items = Item.objects.filter(featured=True)[0:4]
    blog = Post.objects.order_by('-timestamp')[0:4]

    context={
        "i":pictures,
        'items':items,
        "blog":blog,
    }
    return render(request, 'test.html', context)


def new_item(request):
    return render(request, 'new_item.html')


def item_detail(request, id):
    post_all = Item.objects.all()
    post = get_object_or_404(Item, id=id)

    # PostView.objects.get_or_create(user=request.user, post=post)
    context = {
        "post":post,
        'post_all':post_all,
        # 'trend':trend,
    }
    return render(request, 'item_detail.html', context)

def get_all_items(request):
    if 'self' not in request.POST or 'self' not in request.GET:
        # incase form doesnt need ajax
        return (prepare_json(0, get.get_all_items(1)))

def get_max_min_prices(request):
    if 'self' not in request.POST or 'self' not in request.GET:
        return (prepare_json(0, get.get_max_min_prices()))

def filter_items(request):
    if 'self' not in request.POST or 'self' not in request.GET:
        print("X", request.GET['min'], request.GET['max'])
        return (prepare_json(0, get.get_item_by_filter(request.GET['min'],request.GET['max'])))


def about(request):
    return render(request,'about.html')

def sub(request):
    return render(request, 'subscribe.html')

def len(request):
    return render(request, 'learning.html')

def mar(request):
    item  = Item.objects.all()
    cat_all = categor.objects.all()
    tags_all = Tags.objects.all()
    context={
        "i":item,
        "cat":cat_all,
        "tags":tags_all
    }
    return render(request, 'marketplace.html', context)

def job(request):
    studio = Studios.objects.all()
    context = {
        'studio':studio,
    }
    return render(request, 'jobs.html', context)

def blog(request):
    post_all = Post.objects.filter(featured=True)
    cat = Category.objects.all()
    # week_ago = datetime.date.today() - datetime.timedelta(days=7)
    # post_all = Post.objects.filter(timestamp = week_ago).order_by('-count')

    context = {
        'cat':cat,
        'post_all':post_all,
    }
    return render(request, 'blogs.html', context)

def latest(request):
    latest = Post.objects.order_by('-timestamp')
    # # cat = Post.Category.all()
    # week_ago = datetime.date.today() - datetime.timedelta(days=7)
    # post_all = Post.objects.filter(timestamp = week_ago).order_by('-count')

    context = {
        # 'cat':cat,
        'post_all':latest,
    }
    return render(request, 'latest.html', context)
 
def blog_detail(request, id):
    post_all = Post.objects.all()
    post = get_object_or_404(Post, id=id)
    form = CommentForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.instance.user = request.user
            form.instance.post = post
            form.save()
    PostView.objects.get_or_create(user=request.user, post=post)
    context = {
        "form":form,
        "post":post,
        'post_all':post_all,
        # 'trend':trend,
    }
    return render(request, 'blog-detail.html',context)



@login_required
def liked_post(request, id):
    user=request.user
    Like=False
    if request.method=="POST":
        video_id=request.POST['video_id']
        get_video=get_object_or_404(Comment, id=video_id)
        w=Comment.objects.get(id=video_id)
        if user in w.likes.all():
            w.likes.remove(user)
            Like=False
        else:
            w.likes.add(user)
            Like=True
        data={
            "liked":Like,
            "likes_count":w.likes.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect(reverse("video_watch", args=[str(id)]))
# class blogDetailView(DetailView):
#     model = Post
#     template_name = "blog-detail.html"

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    fields = ['title','discription','image', 'image2','video_url','categories','featured','slug']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

def dashbord(request):
    return render(request, 'dashbord/index.html')


def company(request):
    return render(request, 'about/company.html')



def services(request):
    return render(request, 'about/marketing-services.html')



def privacy(request):
    return render(request, 'privacy.html')



def tos(request):
    return render(request, 'tos.html')



def portfolio(request):
    return render(request, 'about/artists/portfolio.html')



def sellguds(request):
    return render(request, 'about/artists/sell-goods.html')



def learning(request):
    return render(request, 'about/artists/learning.html')


def guides(request):
    return render(request, 'guides.html')


def websitebuilder(request):
    return render(request, 'about/artists/website-builder.html')


def signup(request):
    return render(request, 'registration/signup.html')


def contest(request):
    return render(request, 'contests.html')


def search(request):
    item = Item.objects.all()
    query = request.GET.get('q')
    if query:
        queryset = item.filter(
            Q(title__icontains=query) |
            Q(description__icontains=query)
        ).distinct()
    context={
        'queryset':queryset
    }
    return render(request, 'search.html', context)




@login_required
def liked_video(request, id):
    user=request.user
    Like=False
    if request.method=="POST":
        video_id=request.POST['video_id']
        get_video=get_object_or_404(Post, id=video_id)
        w=Post.objects.get(id=video_id)
        if user in w.likes.all():
            w.likes.remove(user)
            Like=False
        else:
            w.likes.add(user)
            Like=True
        data={
            "liked":Like,
            "likes_count":w.likes.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect(reverse("video_watch", args=[str(id)]))




@login_required
def dislike_video(request, id):
    user=request.user
    Dislikes=False
    if request.method == "POST":
        video_id=request.POST['video_id']
        print("printing ajax id", video_id)
        watch=get_object_or_404(Post, id=video_id)
        # w=Post.objects.get(id=video_id)
        if user in watch.dislikes.all():
            watch.dislikes.remove(user)
            Dislikes=False
        else:
            if user in watch.likes.all():
                watch.likes.remove(user)
            watch.dislikes.add(user)
            watch.save()
            Dislikes=True
        data={
            "disliked":Dislikes,
            # 'dislike_count':watch.dislikes.all().count()
            'dislike_count':watch.dislikes.all().count()
        }
        return JsonResponse(data, safe=False)
    return redirect(reverse("video_watch", args=[str(id)]))



def list_category(request, slug):
    categories = categor.objects.all()
    post = Item.objects.all()
    if slug:
        category = get_object_or_404(categor, slug=slug)
        post = post.filter(category=category)
    template = "category.html"
    context = {
        'categories': categories,
        'post': post,
        'category': category,
    }
    return render(request, template, context)



def list_tags(request, slug):
    categories = categor.objects.all()
    tags = Tags.objects.all()
    post = Item.objects.all()
    if slug:
        tag = get_object_or_404(Tags, slug=slug)
        post = post.filter(tag=tag)
    template = "tags.html"
    context = {
        'tags': tags,
        'post': post,
        'tag': tag,
        'cat': categories,
    }
    return render(request, template, context)



def pictures_details(request, id):
    post_all = picture.objects.all()
    post = get_object_or_404(picture, id=id)

    # PostView.objects.get_or_create(user=request.user, post=post)
    context = {
        "post":post,
        'post_all':post_all,
        # 'trend':trend,
    }
    return render(request,'pictures_details.html', context)


def job_details(request, id):
    post_all = picture.objects.all()
    post = get_object_or_404(picture, id=id)

    # PostView.objects.get_or_create(user=request.user, post=post)
    context = {
        "post":post,
        'post_all':post_all,
        # 'trend':trend,
    }
    return render(request,'pictures_details.html', context)



class job_details(DetailView):
    
    def get(self, request, id):
        post_all = Studios.objects.all()
        post = get_object_or_404(Jobs, id=id)
        users_post = None
        if self.request.user == None:
                
            users_post = post
        else:
            users_post = Jobs.objects.filter(user=self.request.user)
        for post in users_post:
            print(post.title)
        myposts = [] 

        posts = get_object_or_404(Studios, id=id)   
        # PostView.objects.get_or_create(user=request.user, post=post)
        context = {
            "post":posts,
            'post_all':post_all,
            'mypost':users_post,
            # 'trend':trend,
        }
        return render(request,'jobs/c/343-industries.html', context)


def podcast(request):
     podcast = Podcast.objects.order_by('-timestamp')
     podcasts = Podcast.objects.filter(featured=True)[0:1]
     context = {
        "pod":podcast,
        "pods":podcasts,
     }
     return render(request, 'podcast.html', context)



def magazin(request):
     magazing = mag.objects.all()
     magazin = mag.objects.order_by('-timestamp')[0:5]
     magazins = [mag.objects.filter(featured=True).first()]
     magazings = mag.objects.filter(featured=True)[1:3]
     context = {
        "magazins":magazins,
        "magazin":magazin,
        "magazing":magazing,
        "magazings":magazings,
     }
     return render(request, 'magazin.html', context)

# url = "https://api.paystack.co/transaction/verify/%s" % (trans_ref)
# 	rec = requests.request('GET',url,headers={'Authorization':'Bearer sk_live_8b0faf614d85452fe4022c08f96489a2d516259d'})
# 	data = rec.json()



#     # r = requests.get("http://50.21.183.64:8069/web/json/website.support.ticket")
#     url = "http://50.21.183.64:8069/web/json/website.support.ticket"
#     header = {'Authorization':'Basic YWJjQGVudWd1ZGlzY28uY29tOkVudWd1ZGlzY29AMzMz','Content-type':'application/json'}
#     rec = requests.get('GET',url,header)
#     data = rec.json()
#     # header = {'Authorization':'Basic YWJjQGVudWd1ZGlzY28uY29tOkVudWd1ZGlzY29AMzMz','Content-type':'application/json'}  
#     # print(dir(r)) 

def api(request):
	rec = None
	if request.method == 'POST':
		url = "http://50.21.183.64:8069/web/json/website.support.ticket"
		header = {'Authorization':'Basic YWJjQGVudWd1ZGlzY28uY29tOkVudWd1ZGlzY29AMzMz','Content-type':'application/json'}
		name = request.POST.get('name')
		phone_number = request.POST.get('phone_number')
		account_num = request.POST.get('account_num')
		email = request.POST.get('email')
		priority = request.POST.get('priority')
		category_of_issue = request.POST.get('category_of_issue')
		description = request.POST.get('description')
		state = request.POST.get('state')
		street = request.POST.get('street')
		channel = request.POST.get('channel')
		subject = request.POST.get('subject')

		data = { "params": 
				   { "name": name,
					 # "create_date": datetime.datetime.now,
					 "cus_phone": phone_number,
					 "acc_no": request.session['acc_no'],
					 "acc_type": request.session['metering_type'],
					 "email": request.session['email'],
					 "state": state,
					 "priority_id": priority,
					 "category": category_of_issue,
					 "description": description,
					 "ticket_number_ems": "PI1641215",
					 "cus_street": street,
					 "created_by": "James",
					 "acc_name": request.session['name'],
					 "call_count": 1,
					 "channel": channel,
					 "subject": subject 
					 } }
		rec = requests.post(url,headers=header,json=data)
		# rec.save()
		# messages.success(request, "Successfully!")
		# return redirect('/suport_ticket')
		print(rec.text)
	# 	data = rec.json()
	# 	if "result" in data.keys():
	# 		if "Success" in data['result'].keys():
	# 			return {'message':'success'}
	# 		else:
	# 			return {'message': 'failed'}
	# 	else:
	# 		return {'message': 'failed'}
	context = {
		"rec": rec,
		"metering_type": request.session['metering_type']
	}
	return render(request, 'api.html',context)