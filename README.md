# Book_Management
This is a small project to store the data of Books, Authors, and Cateogries of Books.
It is for Machine coding round using OOPS concept and Simple DataStructres using Django.

# Prerequisites
Should have basic knowledge about Django and Python. One should know how to hit HTTP request from Postman or any other tool to get a demonstrable project.

# Steps to run the project
1. Clone the project
2. Create a virtual env and install all the pip dependicies
3. Run manage.py file, using below command

```
python manage.py runserver 
```
4. start hitting the API's from Postman

# Files and Their Usage
1. Models.py => This file represents the actual Models that can be used in Db, but in project we have created classes for them.
It contains 3 classes:

<br>

    ```
    class Book:
    class Author:
    class Cateogries:
    ```
</br>

2. Urls.py => It contains all the urls, that routes to the actual functions.


3. views.py => This file contains all the methods, that are routed from "Urls.py file".

<br>

    ```
    <!-- Accepts Http POST Request -->
    def addAuthor(request):
    def addBookToCatalog(request):
    def addCateogry(request):
    <!-- Accepts Http GET Requests -->
    def fetchCateogries(request):
    def getAllAuthorName(request):
    def mostbooksoldbyAuthor(request):
    def mostbooksoldbyCateogry(request):
    def allBooksByAuthor(request):
    ```
</br>

4. Exceptions.py => Contains the custom exception, that are used in the project.

5. helper.py => Used for addtional helper function inside the App.

# Description and rules to hit the API's 

1. def addAuthor(request):
Request should be a POST request and body should be JSON that looks like this, returns a success message on succesfull addition.
```
    <!-- date format should be dd-mm-YYYY and the date should be valid -->
    <!-- death_date, number is not mandatory -->
    {
    "id" : "author1",
    "name" : "XXXXX",
    "number": "XXXXXX",
    "birth_date": "21-05-1998",
    "death_date": ""
    }
```
2. def addBookToCatalog(request):
Request should be a POST request and body should be JSON that looks like this,returns a success message on succesfull addition.

```

{
    <!-- date format should be dd-mm-YYYY and the date should be valid -->
    <!-- all fields are mandatory -->
    "id" : "book1",
    "book_title": "lonley wolf",
    "author_id" : "author1",
    "publisher" : "dharma",
    "publish_date" : "21-10-2019",
    "cateogry_id" : "cateogry1",
    "price" : "300"
    }
```
3. def addCateogry(request):
Request should be a POST request and body should be JSON that looks like this, returns a success message on succesfull addition.

```

{
    <!-- all fields are mandatory -->
    "id" : "cateogry1",
    "cateogry": "Action"
    }
```

4. def fetchCateogries(request):
Request should be a GET request, It did not expect any arguments or params, return a dictionary having the name of all cateogries.

5. def getAllAuthorName(request):
Request should be a GET request, It did not expect any arguments or params, return a dictionary having the name of all Authors.

6. def mostbooksoldbyAuthor(request):
Request should be a GET request, It expect params having an author_id, return a dictionary having the details of book that has highest selling count written by given author.

```

http://127.0.0.1:8000/mostbooksoldbyAuthor/?author_id=Author1
```
7. def mostbooksoldbyCateogry(request):
Request should be a GET request, It expect params having an cateogry_id, return a dictionary having the details of book that has highest selling count in given cateogry.

```

http://127.0.0.1:8000/mostbooksoldbyCateogry/?cateogry_id=Cateogry2
```

8. def allBooksByAuthor(request):
Request should be a GET request, It expect params having an author_id, return a list of dictionaries having the details of all the books written by given author.

```

http://127.0.0.1:8000/allbooksoldbyAuthor/?author_id=Author2
```

# Credits

All the project is created by the Author "ANUBHAV RATHI". Connect with me.

[https://www.linkedin.com/in/anubhav2105/](https://www.linkedin.com/in/anubhav2105/)

[https://www.instagram.com/anubhav_rathi88/](https://www.instagram.com/anubhav_rathi88/)
