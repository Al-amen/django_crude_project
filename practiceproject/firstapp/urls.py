from django.urls import path
from firstapp import views

app_name = 'firstapp'
urlpatterns = [
    path("",views.index,name = "index" ),

    path('addmusician/',views.musician_form, name = 'musicianform'),
    path('addalbumb/', views.albumb_form, name='albumbform'),
    path('albumblist<int:artist_id>/',views.albumb_list,name='albumblist'),
    path('edit_artist<int:artist_id>/',views.edit_artist,name='edit_artist'),
    path('edit_albumb<int:albumb_id>/',views.edit_albumb, name='edit_albumb'),
    path('delete_albumb<int:albumb_id>/',views.delete_albumb, name='delete_albumb'),
    path('delete_artist<int:artist_id>/',views.delete_artist, name='delete_artist'),


    
]
 