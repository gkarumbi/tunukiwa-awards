from rest_framework import serializers
from .models import Project, Profile

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('title', 'image', 'description','link','pub_date','upvote','downvote')

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = MoringaMerch
        fields = ('profile', 'bio', 'phone')