from django.http import HttpResponse, JsonResponse
from shelf.Excpetions import InvalidDateException
from shelf.helper import validate_date
from shelf.Excpetions import InvalidIdException
from shelf.models import Cateogries
from shelf.models import Book
from shelf.Excpetions import IncompleteDataException
from shelf.models import Author
import json


# To store the data 3 dictionaries have been used
authors = {}
books = {}
cateogries = {}

def home(request):
    return HttpResponse(" Welcome to the Library!")

def addAuthor(request):
    """
    Add new Author
    """
    # Sample data
    # {"id" : 1,
    # "name" : "Anubhav",
    # "number": "9953226545",
    # "birth_date": "21-05-1998",
    # "death_date": ""
    # }
    if request.method == 'POST':
        # post_data = json.loads("request.body")
        author = json.loads(request.body)
        
        try:
            author_id = author.get('id')
            author_name = author.get('name')
            phone_number = author.get('number')
            birth_date = author.get('birth_date')
            death_date = author.get('death_date')
            if (author_id is None or author_name is None ):
                raise IncompleteDataException
            if (not validate_date(birth_date)):
                raise InvalidDateException
            else:
                authors[author_id] = Author(author_id, author_name, phone_number, birth_date, death_date)
            return HttpResponse(f'Author added Succesfully for author-id: {author_id}', status = 200)   
        except IncompleteDataException:
             return HttpResponse('Data is Invalid or Incomplete.', status = 406)
        except InvalidDateException:
             return HttpResponse('Date is Invalid', status = 406)
        except Exception as e:
            return HttpResponse(f'Something bad happen with error {e}.', status = 406)
            
    return HttpResponse('Bad Request Type', status = 400)

def addBookToCatalog(request):
    """
    Add new Book
    """
    # Sample data
    # {"id" : 1,
    # "book_title": "lonley wolf",
    # "author_id" : 1,
    # "publisher" : "dharma",
    # "publish_date" : "21/0/2019",
    # "cateogry_id" : "c01",
    # "price" : "300"
    # }
    if request.method == 'POST':
        import json
        # post_data = json.loads("request.body")
        book = json.loads(request.body)
        
        try:
            book_id = book.get('id')
            book_title = book.get('book_title')
            author_id = book.get('author_id')
            publisher = book.get('publisher')
            publish_date = book.get('publish_date')
            category_id = book.get('cateogry_id')
            price = book.get('price')
            sold_count = book.get('count')

            if (book_id is None or book_title is None or author_id is None or publisher is None
            or category_id is None or price is None or sold_count is None):
                raise IncompleteDataException
            if (not validate_date(publish_date)):
                raise InvalidDateException
            else:
                book_obj = Book(book_id, book_title, author_id, publisher, publish_date, category_id, price, int(sold_count))
                books[book_id] = book_obj
                if(author_id not in books.keys()):
                    books[author_id] = []
                books[author_id].append(book_obj)
                if(category_id not in books.keys()):
                    books[category_id] = []
                books[category_id].append(book_obj) 
                
            return HttpResponse(f'Book added Succesfully with book-id: {book_id}', status = 200)     
        except IncompleteDataException:
            return HttpResponse('Data is Invalid or Incomplete.', status = 406)
        except InvalidDateException:
             return HttpResponse('Date is Invalid', status = 406)
        except Exception as e:
             return HttpResponse(f'Something bad happen with error {e}.', status = 406)
    return HttpResponse('Bad Request Type', status = 400)

def addCateogry(request):
    """
    Add new Cateogry
    """
    # Sample data
    # {"id" : "c01",
    # "cateogry": "Action"
    # }
    if request.method == 'POST':
        # post_data = json.loads("request.body")
        cateogry = json.loads(request.body)
        try:
            cateogry_id = cateogry.get('id')
            cateogry_name = cateogry.get('cateogry')
            if (cateogry_id is None or cateogry_name is None ):
                raise IncompleteDataException
            else:
                cateogries[cateogry_id] = Cateogries(cateogry_id, cateogry_name)
            return HttpResponse(f'Book added Succesfully with cateogry-id: {cateogry_id}', status = 200)

        except IncompleteDataException:
            return HttpResponse('Data is Invalid or Incomplete.', status = 406)

        except Exception as e:
            return HttpResponse(f'Something bad happen with error {e}.', status = 406)
    return HttpResponse('Bad Request Type', status = 400)


def fetchCateogries(request):
    """
    Fetch the list of all the cateogries
    """
    if request.method == 'GET':
        cateogry_list = {}
        for cateogry_id in cateogries:
            cateogry_list[cateogry_id] = cateogries[cateogry_id].getcateogry()
        return JsonResponse(cateogry_list)
    return HttpResponse('Bad Request Type', status = 400)

def getAllAuthorName(request):
    """
    Return the List of All the Authors
    """
    if request.method == 'GET':
        authors_list = {}
        for author_id in authors:
            authors_list[author_id] = authors[author_id].getauthor_name()
        return JsonResponse(authors_list)
    return HttpResponse('Bad Request Type', status = 400)

def mostbooksoldbyAuthor(request):
    """Get the book having the highest number of sales for given author"""
    if request.method == 'GET':
        try:
            author_id = request.GET.get('author_id')
            if(author_id not in books.keys()):
                raise InvalidIdException
            book_list = books.get(author_id)
            max_count_book = 0
            book_response = {}
            for book in book_list:
                if book.getsold_count() > max_count_book:
                    max_count_book = book.getsold_count()
                    book_response["book_id"] = book.getbookid()
                    book_response["title"] = book.getitle()
                    book_response["author_id"] = book.getauthor_id()
                    book_response["publisher"] = book.getpublisher()
                    book_response["publish_date"] = book.getpublish_date()
                    book_response["category_id"] = book.getcategory_id()
                    book_response["price"] = book.getprice()
                    book_response["sold_count"] = book.getsold_count()
            return JsonResponse(book_response, status = 200)

        except InvalidIdException:
            return HttpResponse('Invalid author ID', status = 404)
            
        except Exception as e:
            return HttpResponse(f'Something bad happen with error {e}.', status = 406)
    return HttpResponse('Bad Request Type', status = 400)


def mostbooksoldbyCateogry(request):
    """Get the book having the highest number of sales for given Cateogry"""
    if request.method == 'GET':
        try:
            cateogry_id = request.GET.get('cateogry_id')
            if(cateogry_id not in books.keys()):
                raise InvalidIdException
            book_list = books.get(cateogry_id)
            max_count_book = 0
            book_response = {}
            for book in book_list:
                if book.getsold_count() > max_count_book:
                    max_count_book = book.getsold_count()
                    book_response["book_id"] = book.getbookid()
                    book_response["title"] = book.getitle()
                    book_response["author_id"] = book.getauthor_id()
                    book_response["publisher"] = book.getpublisher()
                    book_response["publish_date"] = book.getpublish_date()
                    book_response["category_id"] = book.getcategory_id()
                    book_response["price"] = book.getprice()
                    book_response["sold_count"] = book.getsold_count()
            return JsonResponse(book_response, status = 200)

        except InvalidIdException:
            return HttpResponse('Invalid Cateogry ID', status = 404)
            
        except Exception as e:
            return HttpResponse(f'Something bad happen with error {e}.', status = 406)
    return HttpResponse('Bad Request Type', status = 400)

def allBooksByAuthor(request):
    if request.method == 'GET':
        try:
            author_id = request.GET.get('author_id')
            if(author_id not in books.keys()):
                raise InvalidIdException
            book_list = books.get(author_id)
            all_books = []
            for book in book_list:
                book_response = {}
                book_response["book_id"] = book.getbookid()
                book_response["title"] = book.getitle()
                book_response["author_id"] = book.getauthor_id()
                book_response["publisher"] = book.getpublisher()
                book_response["publish_date"] = book.getpublish_date()
                book_response["category_id"] = book.getcategory_id()
                book_response["price"] = book.getprice()
                book_response["sold_count"] = book.getsold_count()
                all_books.append(book_response)
            return JsonResponse(all_books, safe = False, status = 200)

        except InvalidIdException:
            return HttpResponse('Invalid Author ID', status = 404)
            
        except Exception as e:
            return HttpResponse(f'Something bad happen with error {e}.', status = 406)
    return HttpResponse('Bad Request Type', status = 400)
