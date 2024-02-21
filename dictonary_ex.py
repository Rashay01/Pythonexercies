books = [
    {
        "title": "Infinite Jest",
        "rating": 4.5,
        "genre": "Fiction"
    },
    {
        "title": "A Brief History of Time",
        "rating": 4.8,
        "genre": "Science"
    },
    {
        "title": "The Catcher in the Rye",
        "rating": 3.9,
        "genre": "Fiction"
    },
    {
        "title": "Sapiens",
        "rating": 4.9,
        "genre": "History"
    },
    {
        "title": "Clean Code",
        "rating": 4.7,
        "genre": "Technology"
    },
]

#=====================================================================================
#task 1
best_rated_books = []
for book in books:
  if book["rating"] >= 4.7:
    best_rated_books.append(book["title"])
print(best_rated_books)

#=====================================================================================
#task 2

best_rated_books = [book["title"] for book in books if book["rating"] >= 4.7]
print(best_rated_books)

#=====================================================================================
#task 3

best_rated_books = [book["title"] for book in books if book["rating"] >= 4.7]
best_rated_books.sort()
print(best_rated_books)

#=====================================================================================