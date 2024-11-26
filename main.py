import glob
import os
import csv
import sortingFunctionality
import timeit


class Movie:
    def __init__(self, movie_id, movie_name, year, certificate, runtime, genre, rating, description, director, director_id, star, star_id, votes, gross):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.year = year
        self.certificate = certificate
        self.runtime = runtime
        self.genre = genre
        self.rating = rating
        self.description = description
        self.director = director
        self.director_id = director_id
        self.star = star
        self.star_id = star_id
        self.votes = votes
        self.gross = gross


# COP3530 Module 6 Sorting Notes referenced when making the mergeSort and merge functions
def mergeSort(ratings: list[Movie], left: float, right: float):
    if left < right:
        middle = left + (right - left) // 2
        mergeSort(ratings, left, middle)
        mergeSort(ratings, middle + 1, right)
        merge(ratings, left, middle, right)


def merge(ratings: list[Movie], left: float, middle: float, right: float):
    n1 = middle - left + 1
    n2 = right - middle
    X = [0] * n1
    Y = [0] * n2
    for i in range(n1):
        X[i] = ratings[left + i]
    for i in range(n2):
        Y[i] = ratings[middle + 1 + i]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if float(X[i].votes) >= float(Y[j].votes):
            ratings[k] = X[i]
            i += 1
        else:
            ratings[k] = Y[j]
            j += 1
        k += 1
    while i < n1:
        ratings[k] = X[i]
        i += 1
        k += 1
    while j < n2:
        ratings[k] = Y[j]
        j += 1
        k += 1

def mergeSortLIST(ratings, left: float, right: float):
    if left < right:
        middle = left + (right - left) // 2
        mergeSortLIST(ratings, left, middle)
        mergeSortLIST(ratings, middle + 1, right)
        mergeLIST(ratings, left, middle, right)


def mergeLIST(ratings: list[Movie], left: float, middle: float, right: float):
    n1 = middle - left + 1
    n2 = right - middle
    X = [0] * n1
    Y = [0] * n2
    for i in range(n1):
        X[i] = ratings[left + i]
    for i in range(n2):
        Y[i] = ratings[middle + 1 + i]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if float(X[i]) >= float(Y[j]):
            ratings[k] = X[i]
            i += 1
        else:
            ratings[k] = Y[j]
            j += 1
        k += 1
    while i < n1:
        ratings[k] = X[i]
        i += 1
        k += 1
    while j < n2:
        ratings[k] = Y[j]
        j += 1
        k += 1

# Quick Sort Implementation
# Added Quick Sort to sort movies based on their votes
def quickSort(ratings: list[Movie], low: int, high: int):
    if low < high:
        pi = partition(ratings, low, high)
        quickSort(ratings, low, pi - 1)
        quickSort(ratings, pi + 1, high)


def partition(ratings: list[Movie], low: int, high: int):
    pivot = float(ratings[high].votes)
    i = low - 1
    for j in range(low, high):
        if float(ratings[j].votes) >= pivot:
            i += 1
            ratings[i], ratings[j] = ratings[j], ratings[i]
    ratings[i + 1], ratings[high] = ratings[high], ratings[i + 1]
    return i + 1

def quickSortLIST(ratings, low: int, high: int):
    if low < high:
        pi = partitionLIST(ratings, low, high)
        quickSortLIST(ratings, low, pi - 1)
        quickSortLIST(ratings, pi + 1, high)


def partitionLIST(ratings, low: int, high: int):
    pivot = float(ratings[high])
    i = low - 1
    for j in range(low, high):
        if float(ratings[j]) >= pivot:
            i += 1
            ratings[i], ratings[j] = ratings[j], ratings[i]
    ratings[i + 1], ratings[high] = ratings[high], ratings[i + 1]
    return i + 1

# The dictionary read was made when talking to Coleton O'Donnell, writing part of it together.

# Specify the directory and pattern
directory = './archive/'
pattern = '*.csv'

csv_list = glob.glob(os.path.join(directory, pattern))

csv_dict_list = []

# Iterate over the list of CSVs
for filepath in csv_list:
    if os.path.isfile(filepath):
        # Open the CSV file
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            # Create a CSV reader
            reader = csv.DictReader(csvfile)
            csv_dict_list += list(reader)

# Making reading easier by making class object Movie and placing all instances of objects in csv_dict_list that had a rating in that list
movie_with_ratings = []

for entry in csv_dict_list:
    if entry["rating"] != "":
        movie_with_ratings.append(Movie(entry["movie_id"], entry["movie_name"], entry["year"], entry["certificate"],
                                        entry["runtime"], entry["genre"], entry["rating"], entry["description"],
                                        entry["director"], entry["director_id"], entry["star"], entry["star_id"],
                                        entry["votes"], entry["gross(in $)"]))

# Lists with movie ratings bundled in

# Method 1: map/dictionary with the key being the rating and the value being a list of objects with that rating
movies_dict = {}
final_movie_dict = {}
ratings_dict = {}
genre_dict = {}
for entry in movie_with_ratings:
    if entry.movie_name in movies_dict:
        if entry.description not in movies_dict[entry.movie_name]:
            movies_dict[entry.movie_name].append(entry)
    else:
        movies_dict[entry.movie_name] = [entry]

for entry in movie_with_ratings:
    if entry.movie_name not in final_movie_dict:
        final_movie_dict[entry.movie_name] = entry

for key, value in movies_dict.items():
    for entry in value:
        if entry.rating in ratings_dict:
            ratings_dict[entry.rating].append(entry)
        else:
            ratings_dict[entry.rating] = [entry]

for key, value in final_movie_dict.items():
    if value.genre in genre_dict:
        genre_dict[value.genre].append(entry)
    else:
        genre_dict[value.genre] = [entry]


# Use both Merge Sort and Quick Sort to sort the ratings
for key, value in ratings_dict.items():
    # Merge Sort
    merge_sorted = value[:]
    mergeSort(value, 0, len(merge_sorted) - 1)


code_segment_merge = '''\
import glob
import os
import csv
import sortingFunctionality
import timeit


class Movie:
    def __init__(self, movie_id, movie_name, year, certificate, runtime, genre, rating, description, director, director_id, star, star_id, votes, gross):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.year = year
        self.certificate = certificate
        self.runtime = runtime
        self.genre = genre
        self.rating = rating
        self.description = description
        self.director = director
        self.director_id = director_id
        self.star = star
        self.star_id = star_id
        self.votes = votes
        self.gross = gross


# COP3530 Module 6 Sorting Notes referenced when making the mergeSort and merge functions
def mergeSort(ratings: list[Movie], left: float, right: float):
    if left < right:
        middle = left + (right - left) // 2
        mergeSort(ratings, left, middle)
        mergeSort(ratings, middle + 1, right)
        merge(ratings, left, middle, right)


def merge(ratings: list[Movie], left: float, middle: float, right: float):
    n1 = middle - left + 1
    n2 = right - middle
    X = [0] * n1
    Y = [0] * n2
    for i in range(n1):
        X[i] = ratings[left + i]
    for i in range(n2):
        Y[i] = ratings[middle + 1 + i]
    i = 0
    j = 0
    k = left
    while i < n1 and j < n2:
        if float(X[i].votes) >= float(Y[j].votes):
            ratings[k] = X[i]
            i += 1
        else:
            ratings[k] = Y[j]
            j += 1
        k += 1
    while i < n1:
        ratings[k] = X[i]
        i += 1
        k += 1
    while j < n2:
        ratings[k] = Y[j]
        j += 1
        k += 1

# The dictionary read was made when talking to Coleton O'Donnell, writing part of it together.

# Specify the directory and pattern
directory = './archive/'
pattern = '*.csv'

csv_list = glob.glob(os.path.join(directory, pattern))

csv_dict_list = []

# Iterate over the list of CSVs
for filepath in csv_list:
    if os.path.isfile(filepath):
        # Open the CSV file
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            # Create a CSV reader
            reader = csv.DictReader(csvfile)
            csv_dict_list += list(reader)

# Making reading easier by making class object Movie and placing all instances of objects in csv_dict_list that had a rating in that list
movie_with_ratings = []

for entry in csv_dict_list:
    if entry["rating"] != "":
        movie_with_ratings.append(Movie(entry["movie_id"], entry["movie_name"], entry["year"], entry["certificate"],
                                        entry["runtime"], entry["genre"], entry["rating"], entry["description"],
                                        entry["director"], entry["director_id"], entry["star"], entry["star_id"],
                                        entry["votes"], entry["gross(in $)"]))

# Lists with movie ratings bundled in

# Method 1: map/dictionary with the key being the rating and the value being a list of objects with that rating
movies_dict = {}
ratings_dict = {}
for entry in movie_with_ratings:
    if entry.movie_name in movies_dict:
        if entry.description not in movies_dict[entry.movie_name]:
            movies_dict[entry.movie_name].append(entry)
    else:
        movies_dict[entry.movie_name] = [entry]

for key, value in movies_dict.items():
    for entry in value:
        if entry.rating in ratings_dict:
            ratings_dict[entry.rating].append(entry)
        else:
            ratings_dict[entry.rating] = [entry]

# Use both Merge Sort and Quick Sort to sort the ratings
for key, value in ratings_dict.items():
    # Merge Sort
    merge_sorted = value[:]
    mergeSort(merge_sorted, 0, len(merge_sorted) - 1)
'''

code_segment_quick = '''
import glob
import os
import csv
import sortingFunctionality
import timeit


class Movie:
    def __init__(self, movie_id, movie_name, year, certificate, runtime, genre, rating, description, director, director_id, star, star_id, votes, gross):
        self.movie_id = movie_id
        self.movie_name = movie_name
        self.year = year
        self.certificate = certificate
        self.runtime = runtime
        self.genre = genre
        self.rating = rating
        self.description = description
        self.director = director
        self.director_id = director_id
        self.star = star
        self.star_id = star_id
        self.votes = votes
        self.gross = gross
# Quick Sort Implementation
# Added Quick Sort to sort movies based on their votes
def quickSort(ratings: list[Movie], low: int, high: int):
    if low < high:
        pi = partition(ratings, low, high)
        quickSort(ratings, low, pi - 1)
        quickSort(ratings, pi + 1, high)


def partition(ratings: list[Movie], low: int, high: int):
    pivot = float(ratings[high].votes)
    i = low - 1
    for j in range(low, high):
        if float(ratings[j].votes) >= pivot:
            i += 1
            ratings[i], ratings[j] = ratings[j], ratings[i]
    ratings[i + 1], ratings[high] = ratings[high], ratings[i + 1]
    return i + 1


# The dictionary read was made when talking to Coleton O'Donnell, writing part of it together.

# Specify the directory and pattern
directory = './archive/'
pattern = '*.csv'

csv_list = glob.glob(os.path.join(directory, pattern))

csv_dict_list = []

# Iterate over the list of CSVs
for filepath in csv_list:
    if os.path.isfile(filepath):
        # Open the CSV file
        with open(filepath, 'r', encoding='utf-8') as csvfile:
            # Create a CSV reader
            reader = csv.DictReader(csvfile)
            csv_dict_list += list(reader)

# Making reading easier by making class object Movie and placing all instances of objects in csv_dict_list that had a rating in that list
movie_with_ratings = []

for entry in csv_dict_list:
    if entry["rating"] != "":
        movie_with_ratings.append(Movie(entry["movie_id"], entry["movie_name"], entry["year"], entry["certificate"],
                                        entry["runtime"], entry["genre"], entry["rating"], entry["description"],
                                        entry["director"], entry["director_id"], entry["star"], entry["star_id"],
                                        entry["votes"], entry["gross(in $)"]))

# Lists with movie ratings bundled in

# Method 1: map/dictionary with the key being the rating and the value being a list of objects with that rating
movies_dict = {}
ratings_dict = {}
for entry in movie_with_ratings:
    if entry.movie_name in movies_dict:
        if entry.description not in movies_dict[entry.movie_name]:
            movies_dict[entry.movie_name].append(entry)
    else:
        movies_dict[entry.movie_name] = [entry]

for key, value in movies_dict.items():
    for entry in value:
        if entry.rating in ratings_dict:
            ratings_dict[entry.rating].append(entry)
        else:
            ratings_dict[entry.rating] = [entry]

# Use both Merge Sort and Quick Sort to sort the ratings
for key, value in ratings_dict.items():
    # Quick Sort
    quick_sorted = value[:]
    quickSort(quick_sorted, 0, len(quick_sorted) - 1)
'''
# print("LOADING MOVIESORTER")
# sortingTimeMerge = timeit.timeit(code_segment_merge, number=3)
# sortingTimeMerge = sortingTimeMerge/3
# print("LOADING MOVIESORTER")
# sortingTimeQuick = timeit.timeit(code_segment_quick, number=3)
# sortingTimeQuick = sortingTimeQuick/3
# print(f"\nInitial Average Merge Sort Time: {sortingTimeMerge:.04f} seconds")
# print(f"Initial Average Quick Sort Time: {sortingTimeQuick:.04f} seconds")

set_of_ratings = set({})
for key, value in ratings_dict.items():
    set_of_ratings.add(key)
list_of_ratings = list(set_of_ratings)
quickSortLIST(list_of_ratings, 0, len(list_of_ratings)-1)

print("\n\n");
print("Welcome to Movie Sorter: Where you can find the highest rated films based on your genre preference")
print("The available genres are: Action (A), Adventure (AD), Animation (AN), Biography (B), Crime (C), Family (FAM), Fantasy (FAN), Film-Noir (FN), History (HIS), Horror (HOR), Mystery (MYS), Romance (ROM), SciFi (SCI), Sports (SPO), Thriller (T), and War (W)")
notQuit = True

while notQuit:
    inp = input("Enter the movie name or quit to stop\n")
    if inp == "quit" or inp == "Quit" or inp == "QUIT":
        notQuit = False
    if inp in final_movie_dict:
        for key, value in ratings_dict.items():
            for entry in value:
                if entry.genre == final_movie_dict[inp].genre:
                    print(f"{entry.movie_name}, Rating: {entry.rating}, Votes: {entry.votes}")




# Used geeksforgeeks.com/how-to-measure-elapsed-time-in-python as reference
