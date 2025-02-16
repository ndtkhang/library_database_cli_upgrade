class Book:

    def __init__(self, book_id, title, authors, avg_rating, isbn, isbn13, language_code, num_pages, ratings_count, text_reviews_count, publication_date, publisher):
        self.book_id = book_id
        self.title = title
        self.authors = authors
        self.avg_rating = avg_rating
        self.isbn = isbn
        self. isbn13 = isbn13
        self.language_code = language_code
        self.num_pages = num_pages
        self.ratings_count = ratings_count
        self.text_reviews_count = text_reviews_count
        self.publication_date = publication_date
        self.publisher = publisher

    def __str__ (self):
        return (
            f"Book(\n"
            f"  book_id: {self.book_id}\n"
            f"  title: {self.title}\n"
            f"  authors: {self.authors}\n"
            f"  avg_rating: {self.avg_rating}\n"
            f"  isbn: {self.isbn}\n"
            f"  isbn13: {self.isbn13}\n"
            f"  language_code: {self.language_code}\n"
            f"  num_pages: {self.num_pages}\n"
            f"  ratings_count: {self.ratings_count}\n"
            f"  text_reviews_count: {self.text_reviews_count}\n"
            f"  publication_date: {self.publication_date}\n"
            f"  publisher: {self.publisher}\n"
            f")"
        )