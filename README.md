# Library Management System

Welcome to the Library Management System, a Django-based Web Application for Managing books, users, and borrowed books.


# Setup Instruction

### Prerequisites
- Python 3.x
- Django

## Installation
1. Clone the repository
2. git clone https://github.com/ishan004/LibraryManagement.git
3. Create a Virtual Environment and activate the venv.(option but recommended)
4. Install Dependencies:
    pip install  -r requirements.txt
5. Create a database in postgres
    CREATE DATABASE library;
6. Run Migration
    python manage.py makemigrations
     python manage.py migrate
8. Create a superuser account to manage database using django-admin panel
    python manage.py createsuperuser
9. Start the server:
     python manage.py runserver  (Default port is 8000 but you can change if necessary)

Visit [http://localhost:8000] for the webapp or Visit [http://localhost:8000/admin] for django-admin panel.



# API DOCUMENTATION
### User APIs

- **Create a New User:**
    - Endpoint: `/api/users/create/`
    - Method: POST
    - Parameters: name, email, membership_date

- **List All Users:**
    - Endpoint: `/api/users/list/`
    - Method: GET

- **Get User by ID:**
    - Endpoint: `/api/users/<user_id>/`
    - Method: GET

### Book APIs

- **Add a New Book:**
    - Endpoint: `/api/books/create/`
    - Method: POST
    - Parameters: title, ISBN, published_date, genre

- **List All Books:**
    - Endpoint: `/api/books/list/`
    - Method: GET

- **Get Book by ID:**
    - Endpoint: `/api/books/<book_id>/`
    - Method: GET

- **Assign/Update Book Details:**
    - Endpoint: `/api/books/details/<book_id>/`
    - Method: POST
    - Parameters: number_of_pages, publisher, language

### BorrowedBooks APIs

- **Borrow a Book:**
    - Endpoint: `/api/borrow/create/`
    - Method: POST
    - Parameters: user_id, book_id, borrow_date, return_date (optional)

- **Return a Book:**
    - Endpoint: `/api/borrow/return/<borrowed_book_id>/`
    - Method: POST

- **List All Borrowed Books:**
    - Endpoint: `/api/borrow/list/`
    - Method: GET
 

### Additional Notes 

  ### Additional Note
  - The System also includes Authentication but only has option for admin.
  - Although I planned to make this system to have a separate base for users and admin(Librarian) with different actions and interface due to lack of time only implemented for admin.
  - The System has been tested with the latest version of Python.
  - Although initially i planned to use mysql as the database later decided to implement the new Database System (Postgres) that i am currently working to master.

    Feel Free to reach out and give suggestion on how this could have been implemented better.
