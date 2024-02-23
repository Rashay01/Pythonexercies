#Create a list with the average rating of each movie
#Task 1
#Using map, filter, all

movies = [
    {"title": "Inception", "ratings": [5, 4, 5, 4, 5]},
    {"title": "Interstellar", "ratings": [5, 5, 4, 5, 4]},
    {"title": "Dunkirk", "ratings": [4, 4, 4, 3, 4]},
    {"title": "The Dark Knight", "ratings": [5, 5, 5, 5, 5]},
    {"title": "Memento", "ratings": [4, 5, 4, 5, 4]},
]

movie_titles = map(lambda movie: movie["title"], movies)

print(list(movie_titles))

avg_rateings = map(lambda x: sum(x["ratings"])/len(x["ratings"]), movies)
print(list(avg_rateings))



movies_final = map(lambda x: {**x, "avgerage_rating" : sum(x["ratings"])/len(x["ratings"])}, movies)
print(list(movies_final))

avg_func = lambda movie: sum(movie["ratings"])/len(movie["ratings"])
movies_final1 = map(lambda movie: {**movie, "avgerage_rating":avg_func}, movies)
print(list(movies_final1))

