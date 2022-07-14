from django.shortcuts import redirect, render
from . forms import UserRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Congratulation! Account has been created successfully for {username}, now login again')
            return redirect('login') #name = 'register' in urls.py
    else:
        form  = UserRegisterForm()
    return render(request, 'users/register.html', {'form':form})
