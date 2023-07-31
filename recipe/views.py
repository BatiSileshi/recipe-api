
from rest_framework import viewsets, mixins
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe, Tag
from recipe import serializers
from django.shortcuts import render

# Create your views here.

'''View for manage recipe APIs.'''
class RecipeViewSet(viewsets.ModelViewSet):
    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    #The following are APIview method
    def get_queryset(self):
        '''Retrieve recipe for authenticated user.'''
        return self.queryset.filter(user=self.request.user).order_by('-id')
    
    
    '''Return serializer class for request.'''
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.RecipeSerializer
        
        return self.get_serializer_class
    
    def perform_create(self, serializer):
        '''Create a new recipe.'''
        serializer.save(user=self.request.user)
        

    
class TagViewSet(
    mixins.DestroyModelMixin,
    mixins.UpdateModelMixin, 
    mixins.ListModelMixin, 
    viewsets.GenericViewSet):
    serializer_class = serializers.TagSerializer
    queryset = Tag.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    '''Filters tags of authenticated user.'''
    def get_queryset(self):
        return self.queryset.filter(user=self.request.user).order_by('-name')
    



'''
#APIView
- focused around HTTP methods
- useful for non CRUD APIs
- great for authentication

#Viewsets
- focused around actions (retrieve, list, update, partial update, destroy)
- map to django models
- use routers (automatically generate urls)
- great for CRUD

'''