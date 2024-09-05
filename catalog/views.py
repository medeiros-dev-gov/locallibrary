from django.shortcuts import get_object_or_404, render
from catalog.models import Book, Author, BookInstance, Genre
from django.views.generic import ListView, DetailView

def index(request):
    """View function for home page of site."""
    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors,
    }

    return render(request, 'index.html', context=context)

class BookListView(ListView):
    model = Book
    template_name = 'catalog/book_list.html'
    context_object_name = 'books'
    paginate_by = 10  # Paginate by 10 books per page

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['some_data'] = 'This is just some data'
        return context

class BookDetailView(DetailView):
    model = Book
    template_name = 'catalog/book_detail.html'
    