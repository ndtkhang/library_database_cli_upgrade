import pandas as pd
from book import Book
import csv
from sqlalchemy import create_engine

def main():
    print("\nWelcome to the library, librarian!")
    inputStop = False
    books = []
    while inputStop == False:
        action = input("\nEnter a number to select an action:\n"
                       "0 - Stop the program\n"
                       "1 - Import a book manually\n"
                       "2 - Import a .csv file\n"
                       "3 - Export a .csv file\n"
                       "4 - Export a database\n"
                       "Enter: ")
        if action == "0":
            inputStop = True
        elif action == "1":
            book_info = ["book_id", "title", "authors", "avg_rating", "isbn", "isbn13", "language_code", "num_pages", "ratings_count", "text_reviews_count", "publication_date", "publisher"]
            input_book_datas = []
            for header in book_info:
                data_input = input("Enter {}:".format(header))
                input_book_datas.append(data_input) # Put all user input into a list of strings
            book = Book(*input_book_datas) # Pass those book infos into an instance of the imported Book class
            books.append(book) # add the book user just input into a list of book instances to wait for more user input 
            print("You've imported a book, you can import more books manually or through a .csv file.\n")
        elif action == "2":
            input_csv = input("Enter the name of the .csv file to import data: ")
            with open(input_csv, mode="r", newline="") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    book = Book(row["book_id"], row["title"],row["authors"],row["avg_rating"],row["isbn"],row["isbn13"],row["language_code"],row["num_pages"],row["ratings_count"],row["text_reviews_count"],row["publication_date"],row["publisher"])
                    books.append(book)
                print("You've imported all books from {}, you can import more books manually or through another .csv file.\n".format(input_csv))
        elif action == "3":
            df = pd.DataFrame([book.__dict__ for book in books]) # list of objects -> list of dictionaries -> pandas data frame
            df.to_csv('output.csv')
        elif action == "4":
            table_name = input("Enter the name of the table to store the data: ")
            df = pd.DataFrame([book.__dict__ for book in books]) # list of objects -> list of dictionaries -> pandas data frame
            engine = create_engine("sqlite:///mylibrary.db")
            df.to_sql(table_name, con=engine, if_exists="replace", index=False)
            print("Table added to mylibrary.db database! The table will replace any table with the same name!")
            print("To view table in database, make sure to install sqllite")
        else:
            print("Invalid Number!")

if __name__ == "__main__":
    main()