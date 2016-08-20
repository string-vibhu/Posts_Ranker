from django.shortcuts import render
from django.http import HttpResponse
import os
from .models import Post
from datetime import datetime
import random
from django.db.models import F
from datetime import timedelta
from django.db.models import Max
from django.utils import timezone
from math import exp

# Create your views here.
def load_posts(request):
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'Data/data.txt')
	file=open(file_path)
	filedata=file.read()
	posts=filedata.split('#')
	i=1
	d=5
	for p in posts:
		post=p.split('$')
		title=post[0]
		content=post[1]
		if i==21:
			d=d-1
			i=1
		a=Post(title=title, text=content,date=(datetime.now()-timedelta(days=d)))
		a.save()
		i=i+1

	init_count()
	#calc_rank()
	post_ranking()
	posts=Post.objects.all().order_by("-rank")
	return render(request, 'ranking_algo/post.html', {'posts_data': posts})

def load_posts_today(request):
	module_dir = os.path.dirname(__file__)  # get current directory
	file_path = os.path.join(module_dir, 'Data/data1.txt')
	file=open(file_path)
	filedata=file.read()
	posts=filedata.split('#####')
	for p in posts:
		post=p.split('$$$$$')
		title=post[0]
		content=post[1]
		a=Post(title=title, text=content,date=(datetime.now()))
		a.save()
	update_count()
	post_ranking()
	posts=Post.objects.all().order_by("-rank")
	return render(request, 'ranking_algo/post.html', {'posts_data': posts})
	
def init_count():
    #all_post = Post.Objects.all()
    today_date = datetime.now().date()
    #p4 = Post.Objects.filter(date__date='2016-08-13')
    for i in range(1,6):
        p = Post.objects.filter(date__date = today_date - timedelta(days=i))

        for p1 in p:

          x1 = random.randint(i*10, 200)

          if random.randint(0, 1):
            a = random.uniform(8, 10)	#for authentication
            f = random.uniform(0, 3)	#for fake
            r = random.uniform(3, 5)	#for Rating
            c = random.uniform(0, 4)	#for comment
            s = random.uniform(1, 2)
          else :
            a = random.uniform(0, 5)
            f = random.uniform(6, 9)
            r = random.uniform(0, 3)
            c = random.uniform(0, 4)
            s = random.uniform(0, 0.5)
          p1.auth_count = x1*a
          p1.fake_count = x1*f
          p1.rating = r
          p1.comment_count = x1*c
          p1.share_count=x1*s
          p1.save()
	
def update_count():
    today_date = datetime.now().date()

    for i in range(0,5):
        p = Post.objects.filter(date__date = today_date - timedelta(days=i))


        for p1 in p:

          x1 = random.randint(0, 10-2*i)

          if random.randint(0, 1):
            a = random.randint(8, 10)
            f = random.randint(0, 3)
            r = random.randint(3, 5)
            c = random.randint(0, 4)
            s = random.uniform(1, 2)
          else :
            a = random.randint(0, 5)
            f = random.randint(6, 9)
            r = random.randint(0, 3)
            c = random.randint(0, 4)
            s = random.uniform(0, 0.5)

          p1.auth_count = p1.auth_count+x1*a
          p1.fake_count = p1.fake_count+x1*f
          p1.rating = (p1.rating + r)/2
          p1.comment_count = p1.comment_count + x1*c
          p1.share_count=p1.share_count+x1*s
          p1.save()




def post_ranking():
  #today_date=datetime.now()
  #print today_date
  post = Post.objects.all().order_by("id")
  maxauth = Post.objects.aggregate(Max('auth_count'))
  maxfake = Post.objects.aggregate(Max('fake_count'))
  maxrating = Post.objects.aggregate(Max('rating'))
  maxcomment = Post.objects.aggregate(Max('comment_count'))
  maxshare = Post.objects.aggregate(Max('share_count'))
  if maxauth>maxfake :
    maxfactor = maxauth
  else :
    maxfactor = maxfake

  for single_post in post:
    posted_time = single_post.date
    authentication_count = single_post.auth_count
    fakes_count = single_post.fake_count
    rating_count = single_post.rating
    comments_count = single_post.comment_count
    shares_count = single_post.share_count
    timedifference = timezone.now() - posted_time
    timedifference = timedifference.total_seconds()/60
    timefactor = timedifference -1
    Rank = (((authentication_count - pow(1.001,fakes_count)*fakes_count)/maxfactor.values()[0])*(1.0/6.0) + (float(rating_count)/float(maxrating.values()[0]))*(1.0/6.0) + (float(comments_count)/float(maxcomment.values()[0]))*(1.0/6.0) + (float(shares_count)/float(maxshare.values()[0]))*(1.0/6.0))*(float(2880**2)/(timefactor**2+float(2880**2)))
    single_post.rank=Rank
    single_post.save()
