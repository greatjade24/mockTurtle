from django.shortcuts import render, redirect

# Create your views here.

def myPage(request):
    return render(request, 'mypage/mypage.html');

def test(request):
    return render(request, 'mypage/codetest.html');
