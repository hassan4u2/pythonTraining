import csv
from time import sleep


class User:
    def __init__(self, name, email, role):
        self._id = len(usersList) + 1
        self.name = name
        self.email = email
        self.role = role

    def get_id(self):
        return self._id

    def get_name(self):
        return self.name

    def get_email(self):
        return self.email

    def get_role(self):
        return self.role

    def set_id(self, id):
        self._id = id

    def set_name(self, name):
        self.name = name

    def set_email(self, email):
        self.email = email

    def set_role(self, role):
        self.role = role

    def to_dict(self):
        return {
            '_id': self._id,
            'name': self.name,
            'email': self.email,
            'role': self.role
        }


class LibUser(User):
    def __init__(self, name, email):
        super().__init__(name, email, 'user')
        self.books_borrowed = []

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict['books_borrowed'] = self.books_borrowed
        return user_dict

    def search_book():
        pass

    def borrow_book(self, library, book_id):
        book = library.borrow_book(self._id, book_id)
        if not book:
            return None
        self.books_borrowed.append(book)
        library.write_to_csv(
            '_users.csv', [user.to_dict() for user in library.users])
        return book

    def return_book(self, library, book_id):
        book = library.return_book(self._id, book_id)
        if not book:
            return None
        self.books_borrowed.remove(book)
        library.write_to_csv(
            '_users.csv', [user.to_dict() for user in library.users])
        return book

    def extend_loan_period(self, library, book_id):
        book = library.get_book(book_id)
        if not book:
            return None
        if book not in self.books_borrowed:
            return None
        book.loan_period += 7
        library.write_to_csv(
            '_books.csv', [book.to_dict() for book in library.books])
        return book


class LibAdmin(User):
    def __init__(self, name, email):
        super().__init__(name, email, 'admin')

    def add_book(self, library, title, author, num_of_copies, loan_period):
        book = library.add_book(title, author, num_of_copies, loan_period)
        return book

    def remove_book(self, library, book_id):
        book = library.get_book(book_id)
        if not book:
            return None
        library.books.remove(book)
        self.write_to_csv('_books.csv', [book.to_dict()
                          for book in library.books])
        return book

    def search_book(self, library, query):
        return [book for book in library.books if query.lower() in book.title.lower() or query.lower() in book.author.lower()]


class Book:  # Book class
    def __init__(self, title, author, num_of_copies, loan_period):
        self.id = len(open('_books.csv').readlines()) + 1
        self.title = title
        self.author = author
        self.num_of_copies = num_of_copies
        self.num_of_copies_borrowed = 0
        self.num_of_available_copies = num_of_copies - self.num_of_copies_borrowed
        self.loan_period = loan_period

    def get_id(self):
        return self.id

    def get_title(self):
        return self.title

    def get_author(self):
        return self.author

    def get_num_of_copies(self):
        return self.num_of_copies

    def get_num_of_available_copies(self):
        return self.num_of_available_copies

    def get_num_of_copies_borrowed(self):
        return self.num_of_copies_borrowed

    def set_id(self, id):
        self.id = id

    def set_title(self, title):
        self.title = title

    def set_author(self, author):
        self.author = author

    def set_num_of_copies(self, num_of_copies):
        self.num_of_copies = num_of_copies

    def set_num_of_available_copies(self, num_of_available_copies):
        self.num_of_available_copies = num_of_available_copies

    def set_num_of_copies_borrowed(self, num_of_copies_borrowed):
        self.num_of_copies_borrowed = num_of_copies_borrowed

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'author': self.author,
            'num_of_copies': self.num_of_copies,
            'num_of_copies_borrowed': self.num_of_copies_borrowed,
            'num_of_available_copies': self.num_of_available_copies,
            'loan_period': self.loan_period
        }


class LibrarySystem:
    def __init__(self, users, books):
        self.users = users
        self.books = books

    def write_to_csv(self, filename, data):
        with open(filename, 'a') as file:
            writer = csv.DictWriter(file, fieldnames=data[0].keys())
            for row in data:
                writer.writerow(row)

    def UserRegister(self, name, email, role):
        user = LibUser(name, email)
        user._id = len(usersList) + 1
        self.users.append(user)
        self.write_to_csv('_users.csv', [
                          {'_id': user._id, 'name': user.name, 'email': user.email, 'role': user.role, 'books_borrowed': user.books_borrowed or []}])
        return user

    def AdminRegister(self, name, email):
        admin = LibAdmin(name, email)
        admin._id = len(usersList) + 1
        self.users.append(admin)
        self.write_to_csv('_users.csv', [
                          {'_id': admin._id, 'name': admin.name, 'email': admin.email, 'role': admin.role}])
        return admin

    def Login(self, em):
        # print(self.users)
        for user in self.users:
            ema = user['email']
            if ema == em:
                return True, user
        return False, {}


if __name__ == '__main__':
    pass
