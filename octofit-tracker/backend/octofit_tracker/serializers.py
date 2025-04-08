from rest_framework import serializers
from bson import ObjectId

class ObjectIdField(serializers.Field):
    def to_representation(self, value):
        return str(value)

    def to_internal_value(self, data):
        return ObjectId(data)

class UserSerializer(serializers.Serializer):
    _id = ObjectIdField()
    name = serializers.CharField()
    email = serializers.EmailField()

class TeamSerializer(serializers.Serializer):
    _id = ObjectIdField()
    name = serializers.CharField()
    members = UserSerializer(many=True)

class ActivitySerializer(serializers.Serializer):
    _id = ObjectIdField()
    user = ObjectIdField()
    type = serializers.CharField()
    duration = serializers.IntegerField()

class LeaderboardSerializer(serializers.Serializer):
    _id = ObjectIdField()
    user = UserSerializer()  # Expand the user object
    score = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    _id = ObjectIdField()
    name = serializers.CharField()
    description = serializers.CharField()
