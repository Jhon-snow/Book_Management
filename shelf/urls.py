import imp
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from shelf import views

urlpatterns = [
    path("", views.home, name = "home"),
    path("addauthor/", views.addAuthor, name = "addAuthor"),
    path("addbook/", views.addBookToCatalog, name = "addBook"),
    path("addCateogry/", views.addCateogry, name = "addCatogry"),
    path("listofCateogries/", views.fetchCateogries, name = "fetchAllCateogries"),
    path("listofAuthors/", views.getAllAuthorName, name = "fetchAllAuthors"),
    path("mostbooksoldbyAuthor/", views.mostbooksoldbyAuthor, name = "highestSellingBook"),
    path("mostbooksoldbyCateogry/", views.mostbooksoldbyCateogry, name = "highestSellingBookbyCateogry"),
    path("allbooksoldbyAuthor/", views.allBooksByAuthor, name = "allBooksSellByAuthor"),
]
urlpatterns += staticfiles_urlpatterns()