from rest_framework import generics, permissions
from .models import Posts
from .serializers import PostSerializer

# Create your views here.
class PostList(generics.CreateAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = Posts.objects.all()
  serializer_class = PostSerializer

class PostDetail(generics.RetrieveUpdateDestroyAPIView):
  permission_classes = [permissions.IsAuthenticated]
  queryset = Posts.objects.all()
  serializer_class = PostSerializer
