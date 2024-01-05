from django.shortcuts import  get_object_or_404,render
from django.http import Http404
from django.db.models import Avg

from .models import Book

# Create your views here.

def index (request):
    books = Book.objects.all().order_by("-title")
    num_books = books.count()
    avg_rating = books.aggregate(Avg('rating'))
    return render(request,"books/index.html",{
        "books":books
    })
    
def book_detail(request,slug):
    book = get_object_or_404(Book,slug=slug)
    return render(request,"books/book_detail.html",{
        "title":book.title,
        "author":book.author,
        "rating":book.rating,
        "is_bestselling":book.is_bestselling
    })
