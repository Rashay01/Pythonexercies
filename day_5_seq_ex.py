#Create a list with the average rating of each movie
#Task 1
#Using map, filter, all

movies = [
    {
        "title": "Inception",
        "ratings": [5, 4, 5, 4, 5]
    },
    {
        "title": "Interstellar",
        "ratings": [5, 5, 4, 5, 4]
    },
    {
        "title": "Dunkirk",
        "ratings": [4, 4, 4, 3, 4]
    },
    {
        "title": "The Dark Knight",
        "ratings": [5, 5, 5, 5, 5]
    },
    {
        "title": "Memento",
        "ratings": [4, 5, 4, 5, 4]
    },
]

#Task 1
# movie_titles = map(lambda movie: movie["title"], movies)

# print(list(movie_titles))
#Task 1.1
avg_rateings = map(lambda x: sum(x["ratings"]) / len(x["ratings"]), movies)
print(list(avg_rateings))

# #Task 1.2
# print()
movies_final_avg = map(
    lambda x: { **x, "average_rating": sum(x["ratings"]) / len(x["ratings"])}, movies)
print(list(movies_final_avg))

# print()
# movie_avg = lambda movie: sum(movie["ratings"])/len(movie["ratings"])
# movies_final1 = map(lambda movie: {**movie,"average_rating": movie_avg(movie)}, movies)
# print(list(movies_final1))

# #Task2
# best_movie = max(
#     movies, key=lambda movie: sum(movie["ratings"]) / len(movie["ratings"]))
# print(f'The top rated movie is "{best_movie["title"]}"')

# # av = list(movies_final)
# # best_movie1 = max(
# #   av, key= lambda movie: movie["average_rating"])
# # print(f'The top rated movie is "{best_movie["title"]}"')

# #Task3
# # Movies with ratings more than 4.6

movie_avg1 = lambda movie: (sum(movie["ratings"])/len(movie["ratings"])) >=4.6
movies_final1 = filter(movie_avg1, movies)
top_rated_movies = map(lambda movie: movie["title"], movies_final1)
print(list(top_rated_movies))

movie_greater = lambda movie: movie["average_rating"] >=4.6
movies_final2 = filter(movie_greater, movies_final_avg)
top_rated_movies = map(lambda movie: movie["title"], movies_final2)
print(list(movies_final2))

#Task4

movie_avg = lambda movie: sum(movie["ratings"]) / len(movie["ratings"])
movies_avg_sorted = sorted(movies, key=movie_avg, reverse=True)
names_list = list(map(lambda movie: movie["title"], movies_avg_sorted))
print(names_list)

#Task5
movie_avg = lambda movie: sum(movie["ratings"]) / len(movie["ratings"])
movies_avg_sorted = sorted(movies, key=movie_avg, reverse=True)
names_list = list(map(lambda movie: movie["title"], movies_avg_sorted))
print(", ".join(names_list[:3]))