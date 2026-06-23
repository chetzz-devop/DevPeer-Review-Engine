from rest_framework import serializers
from .models import Project, Profile, Review
from django.contrib.auth.models import User
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError as DjangoValidationError


class Projectserializer(serializers.ModelSerializer):

    class Meta:
        model = Project
        fields = ['id', 'owner', 'title', 'project_link']

    def validate_project_link(self, value):
        # 1. Check if it's a valid link format overall
        validator = URLValidator()
        try:
            validator(value)
        except ValidationError:
            raise serializers.ValidationError(
                "Please enter a valid URL link (e.g., https://example.com).")
        return value


class ReviewSerializer(serializers.ModelSerializer):
    # Enforce rating limits at API level
    value = serializers.IntegerField(min_value=1, max_value=5)

    # 🚀 NEW: Add read-only fields to extract human-readable text
    project_title = serializers.CharField(
        source='project.title', read_only=True)
    author_name = serializers.CharField(
        source='author.user.username', read_only=True)

    class Meta:
        model = Review
        # Add the new fields to your fields array
        fields = [
            'id',
            'project',
            'project_title',
            'author',
            'author_name',
            'value',
            'comment'
        ]

    def validate(self, data):
        """
        Object-level validation to stop users from rating their own work.
        """
        project = data['project']
        author = data['author']

        if project.owner == author:
            raise serializers.ValidationError(
                "You cannot review or rate your own project!")

        return data
