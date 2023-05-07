from django.shortcuts import render, redirect
from footballApp.forms import CustomUserCreationForm, GameForm
from footballApp.models import Game, Team
from django.views.generic import UpdateView, DeleteView

# Create your views here.
def indexPage(request):
    games = Game.objects.all()
    teams = Team.objects.all()

    nextGame = Game.objects.filter(eventStatus='not finished').first()
    numberOfElements = Game.objects.all().count()

    if numberOfElements:
        gameStatus = Game.objects.first().eventStatus

    if numberOfElements > 3 and gameStatus == "finished":
        Game.objects.first().delete()

    return render(request, 'index.html', {'games': games, 'teams': teams, 'nextGame': nextGame})


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


def addGame(request):
    if request.method == "POST":
        form = GameForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')

    form = GameForm()
    data = {
        'form': form,
    }

    return render(request, 'addGame.html', data)


class MatchUpdateView(UpdateView):
    model = Game
    template_name = 'addGame.html'
    form_class = GameForm


class MatchDeleteView(DeleteView):
    model = Game
    success_url = '/'
    template_name = 'delete.html'