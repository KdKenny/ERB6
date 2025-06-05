from django.shortcuts import render , redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from .forms import UserUpdateForm, PasswordChangingForm
from contacts.models import Contact

# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, 'Username already exists !')
                return redirect('accounts:register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'Email already exists !')
                    return redirect('accounts:register')
                else:
                    user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, "Account created successfully !")
                    return redirect('accounts:login')
        else:
            messages.error(request, 'Password do not match !')
            return redirect('accounts:register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username,password=password)
        if user is not None:
            auth.login(request,user)
            messages.success(request,"You are now logged in !")
            return redirect('accounts:dashboard')
        else:
            messages.error(request,"Invalid credentials !")
            return redirect('accounts:login')
    else :
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect("pages:index")

@login_required
def dashboard(request):
    user_form = UserUpdateForm(instance=request.user)
    password_form = PasswordChangingForm(request.user)
    contacts = Contact.objects.filter(user_id=request.user.id)
    context = {
        'user_form': user_form,
        'password_form': password_form,
        'contacts': contacts
    }
    return render(request, 'accounts/dashboard.html', context)

@login_required
def update_profile(request):
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('accounts:dashboard')
    else:
        form = UserUpdateForm(instance=request.user)
    return render(request, 'accounts/update_profile.html', {'form': form})

@login_required
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangingForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Your password was successfully updated!')
            return redirect('accounts:dashboard')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = PasswordChangingForm(request.user)
    return render(request, 'accounts/change_password.html', {'form': form})
