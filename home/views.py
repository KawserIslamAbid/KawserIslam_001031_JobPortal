from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import *
from .models import *

# Create your views here.
def home(request):
    return render(request, 'home/home.html')

@login_required(login_url='login/')
def add_job(request):
    form = JobForm()
    if request.method =='POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('home')
    return render(request, 'job/add_job.html', {'form': form})


def job_list(request):
    job = Job.objects.all()
    return render(request, 'job/job_list.html', {'job': job})


def apply_job(request, pk):
    job = get_object_or_404(Job, pk=pk)
    form = ApplyJobForm(initial={'job': job})
    
    if request.method == 'POST':
        form = ApplyJobForm(request.POST, initial={'job': job})
        if form.is_valid():
            job_apply = form.save(commit=False)
            job_apply.user = request.user
            job_apply.save()
            return redirect('job_list')
    
    return render(request, 'job/job_apply.html', {'job': job, 'form': form})


def apply_job_list(request):
    job = Apply_Job.objects.filter(user=request.user)
    return render(request, 'job/apply_job_list.html', {'job': job})

def profile(request):
    return render(request, 'profile/profile.html')
