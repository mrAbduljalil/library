from django.shortcuts import render, get_object_or_404
from .models import Books

def books_list(request):
    books = Books.objects.all()
    return render(request, 'books_list.html', {'books': books})

def book_detail(request, book_id):
    book = get_object_or_404(Books, id=book_id)
    return render(request, 'book_detail.html', {'book': book})
