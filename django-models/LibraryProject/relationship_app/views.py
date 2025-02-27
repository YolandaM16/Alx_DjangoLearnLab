from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView # Class Based View
from django.contrib.auth import login, logout # Function Based view
from .models import Library
from .models import Book
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required
from django.forms import BookForm
# Create your views here.

# Function Base View For Listing all books
def list_books(request):
    books = Book.objects.all()
    context = {'book_list': books}
    return render(request, 'relationship_app/list_books.html', context)


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'
   

# User Registration Class base View    
class SignupView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "register.html"
   

# class CustomLoginView(LoginView):
    template_name = 'login.html'
   
class CustomLogoutView(LogoutView):
    template_name = 'logout.html'

# User Registration Function base View
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user) # Log in the user after successful registration
            return redirect("home")  # Redirect to homepage or dashboard
   
    else:
        form = UserCreationForm()
        return render(request, "relationship_app/register.html", {"form": form})
   

# User Login View (Django provides an authentication form)
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
   
    else:
        form = AuthenticationForm()
        return render(request, "registration_app/login.html", {"form": form})  
   

def logout_view(request):
    logout(request)
    return redirect("login")

def is_admin(user):
    return user.userprofile.role == 'Admin'

def is_librarian(user):
    return user.userprofile.role == 'Librarian'

def is_member(user):
    return user.userprofile.role == 'Member'


@login_required
@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')

@login_required
@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')

@login_required
@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

# view to add a book
@permission_required("relationship_app.can_add_book")
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm()
    return render(request, 'relationship_app/add_book.html', {'form': form})

# edit book
@permission_required("relationship_app.can_change_book")
def edit_book(request, pk):
    book = get_object_or_404()
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('list_books')
    else:
        form = BookForm(instance = book)
    return render(request, 'relationship_app/edit_book.html', {'form': form})

# delete book
@permission_required("relationship_app.can_delete_book")
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('list_books')
    else:
        return render(request, 'relationship_app/delete_book.html', {'book': book})