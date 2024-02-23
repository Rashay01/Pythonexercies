#managae a libary 
library = [
    {"title": "Python Programming", "author": "Eric Matthes", "year": 2019, "available": True},
    {"title": "Automate the Boring Stuff with Python", "author": "Al Sweigart", "year": 2020, "available": True},
    {"title": "Learning Python I", "author": "Mark Lutz", "year": 2013, "available": False},
    {"title": "Fluent Python", "author": "Luciano Ramalho", "year": 2015, "available": True},
    {"title": "Adavance Python", "author": "Mark Lutz", "year": 2015, "available": False},
]
#-------------------------------------------------------------------------------------------
#Task 1
#creat a function given a new book add to libary 
#add_book(libary, new_book)
#Pass by refrence - can be changed 
#Pass by value -  pass the a copy

new_book = {"title": "Test Programming", "author": "Test Test", "year": 2015, 
            "available" : True}

def add_book(library, new_book):
  library.append(new_book)


add_book(library, new_book)
print(library)

#-------------------------------------------------------------------------------------------
#Task 2
#Search books by Author and return it in a list of books
#search_book(libary, author)

def search_by_author(libary, author):
  return [book for book in libary if book["author"] == author]

print()
print()
ans2 = search_by_author(library, "Mark Lutz")
print(ans2)
#-------------------------------------------------------------------------------------------
#Task3
#Check if book exists and if avalible then say its avaliable

def check_out_book(libary, title):
  for book in libary:
    if book["title"] == title and book["available"] is True:
      book["available"] = False
      return "book is avaliable"
  return "book is not avaliable"

print()
print()
ans3 = check_out_book(library, "Python Programming")
print(ans3)
print(library)
print(check_out_book(library,"trim"))

#-------------------------------------------------------------------------------------------
def check_out_book1(libary, title):
  ans = "book does not exist"
  bExist = False
  bAvaliable = False
  for book in libary:
    if book["title"] == title:
      bExist = True
      if book["available"] is True:
        book["available"] = False
        bAvaliable = True
        ans = "book is avaliable"
      break
  if (bExist is True and bAvaliable is False):
    ans = "book is not avaliable"
  return ans

print()
print()
ans3 = check_out_book1(library, "Python Programming")
print(ans3)
print(check_out_book1(library,"trim"))
print(check_out_book1(library,"Adavance Python"))


#----------------------------------------Best Answer------------------------------------
title_given = input("Enter the title of the book to check out: ")

def check_out_book(library, title):
  for book in library:
      if book["title"] == title:
          if book["available"]:
              book["available"] = False
              return(f"The book '{title}' has been checked out.")
          else:
            return(f"The book '{title}' is not available for check out.")
  return (f"The book '{title}' was not found in the library.")

# Call the function to check out a book
check_out_book(library, title_given)

# Display the updated library list
print("Updated library list:")
print(library)