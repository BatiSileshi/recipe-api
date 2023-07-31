from rest_framework import serializers
from core.models import Recipe, Tag


'''Serializer for Recipe.'''
class RecipeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Recipe
        fields = ['id', 'title', 'time_minutes', 'price', 'link']
        read_only_fields = ['id']
        
        
        
'''Serializer for recipe detail view.'''
class RecipeDetailSerializer(RecipeSerializer):
    class Meta(RecipeSerializer.Meta):
        fields = RecipeSerializer.Meta.fields + ['description']
        
        
'''Serializer for tags.'''
class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']
        read_only_fields = ['id']
        
        