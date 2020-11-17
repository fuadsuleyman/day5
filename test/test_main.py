import pytest
import sys
sys.path.append('..')

from mycodes.main import *

class TestMain:

    @pytest.mark.usefixtures("return_obj_book1")
    def test_book_price(self, return_obj_book1):
        assert return_obj_book1.price == 25
