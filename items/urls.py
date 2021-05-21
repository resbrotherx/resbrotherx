from django.urls import path
from django.urls.conf import include
from . import views
from .views import ( PostCreateView,job_details)

app_name = 'items'

urlpatterns = [
    path('', views.test),
    path('about/', views.about, name="about"),
    path('subscription/', views.sub, name="sub"),
    path('learning/', views.len, name="len"),
    path('marketplace/', views.mar, name="mar"),
    path('new_item/', views.new_item, name="new_item"),
    path('jobs/', views.job, name="job"),
    path('blogs/', views.blog, name="blog"),
    path('latest/', views.latest, name="latest"),
    
    path('contest/', views.contest, name="contest"),
    path('item_detail/<id>/', views.item_detail, name="item_detail"),
    path('create/new/', PostCreateView.as_view(), name='create'),
    path('blog_detail/<id>/', views.blog_detail, name='blog_detail'),
    path('dashbord/', views.dashbord, name="dashbord"),
    path('signup/', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('search/', views.search, name="search"),
    path('about/company/', views.company, name="company"),
    path('about/services/', views.services, name="services"),
    path('privacy/', views.privacy, name="privacy"),
    path('tos/', views.tos, name="tos"),
    path('portfolio/', views.portfolio, name="portfolio"),
    path('sell-goods/', views.sellguds, name="sellguds"),
    path('learning/', views.learning, name="learning"),
    path('website-builder/', views.websitebuilder, name="websitebuilder"),
    path('guides/', views.guides, name="guides"),
    path("likes/<id>/", views.liked_post, name="like-post"),
    path("like/<id>/", views.liked_video, name="like-video"),
    path("dislike/<id>/", views.dislike_video, name="dislike-video"),
    path('list_category/<slug>/', views.list_category, name='list_category'),
    path('list_tags/<slug>/', views.list_tags, name='list_tags'),
    # path('pictures/', views.pictures, name='pictures'),
    path('pictures_details/<id>/', views.pictures_details, name='pictures_details'),

    path('podcast', views.podcast, name='podcast'),
    path('magazin', views.magazin, name='magazin'),
    path('api', views.api, name='api'),
    path('job_details/<id>/', job_details.as_view(), name='job_details'),

]