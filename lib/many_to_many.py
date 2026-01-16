# many_to_many.py

class Author:
    def __init__(self, name):
        self.name = name

    def contracts(self):
        from many_to_many import Contract
        return [c for c in Contract.all if c.author == self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        from many_to_many import Contract
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Book:
    def __init__(self, title):
        self.title = title

    def contracts(self):
        from many_to_many import Contract
        return [c for c in Contract.all if c.book == self]

    def authors(self):
        return [c.author for c in self.contracts()]


class Contract:
    all = []  # must match test expectations

    def __init__(self, author, book, date, royalties):
        from many_to_many import Author, Book

        if not isinstance(author, Author):
            raise Exception("Author must be an Author instance")
        if not isinstance(book, Book):
            raise Exception("Book must be a Book instance")
        if not isinstance(date, str) or not date.strip():
            raise Exception("Date must be a non-empty string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a positive integer")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [c for c in cls.all if c.date == date]

    @classmethod
    def reset(cls):
        cls.all = []