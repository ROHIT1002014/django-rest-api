from django.contrib.auth import get_user_model
from rest_framework import viewsets # to remove repeatation of code

from rest_framework import permissions
from .models import Posts
from .serializers import PostSerializer, UserSErializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostViewSet(viewsets.ModelViewSet):
  permission_classes = [IsAuthorOrReadOnly,]
  queryset = Posts.objects.all()
  serializer_class = PostSerializer

# class PostDetail(generics.RetrieveUpdateDestroyAPIView):
#   permission_classes = [IsAuthorOrReadOnly,]
#   queryset = Posts.objects.all()
#   serializer_class = PostSerializer

# if u see below code is the repetation of above code
class UserViewSet(viewsets.ModelViewSet):
  queryset = get_user_model().objects.all()
  serializer_class = UserSErializer

# class UserDetail(generics.RetrieveUpdateDestroyAPIView):
#   queryset = get_user_model().objects.all()
#   serializer_class = UserSErializer
