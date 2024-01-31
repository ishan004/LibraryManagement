from django.db import models
from datetime import datetime, timedelta
from django.db.models.signals import post_save
from django.dispatch import receiver




# Create your models here.


class User(models.Model):
    
    UserID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=100)
    Email = models.EmailField(null=True)
    MembershipDate = models.DateField()
    
    
    def __str__(self):
        return self.Name

class Book(models.Model):
    BookID = models.AutoField(primary_key=True)
    Title = models.CharField(max_length=100)
    ISBN = models.CharField(max_length=13, unique=True)
    PublishedDate = models.DateField()
    Genre = models.CharField(max_length=50)

    def __str__(self):
        return self.Title

class BookDetails(models.Model):
    Book = models.OneToOneField(Book, on_delete=models.CASCADE)
    DetailsID = models.AutoField(primary_key=True)
    NumberOfPages = models.IntegerField(default=0)
    Publisher = models.CharField(max_length=100)
    Language = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.Book.Title} Details"

class BorrowedBooks(models.Model):
    UserID = models.ForeignKey(User, on_delete=models.CASCADE)
    BookID = models.ForeignKey(Book, on_delete=models.CASCADE)
    BorrowDate = models.DateField()
    ReturnDate = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.UserID.Name} - {self.BookID.Title} ({self.BorrowDate})"
