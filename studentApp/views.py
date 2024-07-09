from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from.models import Profile, Result, SchoolItem
from django.http import HttpResponse



def admin_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None and user.is_staff:
            login(request, user)
            return redirect('custom_admin_login')
        else:
            return render(request, 'admin_login.html', {'error_message': 'Invalid credentials'})
    
    return render(request, 'admin_login.html')

@user_passes_test(lambda u: u.is_superuser)
def custom_admin_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('/admin/')
        else:
            return HttpResponse('<h1>Invalid Credentials</h1><p>Username or password is incorrect.</p>')
    else:
        form = AuthenticationForm()
    return render(request, 'students/custom_admin_login.html', {'form': form})

@user_passes_test(lambda u: u.is_superuser)
def custom_admin_logout(request):
    logout(request)
    return redirect('home')

def home(request):
    return render(request, 'students/home.html')
@login_required
def profile(request):
    user_profile = request.user.profile
    user_results = Result.objects.get(user=request.user)
    results = {
        'math': user_results.math,
        'english': user_results.english,
        'science': user_results.science,
        'biology': user_results.biology,
        'irs': user_results.irs,
    }
    context = {
        'profile': user_profile,
        'results': results,
    }
    return render(request, 'students/profile.html', context)


@login_required
def school_items(request):
    items = SchoolItem.objects.all()
    query = request.GET.get('q')
    if query:
        items = items.filter(name__icontains=query)
    return render(request, 'students/school_items.html', {'items': items, 'query': query})
