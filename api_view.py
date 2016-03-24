from serializers import *
from models import *
from rest_framework import viewsets

#Profile/User
class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
