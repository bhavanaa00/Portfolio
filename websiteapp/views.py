from django.shortcuts import render
from django.http import HttpResponse

from .models import *

# Create your views here.
def web(request):
  if request.method == 'POST':
    name = request.POST['name']
    email = request.POST['email']
    message = request.POST['message']
    new_user = formdata(name=name,email=email,message=message)
    new_user.save()

  else:
    hs = home.objects.all()
    skill = skills.objects.all()
    projects = project.objects.order_by('-id')[:3] 
    works = work.objects.all()
    abouts = about.objects.all()
    contacts = contact.objects.all()

  context = {
    'home':hs,
    'skills':skill,
    'project':projects,
    'work':works,
    'about':abouts,
    'contact':contacts
  }
    
  return render(request, "index.html",context)

def project_view(request):
  all_projects = project.objects.all().order_by('-id')

  return render(request, "projects.html", {'allprojects':all_projects})




