from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Author,Category,Book,Review


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id','username','email','first_name','last_name']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=Category
        fields='__all__' 
        
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model=Author
        fields='__all__'


class ReviewSerializer(serializers.ModelSerializer):
    user=UserSerializer(read_only=True)
    class Meta:
        model=Review
        fields=['id', 'rating', 'comment', 'user', 'created_at', 'updated_at']
        read_only_fields = ['user'] 
          
    def create(self, validated_data):
        validated_data['user']=self.context['request'].user
        return super().create(validated_data)  
    
class BookSerializer(serializers.ModelSerializer):
    author_detail=AuthorSerializer(source='author',read_only=True)
    categories_detail=CategorySerializer(source='categories',read_only=True,many=True) 
    reviews=ReviewSerializer(many=True,read_only=True)
    average_rating=serializers.SerializerMethodField()
    
    class Meta:
        model = Book
        fields = [
            'id', 'title', 'isbn', 'published_date', 'price', 
            'description', 'in_stock', 'author', 'author_detail', 
            'categories', 'categories_detail', 'reviews', 
            'average_rating', 'created_at', 'updated_at'
        ]
    def get_average_rating(self,obj):  
        reviews = obj.review.all()
        if reviews:
            return sum(review.rating for review in reviews)/len(reviews)
        return None  
    
                        