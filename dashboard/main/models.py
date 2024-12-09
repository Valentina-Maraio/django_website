from django.db import models

# Create your models here.
class BookList(models.Model):
    month = models.CharField(max_length=10)
    
    def __str__(self):
        return f"{self.month} 2024"

class Book(models.Model):
    book_list = models.ForeignKey(BookList, on_delete=models.CASCADE)
    title = models.CharField(max_length=30)
    author = models.CharField(max_length=30)
    comment = models.CharField(max_length=300)
    complete = models.BooleanField()
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Comment: {self.comment}, Complete: {self.complete}"
