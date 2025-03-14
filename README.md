class Book:
    def __init__(self, title, isbn, author, length):
        self.title = title
        self.isbn = isbn
        self.author = author
        self.length = length

    def __lt__(self, other):  # For sorting based on ISBN
        return self.isbn < other.isbn

    def __repr__(self): # For easy printing of book object
        return f"Title: {self.title}, ISBN: {self.isbn}, Author: {self.author}, Length: {self.length}"


def selection_sort(books):
    n = len(books)
    swaps = 0
    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if books[j] < books[min_index]:
                min_index = j
        if min_index != i:
            books[i], books[min_index] = books[min_index], books[i]
            swaps += 1
    return books, swaps


books_data = [
    Book("Pride and Prejudice", 9780141439518, "Jane Austen", 448),
    Book("Desiree", 9781842125212, "Annemarie Selinko", 512),
    Book("The Kite Runner", 9781594631931, "Khaled Hosseini", 327),
    Book("Crime & Punishment", 9780553211757, "Fyodor Dostoevsky", 527),
]


sorted_books, num_swaps = selection_sort(books_data.copy())  #Sort a copy to not modify the original


longest_title_book = max(sorted_books, key=lambda book: len(book.title))

print("Sorted Books:")
for book in sorted_books:
    print(book)

print(f"\nNumber of swaps: {num_swaps}")
print(f"\nBook with the longest title: {longest_title_book}")


