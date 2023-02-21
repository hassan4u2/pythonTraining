import csv
from time import sleep


class User:
    def __init__(self, name, email, role):
        self._id = len(usersList) + 1
        self.name = name
        self.email = email
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


class LibAdmin(User):
    def __init__(self, name, email):
        super().__init__(name, email, 'admin')


class Book:  # Book class
    def __init__(self, title, author, num_of_copies, loan_period):
        self.id = len(open('_books.csv').readlines()) + 1
        self.title = title
        self.author = author
        self.num_of_copies = num_of_copies
        self.num_of_copies_borrowed = 0
        self.num_of_available_copies = num_of_copies - self.num_of_copies_borrowed
        self.loan_period = loan_period

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
                return user
            else:
                pass

    def AddBook(self, title, author, num_of_copies, loan_period):
        book = Book(title, author, num_of_copies, loan_period)
        book._id = len(booksList) + 1
        self.books.append(book)
        self.write_to_csv('_books.csv', [{'_id': book._id, 'title': book.title, 'author': book.author, 'num_of_copies': book.num_of_copies,
                          'num_of_copies_borrowed': book.num_of_copies_borrowed, 'num_of_available_copies': book.num_of_available_copies, 'loan_period': book.loan_period}])
        return book

    def RemoveBook(self, book_name):
        for book in self.books:
            if book.title == book_name:
                self.books.remove(book)
                # remove from csv
                with open('_books.csv', 'r') as file:
                    lines = file.readlines()
                    for line in lines:
                        if book_name in line:
                            lines.remove(line)
                            with open('_books.csv', 'w') as file:
                                file.writelines(lines)
                return book
            else:
                pass
        return None

    def SearchBook(self, query):
        # get all books
        books = self.books
        # search for query
        for book in books:
            if query.lower() in book['title'].lower():
                return book
        return None

    def BorrowBook(self, book, user):
        if int(book['num_of_available_copies']) > 0:
            book['num_of_available_copies'] = str(
                int(book['num_of_available_copies']) - 1)
            book['num_of_copies_borrowed'] = str(
                int(book['num_of_copies_borrowed']) + 1)
            list(user['books_borrowed']).append(book)
            # update user line in csv
            with open('_users.csv', 'r') as file:
                lines = file.readlines()
                userObj = f'{user["_id"]}'
                for line in lines:
                    if userObj in line:
                        lines.remove(line)
                        # update line
                        newline = f'{user["_id"]},{user["name"]},{user["email"]},{user["role"]},{user["books_borrowed"]}'
                        lines.append(newline + '\n')
                        # update user csv
                        with open('_users.csv', 'w') as file:
                            file.writelines(lines)
            # update book line in csv
            with open('_books.csv', 'r') as file:
                lines = file.readlines()
                bookObj = f'{book["_id"]}'
                for line in lines:
                    if bookObj in line:
                        lines.remove(line)
                        # update line
                        newline = f'{book["_id"]},{book["title"]},{book["author"]},{book["num_of_copies"]},{book["num_of_copies_borrowed"]},{book["num_of_available_copies"]},{book["loan_period"]}'
                        lines.append(newline + '\n')
                        # update book csv
                        with open('_books.csv', 'w') as file:
                            file.writelines(lines)
            return book
        else:
            return None

    def ReturnBook(self, book, user):
        if book in user['books_borrowed']:
            book['num_of_available_copies'] = str(
                int(book['num_of_available_copies']) + 1)
            book['num_of_copies_borrowed'] = str(
                int(book['num_of_copies_borrowed']) - 1)
            user['books_borrowed'].remove(book)
            # update user line in csv
            with open('_users.csv', 'r') as file:
                lines = file.readlines()
                userObj = f'{user["_id"]}'
                for line in lines:
                    if userObj in line:
                        lines.remove(line)
                        # update line
                        newline = f'{user["_id"]},{user["name"]},{user["email"]},{user["role"]},{user["books_borrowed"]}'
                        lines.append(newline + '\n')
                        # update user csv
                        with open('_users.csv', 'w') as file:
                            file.writelines(lines)
            # update book line in csv
            with open('_books.csv', 'r') as file:
                lines = file.readlines()
                bookObj = f'{book["_id"]}'
                for line in lines:
                    if bookObj in line:
                        lines.remove(line)
                        # update line
                        newline = f'{book["_id"]},{book["title"]},{book["author"]},{book["num_of_copies"]},{book["num_of_copies_borrowed"]},{book["num_of_available_copies"]},{book["loan_period"]}'
                        lines.append(newline + '\n')
                        # update book csv
                        with open('_books.csv', 'w') as file:
                            file.writelines(lines)
            return book
        else:
            return None

    def ExtendLoanPeriod(self, book, user, days):
        if book in user.books_borrowed:
            book.loan_period += days
            # update book line in csv
            with open('_books.csv', 'r') as file:
                lines = file.readlines()
                bookObj = f'{book._id}'
                for line in lines:
                    if bookObj in line:
                        lines.remove(line)
                        # update line
                        newline = f'{book._id},{book.title},{book.author},{book.num_of_copies},{book.num_of_copies_borrowed},{book.num_of_available_copies},{book.loan_period}'
                        lines.append(newline)
                        # update book csv
                        with open('_books.csv', 'w') as file:
                            file.writelines(lines)
            return True
        else:
            return False


if __name__ == '__main__':
    try:
        usersList = []
        with open('_users.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                try:
                    user = {'_id': row[0], 'name': row[1], 'email': row[2],
                            'role': row[3], 'books_borrowed': row[4]}
                except IndexError:
                    user = {'_id': row[0], 'name': row[1], 'email': row[2],
                            'role': row[3], 'books_borrowed': []}
                usersList.append(user)

        booksList = []
        with open('_books.csv', 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                book = {'_id': row[0], 'title': row[1], 'author': row[2], 'num_of_copies': row[3],
                        'num_of_copies_borrowed': row[4], 'num_of_available_copies': row[5], 'loan_period': row[6]}
                booksList.append(book)

    # list index out of range
    except IndexError:
        print("Please check the csv files")
        booksList = []
    except Exception as e:
        print(e)

    while True:
        if not usersList:
            usersList = []
        if not booksList:
            booksList = []
        library = LibrarySystem(usersList, booksList)
        print("\n(LIB) Welcome to the Library System ##")
        print("\t[1] Register as User")
        print("\t[2] Register as Admin")
        print("\t[3] Login")
        print("\t[4] Exit")
        choice = int(input("- Enter your choice: "))
        if choice == 1:  # register as user
            name = input("- Enter your name: ")
            email = input("- Enter your email: ")
            user = library.UserRegister(name, email, 'user')
            print(
                f"[INFO]: User {user.email} has been registered successfully")
        elif choice == 2:  # register as admin
            name = input("- Enter your name: ")
            email = input("- Enter your email: ")
            admin = library.AdminRegister(name, email)
            print(
                f"[INFO]: Admin {admin.email} has been registered successfully")
        elif choice == 3:  # login
            email = input("- Enter your email: ")
            user = library.Login(email)
            if user == None:
                print("[ERROR]: User not found")
                continue
            else:
                user_role = user['role']
                # check if user is a LibUser or LibAdmin object
                if user_role == 'admin':  # login as admin
                    print(f'\nWelcome {user["name"]} (Admin)\n')
                    while True:
                        print("\t[1] Add Book")
                        print("\t[2] Remove Book")
                        print("\t[3] Search Book")
                        print("\t[4] Logout")
                        choice = int(input("- Enter your choice: "))
                        if choice == 1:
                            title = input("- Enter the title of the book: ")
                            author = input("- Enter the author of the book: ")
                            num_of_copies = int(
                                input("- Enter the number of copies: "))
                            loan_period = int(
                                input("- Enter the loan period in days: "))
                            book = library.AddBook(
                                title, author, num_of_copies, loan_period)
                            print(
                                f"[INFO]: Book {book.title} has been added successfully")
                        elif choice == 2:
                            book_name = input(
                                "- Enter the title of the book to delete: ")
                            book = library.RemoveBook(book_name)
                            if book is not None:
                                print(
                                    f"[INFO]: Book {book.title} has been removed successfully")
                            else:
                                print("[RAISE]: Book not found")
                        elif choice == 3:
                            book_name = input(
                                "- Enter the title of the book to search: ")
                            book = library.SearchBook(book_name)
                            if book is not None:
                                print(
                                    f"[INFO]: Book {book['title']} has been found successfully")
                                # test table format
                                print(
                                    f"{'ID':<10}{'Title':<20}{'Author':<20}{'Copies':<10}{'Borrowed':<10}{'Available':<10}{'Loan Period':<10}")
                                print(
                                    f"{book['_id']:<10}{book['title']:<20}{book['author']:<20}{book['num_of_copies']:<10}{book['num_of_copies_borrowed']:<10}{book['num_of_available_copies']:<10}{book['loan_period']:<10}")

                            else:
                                print("[RAISE]: Book not found")
                        elif choice == 4:
                            print("[Bye]: Thank you for using the Library System")
                            exit()
                elif user_role == 'user':  # login as a user
                    print(f'\nWelcome {user["name"]} (User)\n')
                    print("\t[1] Borrow a Book")
                    print("\t[2] Return a Book")
                    print("\t[3] Get your borrowed books")
                    print("\t[4] Extend Loan Period")
                    print("\t[5] Search for a Book")
                    print("\t[6] Logout")
                    choice = int(input("- Enter your choice: "))
                    if choice == 1:
                        book_name = input(
                            "- Enter the title of the book to borrow: ")
                        book_obj = library.SearchBook(book_name)
                        borrow = library.BorrowBook(book_obj, user)
                        if borrow is not None:
                            print(
                                f"[INFO]: Book {book_obj['title']} has been borrowed successfully")
                        else:
                            print("[RAISE]: Book not found")
                    elif choice == 2:
                        book_name = input(
                            "- Enter the title of the book to return: ")
                        book_obj = library.SearchBook(book_name)
                        return_book = library.ReturnBook(book_obj, user)
                        if return_book is not None:
                            print(
                                f"[INFO]: Book {book_obj['title']} has been returned successfully")
                        else:
                            print("[RAISE]: Book not found")
                    elif choice == 3:
                        user_borrowed_books = user['books_borrowed']
                        # table format
                        print(
                            f"{'ID':<10}{'Title':<20}{'Author':<20}{'Copies':<10}{'Borrowed':<10}{'Available':<10}{'Loan Period':<10}")
                        for book_id in user_borrowed_books:
                            book = library.SearchBook(book_id)
                            print(
                                f"{book['_id']:<10}{book['title']:<20}{book['author']:<20}{book['num_of_copies']:<10}{book['num_of_copies_borrowed']:<10}{book['num_of_available_copies']:<10}{book['loan_period']:<10}")
                    elif choice == 4:
                        book_name = input(
                            "- Enter book title to extend the loan period: ")
                        book_obj = library.SearchBook(book_name)
                        days = int(input("- Enter num of exrta days needed: "))
                        extendbook = library.ExtendLoanPeriod(
                            book_obj, user, days)
                        if book is not None:
                            print(
                                f"[INFO]: Loan period of the book {book.title} has been extended successfully")
                        else:
                            print("[RAISE]: Book not found")
                    elif choice == 5:
                        book_name = input(
                            "- Enter the title of the book to search: ")
                        book = library.SearchBook(book_name)
                        if book is not None:
                            print(
                                f"[INFO]: Book {book['title']} has been found successfully")
                            # test table format
                            print(
                                f"{'ID':<10}{'Title':<20}{'Author':<20}{'Copies':<10}{'Borrowed':<10}{'Available':<10}{'Loan Period':<10}")
                            print(
                                f"{book['_id']:<10}{book['title']:<20}{book['author']:<20}{book['num_of_copies']:<10}{book['num_of_copies_borrowed']:<10}{book['num_of_available_copies']:<10}{book['loan_period']:<10}")
                        else:
                            print("[RAISE]: Book not found")
                    elif choice == 6:
                        print("[Bye]: Thank you for using the Library System")
                        exit()

                else:  # invalid role
                    print("Invalid role")
                    continue
        elif choice == 4:  # exit
            print("Thank you for using the Library System")
            exit()
