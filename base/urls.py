from django.contrib import admin
from django.urls import path,include
from . import views
from .views import page1_view, page2_view, page3_view, page4_view, page5_view,delete_file

urlpatterns = [
    path('',views.Base,name='base'),
    path('login/',views.Login,name='login'),
    path('signup/',views.Signup,name='signup'),
    path('signout/',views.SignOut,name='signout'),
    path('profile/',views.Profile,name='profile'),
    
    path('page1/', page1_view, name='page1'),
    path('page2/', page2_view, name='page2'),
    path('page3/', page3_view, name='page3'),
    path('page4/', page4_view, name='page4'),
    path('page5/', page5_view, name='page5'),
    path('delete_file/<int:file_id>/', views.delete_file, name='delete_file'),
    path('delete_file2/<int:file_id>/', views.delete_file2, name='delete_file2'),
    path('delete_file3/<int:file_id>/', views.delete_file3, name='delete_file3'),
    path('delete_file4/<int:file_id>/', views.delete_file4, name='delete_file4'),
    path('delete_file5/<int:file_id>/', views.delete_file5, name='delete_file5'),
    
    
    path('delete-comment/<int:comment_id>/',views.delete_comment, name='delete_comment'),
    path('comment/<int:comment_id>/toggle_like/',views.toggle_like, name='toggle_like'),
]