import math
import string
import numpy


def update_words(param):
    for i in param:
        if i not in givenWords:
            givenWords.append(i)


def mathematical_function(value):
    return math.log(count / value)


# values
count = int(input())
strings = [""] * (count + 1)  # chiz
givenWords = []

# inputs
for i in range(count):
    strings[i] = input().translate(str.maketrans('', '', string.punctuation)).lower().strip().split()
    update_words(strings[i])
query = input().translate(str.maketrans('', '', string.punctuation)).lower().strip().split()

# temp
update_words(query)
strings[count] = query
count += 1

# data sets
my_matrix = numpy.empty((count, len(givenWords)))
my_query = numpy.empty((1, len(givenWords)))
my_array = numpy.empty((1, len(givenWords)))

# calculate
for i in range(count):
    for j in range(len(givenWords)):
        my_matrix[i][j] = strings[i].count(givenWords[j]) / len(strings[i])
for i in range(len(givenWords)):
    my_query[0][i] = query.count(givenWords[i]) / len(query)
for index, value in enumerate(numpy.count_nonzero(my_matrix != 0, axis=0)):
    my_array[0][index] = mathematical_function(value)

my_matrix = numpy.multiply(my_matrix, my_array)
my_query = numpy.multiply(my_query, my_array)

max = 0
ans = 0
for i in range(count - 1):
    temp = numpy.dot(my_query, my_matrix[i][:]) / numpy.linalg.norm(my_query)
    # numpy.linalg.norm(my_query - my_matrix[i][:])
    if (temp > max):
        max = temp
        ans = i
print(ans + 1)
