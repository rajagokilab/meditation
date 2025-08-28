from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


def home(request):
    return render(request, 'home.html')

# views.py
from django.shortcuts import render


def about(request):
    return render(request, 'about.html')

def meditation(request):
    return render(request, 'meditation.html')

from django.shortcuts import render
from .forms import ContactForm

def contact_view(request):
    success = False
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # process the form (save to DB, send email, etc.)
            print(form.cleaned_data)  # <-- For now just print to console
            success = True
            form = ContactForm()  # Reset form after successful submission
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form, "success": success})


from django.shortcuts import render

def therapy(request):
    return render(request, 'therapy.html')

# views.py
def therapy_detail(request, therapy_type):
    return render(request, 'therapy_detail.html', {'therapy_name': therapy_type})


from django.shortcuts import render

from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib import messages

from django.shortcuts import render, redirect
from django.contrib import messages

def approach_form(request):
    therapy_title = request.GET.get('title', 'Therapy Approach Form')

    if request.method == "POST":
        # Collect form data
        first_name = request.POST.get('firstName')
        last_name = request.POST.get('lastName')
        mobile = request.POST.get('mobileNo')
        email = request.POST.get('emailId')
        therapy_day = request.POST.get('therapyDay')
        family_members = request.POST.get('familyMembers')
        address = request.POST.get('address')
        time_availability = request.POST.get('timeAvailability')
        current_city = request.POST.get('currentCity')

        # Optional: save to DB
        # ApproachForm.objects.create(
        #     first_name=first_name,
        #     last_name=last_name,
        #     mobile=mobile,
        #     email=email,
        #     therapy_title=therapy_title,
        #     therapy_day=therapy_day,
        #     family_members=family_members,
        #     address=address,
        #     time_availability=time_availability,
        #     current_city=current_city
        # )

        # Show message
        messages.success(request, "Form submitted successfully!")

        # Redirect to payment page
        return redirect('pay')  # Ensure 'pay' URL exists

    return render(request, 'approach_form.html', {'therapy_title': therapy_title})

def pay(request):
    # Render your payment page
    return render(request, 'payment.html')

def trial(request):
    # Render your payment page
    return render(request, 'trial.html')

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Check if the user exists first
        if not User.objects.filter(username=username).exists():
            messages.warning(request, "User does not exist. Please sign up first.")
            return render(request, 'login.html')

        # Authenticate the user
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect after successful login
        else:
            messages.error(request, "Incorrect password. Please try again.")

    return render(request, 'login.html')


from django.contrib.auth import logout

def logout_view(request):
    logout(request)
    return redirect('home')


from django.contrib.auth.models import User
from django.contrib.auth import login
from django.contrib import messages

def signup_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken")
        else:
            user = User.objects.create_user(username=username, password=password)
            login(request, user)
            return redirect('home')
    return render(request, 'signup.html')






