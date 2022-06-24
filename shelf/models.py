from cgi import print_exception
from msilib.schema import PatchPackage
from optparse import TitledHelpFormatter
import re
from unicodedata import category, name
from django.db import models


# Create your models here.
class Book:
    def __init__(self, book_id, title, author_id, publisher, publish_date, cateogry_id, price, sold_count) -> None:
        self.__book_id = book_id
        self.__title = title
        self.__author_id = author_id
        self.__publisher = publisher
        self.__publish_date = publish_date
        self.__category_id = cateogry_id
        self.__price = price
        self.__sold_count = sold_count
    
    def setbookid(self, book_id):
        self.__book_id = book_id

    def getbookid(self):
        return self.__book_id

    def settitle(self, title):
        self.__title = title
    
    def getitle(self):
        return self.__title

    def setauthor_id(self, author_id):
        self.__author_id = author_id

    def getauthor_id(self):
        return self.__author_id

    def setpublisher(self, publisher):
        self.__publisher = publisher

    def getpublisher(self):
        return self.__publisher
    
    def setpublish_date(self, publish_date):
        self.__publish_date = publish_date

    def getpublish_date(self):
        return self.__publish_date

    def setcategory_id(self, category_id):
        self.__category_id = category_id

    def getcategory_id(self):
        return self.__category_id
    
    def setprice(self, price):
        self.__price = price

    def getprice(self):
        return self.__price

    def setsold_count(self, sold_count):
        self.__sold_count = sold_count

    def getsold_count(self):
        return self.__sold_count


class Author:
    def __init__(self, author_id, author_name, phone_number, birth_date, death_date) -> None:
        self.__author_id = author_id
        self.__author_name = author_name
        self.__phone_number = phone_number
        self.__birth_date = birth_date
        self.__death_date = death_date or None

    def setauthor_id(self, author_id):
        self.__author_id = author_id

    
    def getauthor_id(self):
        return self.__author_id

    def setauthor_name(self, author_name):
        self.__author_name = author_name

    def getauthor_name(self):
        return self.__author_name

    def setphone_number(self, phone_number):
        self.__phone_number = phone_number

    def getphone_number(self):
        return self.__phone_number

    def setbirth_date(self, birth_date):
        self.__birth_date = birth_date

    def getbirth_date(self):
        return self.__birth_date

    def setdeath_date(self, death_date):
        self.__death_date = death_date

    def getdeath_date(self):
        return self.__death_date

class Cateogries:
    def __init__(self, id, cateogry) -> None:
        self.cateogry_id = id
        self.cateogry = cateogry

    
    def setcateogry_id(self, cateogry_id):
        self.cateogry_id = cateogry_id

    def getcateogry_id(self):
        return self.cateogry_id
    
    def setcateogry(self, cateogry):
        self.cateogry = cateogry

    def getcateogry(self):
        return self.cateogry