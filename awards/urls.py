from django.conf.urls import url 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url('^$', views.index, name='index'),
    url('project/new/', views.create_project, name = 'new-project'),
    url('profile/new/', views.create_profile, name = 'new-profile'),
    url('accounts/profile/(?P<username>[-_\w.]+)$', views.profile, name= 'profiles'),
    url('profiles/upvote/(\d+)', views.like_project, name="like_post"),
    url('profiles/downvote/(\d+)', views.dislike_project, name="dislike_post"),
    url('api/profile/', views.ProfileList.as_view()),
    url('api/project/', views.ProjectList.as_view()),

]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)