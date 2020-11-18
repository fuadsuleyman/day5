import pytest
import sys
sys.path.append('..')

from mycodes.main import *

obj_book1 = Book('English', 'Check London', '2018', 349, 'Adventure', 'Maarif Neshriyyati', 20, 17, 15, 'Mark Tvein')

obj_tshirt1 = Clothes(14, 'cotton', 'red', 'Tshirt', 100, 80, 99)

obj_product1 = Product('Soyuducu', 'higth', 700, 590, 699)

@pytest.fixture()
def return_obj_book1():
    return obj_book1

@pytest.fixture()
def return_obj_tshirt1():
    return obj_tshirt1

@pytest.fixture()
def return_obj_product1():
    return obj_product1

