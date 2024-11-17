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



#The dictionary read was made when talking to Coleton O'Donnell, writing part of it together.

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

#making reading easier by making class object Movie and placing all instances of objects in csv_dict_list that had a rating in that list

movie_with_ratings = []

for entry in csv_dict_list:
    if entry["rating"] != "":
        movie_with_ratings.append(Movie(entry["movie_id"], entry["movie_name"], entry["year"], entry["certificate"], entry["runtime"], entry["genre"], entry["rating"], entry["description"], entry["director"], entry["director_id"], entry["star"], entry["star_id"], entry["votes"], entry["gross(in $)"]))

#lists with movie ratings bundled in

movies_0to2= []
movies_2to4 = []
movies_4to6 = []
movies_6to8 = []
movies_8to9 = []
movies_9to10 = []
count = 0

for entry in movie_with_ratings:
    if float(entry.rating) <= 1.9:
        movies_0to2.append(entry)
    else:
        if float(entry.rating) <= 4.0:
            movies_2to4.append(entry)
        else:
            if float(entry.rating) <= 6.0:
                movies_4to6.append(entry)
            else:
                if float(entry.rating) <= 8.0:
                    movies_6to8.append(entry)
                else:
                    if float(entry.rating) <= 9.0:
                        movies_8to9.append(entry)
                    else:
                        movies_9to10.append(entry)




#used geeksforgeeks.com/how-to-measure-elapsed-time-in-python as reference

# code_segment = '''\
# import sortingFunctionality
# test = [3, 2, 50, 1, 100, 2.5]
# sortingFunctionality.mergeSort(test, 0 , 5)
# '''
#
# sortingTime =  timeit.timeit(code_segment, number=1000000)
# print(f"{sortingTime:.03f} seconds")

# for entry in csv_dict_list:
#     if entry["rating"] == "8.0":
#         count+=1
#
# print(count)