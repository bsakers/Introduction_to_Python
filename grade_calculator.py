grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]
from math import sqrt

def grades_sum(scores):
    total = 0
    for score in scores:
        total += score
    return total

print grades_sum(grades)

def grades_average(grades_input):
    return grades_sum(grades_input) / float(len(grades_input))

print grades_average(grades)

def grades_variance(scores):
    average = grades_average(scores)
    variance = 0
    for score in scores:
        variance += (average - score) ** 2
    return variance / float(len(scores)-1)

print grades_variance(grades)

def standard_deviation(scores):
    return sqrt(grades_variance(scores))

example_data = [727.7, 1086.5, 1091, 1361.3, 1490.5, 1956.1]
print standard_deviation(example_data)
