from django.urls import path
from notes import views

urlpatterns = [
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('signup/',views.signup,name='signup'),
    path('logout/',views.logout,name='logout'),
    path('add_note/',views.add_note,name='add_note'),
    path('about/',views.about,name='about'),
    path('edit_note/<str:pk>/',views.edit_note,name='edit_note'),
    path('delete_note/<str:pk>/',views.delete_note,name='delete_note'),
]
