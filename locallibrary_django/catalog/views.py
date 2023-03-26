from django.shortcuts import render
from .models import Book, Author, BookInstance, Genre
from django.views import generic

# Create your views here.


def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    # number of genres containing the word 'fantasy'
    num_genres_fantasy = Genre.objects.filter(name__icontains="fantasy").count()

    # number of books containing the word 'wind'
    num_books_wind = Book.objects.filter(title__icontains="wind").count()

    # number of visits to this view, as counted in the session variable
    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "num_genres_fantasy": num_genres_fantasy,
        "num_books_wind": num_books_wind,
        "num_visits": num_visits,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "index.html", context=context)


# BookListView
class BookListView(generic.ListView):
    model = Book
    # # your own name for the list as a template variable
    # context_object_name = 'book_list'
    # # Get 5 books containing the title war
    # queryset = Book.objects.filter(title__icontains='war')[:5]
    # # Specify your own template name/location
    # template_name = 'books/my_arbitrary_template_name_list.html'
    # # can override get_queryset() to return a different queryset
    # def get_queryset(self):
    # return Book.objects.filter(title__icontains='war')[:5] # Get 5 books containing the title war
    # set the number of objects to display per page
    paginate_by = 5


# BookDetailView


class BookDetailView(generic.DetailView):
    model = Book


# AuthorListView


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 5


# AuthorDetailView


class AuthorDetailView(generic.DetailView):
    model = Author
