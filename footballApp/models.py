from django.db import models

# Create your models here.
class Game(models.Model):
    firstTeam = models.CharField(max_length=20, blank=False)
    firstTeamStatus = models.CharField(max_length=5, blank=False)
    goalsFirstTeam = models.IntegerField(default=0)
    playersFirstTeam = models.CharField(max_length=300, blank=False)

    secondTeam = models.CharField(max_length=20, blank=False)
    secondTeamStatus = models.CharField(max_length=5, blank=False)
    goalsSecondTeam = models.IntegerField(default=0)
    playersSecondTeam = models.CharField(max_length=300, blank=False)

    eventOwner = models.CharField(max_length=20, blank=False)
    eventStatus = models.CharField(max_length=20, blank=False)

    def get_absolute_url(self):
        return '/'

    def __str__(self):
        return self.firstTeam + " - " + self.secondTeam


class Team(models.Model):
    place = models.CharField(max_length=3, blank=False)
    teamName = models.CharField(max_length=20, blank=False)
    win = models.CharField(max_length=3, blank=False)
    loss = models.CharField(max_length=3, blank=False)
    draw = models.CharField(max_length=3, blank=False)

    def __str__(self):
        return self.teamName
