from django.conf.urls import url
from . import views

app_name='ranking_algo'
urlpatterns = [
	url(r'^upload_posts/$',views.load_posts,name='load_posts'),
	url(r'^upload_todays_posts/$',views.load_posts_today,name='load_today'),
	url(r'^get_posts/$',views.calc_rank,name='get_posts'),
]