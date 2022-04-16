from django.shortcuts import render,redirect
from django.urls import reverse
from .form import ApplyForm,AddForm
from .models import job,applicant
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from .filters import JobFilter


# Create your views here.


def job_list(request):
    job_list = job.objects.all()

    ## filters
    myfilter = JobFilter(request.GET,queryset=job_list)
    job_list = myfilter.qs

    #Pagination
    paginator = Paginator(job_list, 3) # Show 5 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)


    context = {'jobs':page_obj , 'myfilter' : myfilter}
    
    return render(request,'jobs/job_list.html',context)


#job details
def job_detail(request,slug):
    job_detail = job.objects.get(slug=slug)

    if request.method=='POST': #if i click submit button (apply):
        form = ApplyForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.applied_job = job_detail
            myform.save()

    else:
        form = ApplyForm()


    context = {'job_detail': job_detail, 'jobdetailform': form }
    return render(request,'jobs/job_detail.html',context)


@login_required
def add_job(request):
    if request.method=='POST':
        form = AddForm(request.POST , request.FILES)
        if form.is_valid():
            myform = form.save(commit=False)
            myform.owner = request.user
            myform.save()
            return redirect(reverse('jobs:job_list'))

    else:
        form = AddForm()

    return render(request,'jobs/add_job.html',{'addjobform':form})