from django.shortcuts import render, redirect, HttpResponse
from .models import *

# Create your views here.
def index(request):
    return redirect('/shows')

def shows(request):
    context ={
        'shows': Show.objects.all().order_by('-release_date')
    }
    return render(request, 'tv_show_app/all_shows.html', context)

def new(request):
    return render(request, 'tv_show_app/add_show.html')

def new_show(request):    
    if request.method == 'GET':
        return redirect("/new")
    else:
        if request.method == 'POST':
            title = request.POST['title']
            network = request.POST['network']
            release_date = request.POST['release_date']
            description = request.POST['description']

            obj_new =Show.objects.create(title=title, network=network, release_date=release_date, description=description)
            obj_new.save()
        return redirect(f'/shows/{obj_new.id}')

def info_show(request, show_id):
    context = {
        'show_info': Show.objects.get(id=show_id)
    }
    return render(request, 'tv_show_app/info_show.html', context)

def edit_show(request, show_id):
    context = {
        'show_info': Show.objects.get(id=show_id)
    }
    return render(request, 'tv_show_app/edit_show.html', context)

def updated_show(request, show_id):
    if request.method == 'GET':
        return redirect("/new")
    else:
        if request.method == 'POST':
            new_title = request.POST['title']
            new_network = request.POST['network']
            new_release_date = request.POST['release_date']
            new_description = request.POST['description']

            show =Show.objects.get(id=show_id)
            show.title = new_title
            show.description = new_description
            show.network = new_network
            show.release_date = new_release_date
            show.save()

            return redirect(f'/shows/{show.id}')  

def delete_show(request, show_id):
    show_info = Show.objects.get(id=show_id)
    show_info.delete()
    return redirect('/shows')            

