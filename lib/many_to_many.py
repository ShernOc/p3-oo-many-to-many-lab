
class Author:
    all = []
    def __init__(self,name):
        self.name = name 
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]
        
    def books(self):
            return [book for book in Book.all] 
    
    def sign_contract(self,book,date,royalties):
        #return a new Contract object
        return Contract(author = self, book = book, date=date,royalties=royalties) 
    
    def total_royalties(self):
        #return total amount of royalties that the author has earned. 
        total = 0
        for royal in self.contracts():
            total +=royal.royalties
        return total
    
class Book:
    all = []
    
    def __init__(self,title):
        self.title = title 
        self.contract = []
        Book.all.append(self)
        
    def contracts(self):
        return [contract for contract in Contract.all if contract.book ==self]# return a list of its contracts based on the book 
    def authors(self):
        return [author for author in Author.all] # return the list of the authors 
    
class Contract:
    all = []
    def __init__(self,author,book,date,royalties):
        self.author = author 
        self.book = book
        self.date = date 
        self.royalties = royalties
        Contract.all.append(self)
          
    @property
    def author(self):
        return self._author

    #setter 
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("Author, must be an instance of the Author class")
        self._author = value
        
    @property 
    def book(self):
        return self._book 
        
    #setter 
    @book.setter 
    def book(self,value):
        if not isinstance(value,Book):
            raise Exception ("Book, must be an instance of Book class ")
        self._book = value 
        
    @property
    def date(self):
        return self._date
    
    #date setter 
    @date.setter
    def date(self,value):
        if not isinstance(value, str):
            raise Exception("The date property should be a string ")
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    #royalties setter 
    @royalties.setter 
    def royalties(self,value):
        if not isinstance(value,int):
            raise Exception("The royalties properties should be a number")
        self._royalties =value 
        
    @classmethod
    def contracts_by_date(cls, date):
         #return all contracts that have the same date as the date passed into the method 
        return [contract for contract in cls.all if contract.date == date]
        
    
   
        
      
       
       