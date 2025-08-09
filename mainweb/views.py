from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


def user_login(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(request, username=email, password=password)

        if user is not None:

            login(request, user)
            domain = email.split('@')[-1]

            if domain == 'employee.gmail.com':
                messages.success(request, f'Welcome, Employee {user.username}!')
                return redirect('employee_section')
            else:

                messages.success(request, f'Welcome, {user.username}!')
                return redirect('buyer_section')
        else:
            messages.error(request, 'Invalid email or password.')
    return render(request, 'user_login.html')

def erp_dashboard(request):
        return render(request, 'employeedashboard.html')