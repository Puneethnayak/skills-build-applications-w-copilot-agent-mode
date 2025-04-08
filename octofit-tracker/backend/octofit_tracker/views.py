from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
from django.http import JsonResponse
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, LeaderboardSerializer, WorkoutSerializer
from bson import ObjectId
from pymongo import MongoClient

client = MongoClient('mongodb://localhost:27017/')
db = client['octofit']

def api_root(request):
    return JsonResponse({
        "message": "Welcome to OctoFit API",
        "url": "https://urban-space-parakeet-979wrq4xg79fpv7w-8000.app.github.dev"
    })

class UserViewSet(viewsets.ViewSet):
    def list(self, request):
        users = list(db.users.find())
        return Response(users)

    def retrieve(self, request, pk=None):
        user = db.users.find_one({"_id": ObjectId(pk)})
        return Response(user)

class TeamViewSet(viewsets.ViewSet):
    def list(self, request):
        teams = list(db.teams.find())
        return Response(teams)

    def retrieve(self, request, pk=None):
        team = db.teams.find_one({"_id": ObjectId(pk)})
        return Response(team)

class ActivityViewSet(viewsets.ViewSet):
    def list(self, request):
        activities = list(db.activities.find())
        return Response(activities)

    def retrieve(self, request, pk=None):
        activity = db.activities.find_one({"_id": ObjectId(pk)})
        return Response(activity)

class LeaderboardViewSet(viewsets.ViewSet):
    def list(self, request):
        leaderboards = list(db.leaderboards.find())
        return Response(leaderboards)

    def retrieve(self, request, pk=None):
        leaderboard = db.leaderboards.find_one({"_id": ObjectId(pk)})
        return Response(leaderboard)

class WorkoutViewSet(viewsets.ViewSet):
    def list(self, request):
        workouts = list(db.workouts.find())
        return Response(workouts)

    def retrieve(self, request, pk=None):
        workout = db.workouts.find_one({"_id": ObjectId(pk)})
        return Response(workout)
