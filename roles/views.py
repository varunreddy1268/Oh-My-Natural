from django.shortcuts import render, redirect
from roles.models import CreateTable


# Create your views here.
def register_user(request):
    if request.method == 'POST':
        f_name = request.POST.get('first_name')
        l_name = request.POST.get('last_name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        cs = CreateTable()
        user = cs.insert_user(f_name, l_name, email, password)
        return redirect('/')
    return render(request, 'signup.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        cs = CreateTable()
        valid = cs.check_login(email, password)
        if valid:
            request.session['user_id'] = valid[0]
            return redirect('/dashboard')
    return render(request, 'login.html')


def all_flights(request):
    if request.method == 'POST':
        cs = CreateTable()
        flights = cs.all_flights()
        return render(flights)