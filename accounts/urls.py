from django.urls import include, path

from . import views

app_name='accounts'

urlpatterns = [
    path('signup',views.signup , name='signup'),
    path('profile/',views.profile , name='profile'),
    path('profile/edit',views.profile_edit , name='profile_edit'),
    path('profile/myjobs/<str:slug>/applicants',views.Browse_applicants , name='applied_applicants'),
    path('profile/myjobs/<str:slug>/bestcandidates',views.Best_candidites , name='best_candidates'),
    path('profile/myjobs',views.My_jobs , name='myjobs'),

]