from django.shortcuts import render, get_object_or_404

from firstapp import forms

from firstapp import models
from django.db.models import Avg


def index(request) :
    musician_list = models.Musician.objects.order_by('first_name')
    
    diction = {'title':'Home page',"musician_list":musician_list}
    
    return render(request, 'firstapp/index.html', context = diction)
             

def albumb_list(request, artist_id):
    musician_info = models.Musician.objects.get(pk=artist_id)
    albumb_list = models.Album.objects.filter(artist_id=artist_id).order_by('name','relase_date')
    artist_rating = models.Album.objects.aggregate(Avg('nums_strs'))
    diction = {'title' : 'albumb_list' , 'musician_info':musician_info, 'albumb_list':albumb_list,"artist_rating":artist_rating}
    return render(request, 'firstapp/albumblist.html' ,context=diction)

def musician_form(request):
    new_form = forms.MusicianForm()
    
    diction = {'title':'Add Musician', 'new_form': new_form}
    
            
    if request.method == "POST":
        new_form = forms.MusicianForm(request.POST)
                   
        if new_form.is_valid():
            
            new_form.save(commit=True)
            return index(request)
            
    return render(request, 'firstapp/musicianform.html', context=diction)

def albumb_form(request):
    new_form = forms.AlbumbForm()
    
    diction = {'title': 'Add alabumb' ,"new_form":new_form}
    
    if request.method == "POST":
        new_form = forms.AlbumbForm(request.POST)
        new_form.save(commit=True)
        return index(request)
            
    
    return render(request,'firstapp/alabumform.html',context=diction)
    

def edit_artist(request,artist_id):
    artist_info = models.Musician.objects.get(pk=artist_id)
    form = forms.MusicianForm(instance=artist_info)
   
    if request.method == "POST":
        form = forms.MusicianForm(request.POST,instance=artist_info)
        
        if form.is_valid():
            form.save(commit=True)
            return albumb_list(request,artist_id)
    diction = {'form':form, 'artist_id':artist_id}
    return render(request, 'firstapp/edit_artist.html',context=diction)

def edit_albumb(request, albumb_id):
    albumb_info = models.Album.objects.get(pk=albumb_id) 
    form = forms.AlbumbForm(instance=albumb_info)
    diction = {'edit_form': form}
    if request.method == "POST":
        form = forms.AlbumbForm(request.POST,instance=albumb_info)  # Correctly pass request.POST and request.FILES
        if form.is_valid():
            form.save(commit=True)
            diction.update({"success_text": "Successfully updated", "edit_form": form})
            
        
    
    diction.update({'albumb_id':albumb_id})
    
    
    return render(request, 'firstapp/edit_albumb.html', context=diction)

def delete_albumb(request, albumb_id):
    albumb = models.Album.objects.get(pk=albumb_id).delete()
    diction = {"delete_message":"Albumb delete Sucessfully"}
    
    return render(request,'firstapp/delete.html',context=diction)

def delete_artist(request, artist_id):
    artist = models.Musician.objects.get(pk=artist_id).delete()
    diction = {"delete_message": "Artist delete successfully"}
    
    return render(request, 'firstapp/delete.html',context=diction)