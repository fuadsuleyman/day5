import pytest
import sys
sys.path.append('..')

from mycodes.main import *

obj_book1 = Book('English', 'Check London', '2018', 349, 'Adventure', 'Maarif Neshriyyati', 'Mark Tvein', 30, 25, 27)

@pytest.fixture()
def return_obj_book1():
    return obj_book1