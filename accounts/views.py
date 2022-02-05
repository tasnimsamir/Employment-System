from django.shortcuts import redirect, render
from .form import SignupForm , UserForm , ProfileForm
from django.contrib.auth import authenticate, login
from .models import Profile
from django.urls import reverse
from django.core.paginator import Paginator
from jobs.models import applicant, job
from accounts.utils import match
# Create your views here.
# The data of the user is divided into two tables: users & profile, so we deal with 2 forms 

def signup(request):
    if request.method=="POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request,user)
            return redirect('/accounts/profile')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html',{'signupform':form})



def profile(request):
    profile = Profile.objects.get(user=request.user)
    return render(request,'accounts/profile.html',{'profile': profile})



def profile_edit(request):
    profile = Profile.objects.get(user=request.user)

    if request.method=='POST':
        userform = UserForm(request.POST,instance=request.user)
        profileform = ProfileForm(request.POST,request.FILES,instance=profile )
        if userform.is_valid() and profileform.is_valid():
            userform.save()
            myprofile = profileform.save(commit=False)
            myprofile.user = request.user
            # myprofile.applicant = Profile.applicant.get(user = request.user)
            myprofile.save()
            return redirect(reverse('accounts:profile'))

    else :
        userform = UserForm(instance=request.user)
        profileform = ProfileForm(instance=profile)

    return render(request,'accounts/profile_edit.html',{'userform':userform , 'profileform':profileform})


def My_jobs(request):
    my_job = job.objects.filter(owner = request.user)
    #Pagination
    paginator = Paginator(my_job, 6) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request,'accounts/myjobs.html',{'myjob':page_obj})

def Browse_applicants(request,slug):
    applied_job = job.objects.get(slug=slug)
    applicants = applicant.objects.filter(applied_job = applied_job)

    #Pagination
    paginator = Paginator(applicants, 3) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    return render(request,'accounts/appliedAplicants.html',context={'profile_applicant': page_obj})


def Best_candidites(request,slug):
    score = []
    threshold = 0.99
    applied_job_description = job.objects.values_list('description',flat=True).get(slug=slug)
    all_applicants_bio = applicant.objects.values_list('id','biography')
    for bio in all_applicants_bio:
        bio_id = bio[0]
        bio_txt = bio[1]
        score.append((bio_id,match(applied_job_description,bio_txt)[0][0]))
    print(score)

    best_ids = [x[1] for x in score if x[1] >= threshold]
    print(best_ids)
    best_cand = applicant.objects.filter(pk__in = best_ids)

    #Pagination
    paginator = Paginator(best_cand, 5) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request,'accounts/BestCandidates.html',{'bst_candidates':page_obj})