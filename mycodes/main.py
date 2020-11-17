import uuid
armud = 25

class Product:
    next_id = 1
    def __init__(self,id=None, title=None, rating=None, price=None, prod_cost=None, discount_price=None, description=None, image=None, category=None, brand=None, color=None):
        self.__id = Product.next_id
        self.title = title
        self.rating = rating
        self.__price = price
        self.__prod_cost = prod_cost
        self.discount_price = discount_price
        self.description = description
        self.image = image
        self.category = category
        self.brand = brand
        self.color = color
        Product.next_id += 1
        print(f'{self.__class__.__name__} klasinin obyekti yaradildi')
    
    @property
    def id(self):
        return self.__id
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, x):
        self.__price = x
        if self.price < self.prod_cost:
            print(f'Diqqet! Mehsulun qiymeti maya deyerinden asagidi')

    @property
    def prod_cost(self):
        return self.__prod_cost
    
    @prod_cost.setter
    def prod_cost(self, x):
        self.__prod_cost = x

    def set_discount_price(self, disc_type, disc_value):
        if disc_type == 'faiz':
            self.discount_price = self.price - (self.price * disc_value) // 100
        elif disc_type == 'vahid':
            self.discount_price = self.price - disc_value
        else:
            print('Parametrler duzgun daxil edilmeyib')
            return

    def get_name(self):
        return f'Mehsulun adi: {self.title}'

    def __str__(self):
        if self.__class__.__name__ == 'Book':
            return f'Title: {self.title} | Kitabın yazarı {self.author}'
        elif self.__class__.__name__ == 'Clothes':
            return f'Title: {self.title} | Paltarın rəngi {self.color}'
        else:
            return f'Title: {self.title}'
    
    def __sub__(self, other):
        return self.price - other.price

    def __len__(self):
        if self.__class__.__name__ == 'Book':
            return self.page_count
        elif self.__class__.__name__ == 'Clothes':
            return self.size
        else:
            return 0
    
    def __del__(self): 
        print(f'{self.__class__.__name__} klasinin obyekti silindi!')


class Book(Product):
    next_id = 1
    def __init__(self, language=None, author=None, published_at=None, page_count=None, genre=None, publisher=None, title=None, price=None, prod_cost=None, discount_price=None, description=None, image=None, category=None, rating=None, id=None,):
        super(Book, self).__init__(id, title, price, prod_cost, discount_price, description, image, category, rating)
        self.language = language
        self.author = author
        self.published_at = published_at
        self.page_count = page_count
        self.genre = genre
        self.publisher = publisher
        self.__id = Book.next_id
        Book.next_id += 1

    def get_name(self):
        return f'Kitabin adi: {self.title} | Kitabin yazari: {self.author}'

class Clothes(Product):
    next_id = 1
    def __init__(self, size=None, material=None, color=None, title=None, price=None, prod_cost=None, discount_price=None, description=None, image=None, category=None, brand=None, rating=None, id=None):
        super(Clothes, self).__init__(id, title, price, prod_cost, discount_price, description, image, category, rating)
        self.size = size
        self.material = material
        self.color = color
        self.__id = Clothes.next_id
        Clothes.next_id += 1

    def get_name(self):
        return f'Paltarin adi: {self.title} | Paltarin rengi: {self.color}'

class Electronic(Product):
    def __init__(self, power=None, id=uuid.uuid1(), title=None, rating=None, price=None, prod_cost=None, discount_price=None, description=None, image=None, category=None, brand=None, color=None):
        super().__init__(id, title, rating, price, prod_cost, discount_price, description, image, category, brand, color)
        self.power = power
    
class Phone(Electronic):
    def __init__(self, battery_capacity=None, power=None, id=uuid.uuid1(), title=None, rating=None, price=None, prod_cost=None, discount_price=None, description=None, image=None, category=None, brand=None, color=None):
        super().__init__(id, power, title, rating, price, prod_cost, discount_price, description, image, category, brand, color)
        self.battery_capacity = battery_capacity

class Notebook(Electronic):
    def __init__(self, screen_size=None, power=None, id=uuid.uuid1(), title=None, rating=None, price=None, prod_cost=None, discount_price=None, description=None, image=None, category=None, brand=None, color=None):
        super().__init__(id, power, title, rating, price, prod_cost, discount_price, description, image, category, brand, color)
        self.screen_size = screen_size


###########
# print('-----------------Test Kodlar------------------------')

# tshirt1 = Clothes(14, 'cotton', 'red', 'Tshirt', 100, 80, 99) 
# book1 = Book('English', 'Check London', '2018', 349, 'Adventure', 'Maarif Neshriyyati', 'Mark Tvein', 30, 25, 27)
# book2 = Book('Azerbaycan', 'Axundov', '1996', 400, 'Adventure', 'Maarif Neshriyyati', 'Aldanmish Kevakib', 25, 20, 23)

# print(tshirt1)
# print(book1)

# print(f'book1 - book2 = {book1 - book2}')

# print(f'Sehifelerin sayi(len(book1)): {len(book1)}')

# print(f'Old Price: {book1.price}')
# book1.price = 10
# print(f'New Price: {book1.price}')

# print(f'book1-in id-si: {book1.id}')
# print(f'book2-nin id-si: {book2.id}')

# print('-----------------------------------------')
# print(f'bookun price-na baxiram: {book1.price}')
# print('-----------------------------------------')
############