from django.shortcuts import render
from footballApp.forms import CustomUserCreationForm

# Create your views here.
def indexPage(request):
    return render(request, 'index.html')


def registrationPage(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            print(form.error_messages)
    else:
        form = CustomUserCreationForm()

    formData = {
        'form': form,
    }

    return render(request, 'registration.html', formData)