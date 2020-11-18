import pytest
import sys
sys.path.append('..')

from mycodes.main import *

class TestMain:

    # Test to get price
    @pytest.mark.usefixtures("return_obj_book1")
    def test_book_price(self, return_obj_book1):
        assert return_obj_book1.price == 20
    
    # Test to set_prod_cost method 
    @pytest.mark.usefixtures("return_obj_book1")
    def test_set_prod_cost(self, return_obj_book1):
        return_obj_book1.prod_cost = 16
        assert return_obj_book1.prod_cost == 16
    
    # Next 3 tests check set_discount_price method
    @pytest.mark.usefixtures("return_obj_book1")
    def test_set_discount_price_persent(self, return_obj_book1):
        return_obj_book1.set_discount_price('faiz', 10)
        assert return_obj_book1.discount_price == 18

    @pytest.mark.usefixtures("return_obj_book1")
    def test_set_discount_price_unit(self, return_obj_book1):
        return_obj_book1.set_discount_price('vahid', 10)
        assert return_obj_book1.discount_price == 10

    @pytest.mark.usefixtures("return_obj_book1")
    def test_set_discount_price_wrong_type(self, return_obj_book1):
        return_obj_book1.set_discount_price('salam', 10)
        assert return_obj_book1.set_discount_price('salam', 10) == 'Parametrler duzgun daxil edilmeyib'
    
    # Next 3 tests for test get_name() method
    @pytest.mark.usefixtures("return_obj_book1")
    def test_get_name_book(self, return_obj_book1):
        assert return_obj_book1.get_name() == 'Kitabin adi: Mark Tvein | Kitabin yazari: Check London'
    
    @pytest.mark.usefixtures("return_obj_tshirt1")
    def test_get_name_book(self, return_obj_tshirt1):
        assert return_obj_tshirt1.get_name() == 'Paltarin adi: Tshirt | Paltarin rengi: red'
    
    @pytest.mark.usefixtures("return_obj_product1")
    def test_get_name_book(self, return_obj_product1):
        assert return_obj_product1.get_name() == 'Mehsulun adi: Soyuducu'