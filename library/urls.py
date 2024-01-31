from django.urls import path
from .views import home_view , admin_dashboard_view, add_new_book,list_all_books, get_book_by_id, assign_update_book_details,create_new_user,list_all_users,get_user_by_id, borrow_book, return_book,list_all_borrowed_books 
# from library.views import 

urlpatterns = [
    path('', home_view, name='home'),
    path('admindashboard/',admin_dashboard_view, name='admindashboard' ),
    
    
    path('add_new_book/', add_new_book, name='add_new_book'),
    path('list_all_books/', list_all_books, name='list_all_books'),
    path('get_book_by_id/<int:book_id>/', get_book_by_id, name='get_book_by_id'),
    path('assign_update_book_details/<int:book_id>/', assign_update_book_details, name='assign_update_book_details'),
    
    path('create_new_user/', create_new_user, name='create_new_user'),
    path('list_all_users/', list_all_users, name='list_all_users'),
    path('get_user_by_id/<int:user_id>/', get_user_by_id, name='get_user_by_id'),
    
    path('borrow_book/', borrow_book, name='borrow_book'),
    path('return_book/', return_book, name='return_book'),
    path('list_all_borrowed_books/', list_all_borrowed_books, name='list_all_borrowed_books'),
    
    
]