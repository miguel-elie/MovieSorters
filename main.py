import glob
import os
import csv
import sortingFunctionality
import movies
import timeit

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

count = 0

#lists with movie ratings bundled in
#for example: movies_1 is all movies with IMDb scores between 0 and 1
#movies_2 is all movies with IMDb scores between 1 and 2

movie_with_ratings = []
movies_1 = []
movies_2 = []
movies_3 = []
movies_4 = []
movies_5 = []
movies_6 = []
movies_7 = []
movies_8 = []
movies_9 = []

#used geeksforgeeks.com/how-to-measure-elapsed-time-in-python as reference

code_segment = '''\
import sortingFunctionality
test = [3, 2, 50, 1, 100, 2.5]
sortingFunctionality.mergeSort(test, 0 , 5)
'''

sortingTime =  timeit.timeit(code_segment, number=1000000)
print(f"{sortingTime:.03f} seconds")

# for entry in csv_dict_list:
#     if entry["rating"] == "8.0":
#         count+=1
#
# print(count)