from django.contrib import admin
from .models import User, Book, BookDetails, BorrowedBooks
# Register your models here.

admin.site.register(User)
admin.site.register(Book)
admin.site.register(BookDetails)
admin.site.register(BorrowedBooks)