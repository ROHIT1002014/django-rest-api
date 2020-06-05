from django.contrib.auth import get_user_model

from rest_framework import serializers
from .models import Posts

class PostSerializer(serializers.ModelSerializer):
  class Meta:
    model = Posts
    fields = '__all__'

class UserSErializer(serializers.ModelSerializer):
  class Meta:
    model = get_user_model()
    fields = ('id', 'username')