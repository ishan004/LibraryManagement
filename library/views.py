from django.shortcuts import render,redirect, HttpResponse,get_object_or_404
from django.http import  HttpResponseRedirect
from .models import User 
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .models import Book, BookDetails, BorrowedBooks
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from django.contrib import messages

# Create your views here.

def home_view(request):
    return render(request, 'home.html')
@login_required
def admin_dashboard_view(request):
    return render(request, 'admin/admin_dashboard.html')


@login_required
@csrf_exempt
def add_new_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        isbn = request.POST.get('isbn')
        publishedDate = request.POST.get('published_date')
        genre = request.POST.get('genre')
        
        book = Book.objects.create(Title=title, ISBN =isbn, PublishedDate=publishedDate,Genre=genre)
        
        return HttpResponseRedirect(reverse('list_all_books'))
    else:
        return render(request, 'admin/add_new_book.html')
@login_required    
def list_all_books(request):
    books = Book.objects.all()
    return render(request, 'admin/list_all_books.html', {'books': books})


@login_required
def get_book_by_id(request, book_id):
    book = get_object_or_404(Book, BookID=book_id)
    return render(request, 'admin/book_details.html', {'book': book})
        
@login_required
@csrf_exempt
def assign_update_book_details(request, book_id):
    book = get_object_or_404(Book, BookID=book_id)
    
    if request.method == 'POST':
        number_of_pages = request.POST.get('number_of_pages')
        publisher = request.POST.get('publisher')
        language = request.POST.get('language')

        book_details, created = BookDetails.objects.get_or_create(Book=book)
        book_details.NumberOfPages = number_of_pages
        book_details.Publisher = publisher
        book_details.Language = language
        book_details.save()

        return HttpResponseRedirect(reverse('list_all_books'))
    else:
        return render(request, 'admin/assign_update_book_details.html', {'book': book})
    
# Api for member creation can be accessed through admin
@login_required
@csrf_exempt
def create_new_user(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        membership_date = request.POST.get('membership_date')
        
        user = User(Name=name, Email=email, MembershipDate=membership_date)
        user.save()
        messages.success(request, 'User created successfully!')
        return HttpResponseRedirect(request.path_info)
    return render(request, 'admin/useroperation/create_new_user.html')
    
@login_required    
def list_all_users(request):
    if request.method == 'GET':
        users = User.objects.all()
        return render(request, 'admin/useroperation/list_all_user.html', {'users': users})
    else:
        return HttpResponse(status=405) 
     
@login_required
def get_user_by_id(request, user_id):
    if request.method == 'GET':
        user = get_object_or_404(User, UserID=user_id)
        return render(request, 'admin/useroperation/get_user_by_id.html', {'user': user})
    else:
        return HttpResponse(status=405)  

# Api for Borrow operations. Can be accessed by users
@login_required
@csrf_exempt
def borrow_book(request):
    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        book_id = request.POST.get('book_id')
        return_date = request.POST.get('return_date')

        user = get_object_or_404(User, UserID=user_id)
        book = get_object_or_404(Book, BookID=book_id)

        if not BorrowedBooks.objects.filter(BookID=book, ReturnDate__isnull=True).exists():
            borrow_date = datetime.now().date()

            if datetime.strptime(return_date, '%Y-%m-%d').date() < borrow_date:
                messages.success(request, "Return date cannot be less than the present date.")
                return HttpResponseRedirect(request.path_info)

            borrowed_book = BorrowedBooks.objects.create(UserID=user, BookID=book, BorrowDate=borrow_date, ReturnDate=return_date)
            messages.success(request, f'You have successfully borrowed {borrowed_book.BookID.Title} Book.')
            return HttpResponseRedirect(request.path_info)
        else:
            messages.success(request, 'Selected book is not available for borrowing.')
            return HttpResponseRedirect(request.path_info)
    else:
        users = User.objects.all()
        available_books = Book.objects.exclude(borrowedbooks__ReturnDate__isnull=False)
        return_date = datetime.now().date()
        
        no_books_available = not available_books.exists()
        
        return render(request, 'admin/borrow/borrow_book.html', {'users': users, 'available_books': available_books, 'borrow_date': return_date, 'no_books_available': no_books_available})

@login_required
def return_book(request):
    # Retrieve the list of borrowed books ordered by return date
    borrowed_books = BorrowedBooks.objects.filter(ReturnDate__isnull=False).order_by('ReturnDate')

    if request.method == 'POST':
        borrowed_book_id = request.POST.get('borrowed_book_id')
        borrowed_book = get_object_or_404(BorrowedBooks, id=borrowed_book_id)

        # Delete the borrowed book
        borrowed_book.delete()

        message = f'Book {borrowed_book.BookID.Title} returned by {borrowed_book.UserID.Name}. The book is now available for borrowing.'
        return redirect('return_book')  # Redirect to the same view after processing POST

    if not borrowed_books.exists():
        no_books_message = 'There are no books currently borrowed.'
        return render(request, 'admin/borrow/return_book.html', {'borrowed_books': borrowed_books, 'no_books_message': no_books_message})

    return render(request, 'admin/borrow/return_book.html', {'borrowed_books': borrowed_books})

#can be accessed by Admin or librarian
@login_required
def list_all_borrowed_books(request):
    if request.method == 'GET':
        borrowed_books = BorrowedBooks.objects.all().order_by('ReturnDate')
        
        return render(request, 'admin/borrow/list_all_borrowed_books.html', {'borrowed_books': borrowed_books})
    else:
        return HttpResponse(status=405) 