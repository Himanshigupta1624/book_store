from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Author(models.Model):
    name=models.CharField(max_length=150)
    bio=models.TextField(blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering=['name']
        


class Category(models.Model)  :
    name=models.CharField(max_length=150)
    description=models.TextField(blank=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural='Categories'
        ordering=['name']
        

class Book(models.Model):
    title=models.CharField(max_length=250)
    author=models.ForeignKey(Author,on_delete=models.CASCADE,related_name='books')
    categories=models.ManyToManyField(Category,related_name='books')
    isbn=models.CharField(max_length=13,unique=True)
    published_date=models.DateField()
    price=models.DecimalField(max_digits=7,decimal_places=2)
    description=models.TextField(blank=True)
    in_stock=models.BooleanField(default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    
    
    class Meta:
        ordering=['-created_at']
        
        
class Review(models.Model):
    book=models.ForeignKey(Book,on_delete=models.CASCADE,related_name='review')
    
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name='review')                
    rating=models.IntegerField(choices=[(i,i) for i in range (1,6)])
    comment=models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        unique_together = ('book', 'user')
        ordering = ['-created_at']
        
        def __str__(self):
            return f'{self.user.username} - {self.book.title} - {self.rating}'
        
