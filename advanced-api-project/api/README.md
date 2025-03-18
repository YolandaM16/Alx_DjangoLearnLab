# Book API

## Endpoints
- `GET /api/books/` - List all books 
- `GET /api/books/<int:pk>/` - Retrieve a single book 
- `POST /api/books/create/` - Create a new book 
- `PUT /api/books/update/<int:pk>/` - Update a book 
- `DELETE /api/books/delete/<int:pk>/` - Delete a book 

## Authentication
- Authentication is required for creating, updating, and deleting books.
- Use Token Authentication or JWT.

## Permissions
- Read access is open to everyone.
- Write access (POST, PUT, DELETE) is restricted to authenticated users.
- Only the book owner can update or delete their book.

