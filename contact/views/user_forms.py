from django.shortcuts import render, redirect
from django.contrib import messages
from contact.forms import RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User registered successfully')
            return redirect('contact:index')

        else:
            messages.error(request, 'Error.')

    return render(
        request,
        'contact/register.html',
        {
            'form': form
        }
    )