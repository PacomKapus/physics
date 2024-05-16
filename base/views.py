from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
from .forms import SignUpForm,UploadFileForm, UploadFileForm2, UploadFileForm3 ,UploadFileForm4, UploadFileForm5 , CommentForm
from django.contrib.auth import login, logout
from django.contrib.auth.hashers import  check_password
from django.contrib import messages
from .models import UploadedFile , UploadedFile2 , UploadedFile3 ,UploadedFile4 , UploadedFile5 , Comment
from datetime import datetime
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.urls import reverse
from django.http import HttpResponseForbidden, HttpResponseNotAllowed


@login_required(login_url='login')
def Base(request):
    today_date = datetime.now().date()
    comments = Comment.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.save()
            return redirect(request.get_full_path() + '#comments-section')
    else:
        form = CommentForm()
    return render(request, 'base.html', {'form': form, 'comments': comments,'today_date': today_date})

def delete_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        comment.delete()
    return redirect('base')

def Login(request):
    error = ""
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = User.objects.get(email=email)
            if check_password(password, user.password):
                login(request, user)
                return redirect('base')
            else:
                messages.error(request, 'Email or Password is incorrect')
                return redirect('login')
        except User.DoesNotExist:
            messages.error(request, 'Email or Password is incorrect')
            return redirect('login')

    return render(request, 'login.html', {'error': error})

def Signup(request):
    form = SignUpForm()
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            user = form.save()
            login(request, user)
            return redirect('/base')
    return render(request, 'signup.html', {'form': form})

def SignOut(request):
    logout(request)
    return redirect('login')

def Profile(request):
    return render(request, 'profile.html')

def page1_view(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('page1')  # перенаправление на ту же страницу для обновления
    else:
        form = UploadFileForm()
    files = UploadedFile.objects.filter(user=request.user)
    return render(request, 'page1.html', {'form': form, 'files': files})

def page2_view(request):
    if request.method == 'POST':
        form = UploadFileForm2(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('page2')  # перенаправление на ту же страницу для обновления
    else:
        form = UploadFileForm2()
    files = UploadedFile2.objects.filter(user=request.user)
    return render(request, 'page2.html', {'form': form, 'files': files})

def page3_view(request):
    if request.method == 'POST':
        form = UploadFileForm3(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('page3')  # перенаправление на ту же страницу для обновления
    else:
        form = UploadFileForm3()
    files = UploadedFile3.objects.filter(user=request.user)
    return render(request, 'page3.html', {'form': form, 'files': files})

def page4_view(request):
    if request.method == 'POST':
        form = UploadFileForm4(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('page4')  # перенаправление на ту же страницу для обновления
    else:
        form = UploadFileForm4()
    files = UploadedFile4.objects.filter(user=request.user)
    return render(request, 'page4.html', {'form': form, 'files': files})

def page5_view(request):
    if request.method == 'POST':
        form = UploadFileForm5(request.POST, request.FILES)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            return redirect('page5')  # перенаправление на ту же страницу для обновления
    else:
        form = UploadFileForm5()
    files = UploadedFile5.objects.filter(user=request.user)
    return render(request, 'page5.html', {'form': form, 'files': files})

@login_required
def toggle_like(request, comment_id):
    comment = Comment.objects.get(pk=comment_id)
    user = request.user

    if user in comment.likes.all():
        comment.likes.remove(user)
    else:
        comment.likes.add(user)

    base_url = reverse('base') + '#comments-section'
    return redirect(base_url)

def delete_file(request, file_id):
    file_to_delete = get_object_or_404(UploadedFile, pk=file_id)
    
    if file_to_delete.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this file.")

    file_to_delete.delete()
    # После удаления перенаправляем пользователя на страницу, с которой он пришел
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    # Если HTTP_REFERER не найден, перенаправляем на главную страницу или другую страницу по вашему выбору
    return redirect('baseline')

def delete_file2(request, file_id):
    file_to_delete = get_object_or_404(UploadedFile2, pk=file_id)
    
    if file_to_delete.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this file.")

    file_to_delete.delete()
    
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    
    return redirect('baseline')

def delete_file3(request, file_id):
    file_to_delete = get_object_or_404(UploadedFile3, pk=file_id)
    
    if file_to_delete.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this file.")

    file_to_delete.delete()
    
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    
    return redirect('baseline')

def delete_file4(request, file_id):
    file_to_delete = get_object_or_404(UploadedFile4, pk=file_id)
    
    if file_to_delete.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this file.")

    file_to_delete.delete()
    
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    
    return redirect('baseline')


def delete_file5(request, file_id):
    file_to_delete = get_object_or_404(UploadedFile5, pk=file_id)
    
    if file_to_delete.user != request.user:
        return HttpResponseForbidden("You don't have permission to delete this file.")

    file_to_delete.delete()
    
    referer = request.META.get('HTTP_REFERER')
    if referer:
        return redirect(referer)
    
    return redirect('baseline')