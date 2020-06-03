from rest_framework import generics, permissions
from .models import Posts
from .serializers import PostSerializer
from .permissions import IsAuthorOrReadOnly

# Create your views here.
class PostList(generics.ListCreateAPIView):
  permission_classes = [IsAuthorOrReadOnly,]
  queryset = Posts.objects.all()
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [IsAuthorOrReadOnly,]
  queryset = Posts.objects.all()
  serializer_class = PostSerializer
