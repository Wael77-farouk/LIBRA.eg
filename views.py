from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import BookForm , CategoryForm
from django.shortcuts import redirect
# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        if add_book.is_valid():
            add_book.save()
    
    add_category =  CategoryForm(request.POST)
    if add_category.is_valid():
        add_category.save()

    context = {
        'category':Category.objects.all(),
        'book': Books.objects.all(),
        'form': BookForm(),
        'formcat':CategoryForm(),
        'allbooks': Books.objects.filter(active=True).count(),
        'booksold': Books.objects.filter(status='sold').count(),
        'bookrented': Books.objects.filter(status='rented').count(),
        'bookavailable': Books.objects.filter(status='available').count(),

    }
    return render(request,'pages/index.html', context)



def books(request):
    search = Books.objects.all()
    title = None
    if 'search_name' in request.GET:
        title = request.GET['search_name']
        if title:
            search = search.filter(title__icontains=title)

    context = {
        'category': Category.objects.all(),
        'book': search,
        'formcat':CategoryForm(),

    }
    return render(request, 'pages/books.html',context)


def update(request, id):
    book_id = Books.objects.get(id=id)
    if request.method =='POST':
        book_save = BookForm(request.POST, request.FILES , instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
            book_save = BookForm(instance=book_id)   
    context = {
            'form':book_save,
        }
    return render(request,'pages/update.html',context)

def delete(request,id):
    book_delete = Books.objects.get(id=id)
    #book_delete = get_object_or_404(Books,id=id)
    if request.method =='POST':
        book_delete.delete()
        return redirect('/')
    return render(request,'pages/delete.html')





























