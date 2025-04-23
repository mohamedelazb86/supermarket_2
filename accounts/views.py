from django.shortcuts import render


def signup(request):
    return render(request,'accounts/signup.html',{})

def activate_code(request):
    return render(request,'accounts/activate_code.html',{})