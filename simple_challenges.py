#test if a number is an integer (without using type())

def is_integer(x):
    if abs(x - round(x)) > 0:
        return False
    else:
        return True

print is_integer(7.0) #true
print is_integer(7.5) #false
print is_integer(-1)  #true

#sum each digit of a number together
def digit_sum(n):
    sum= 0
    for digit in str(n):
        sum += int(digit)
    return sum

print digit_sum(12345) #15

#calculate a factorial
def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x-1)

print factorial(4) # 24
print factorial(5) # 120

#determine if a number is prime (note here that break is not needed in order to not execute the else statement, return serves that purpose)
def is_prime(x):
    if x<2:
        return False
    else:
        for n in range(2, x- 1):
            if x % n == 0:
                return False
        return True

print is_prime(0) #false
print is_prime(1) #false
print is_prime(5) #true
print is_prime(16) #false
print is_prime(67) #true

#reverse a string
def reverse(string):
    new_string= ""
    for char in string:
        new_string = char + new_string
    return new_string

print reverse("hello")
print reverse("lets")
print reverse("dance")

#remove vowels
vowels= ["a", "e", "i", "o", "u"]

def anti_vowel(string):
    new_string= ""
    for char in string:
        if char.lower() not in vowels:
            new_string += char
    return new_string

print anti_vowel("All those moments will be lost in time, like tears in rain")

#scrabble score (minus multipliers)
point_allocation = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2,
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3,
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1,
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4,
         "x": 8, "z": 10}

def scrabble_score(word):
    score = 0
    for char in word:
        score += point_allocation[char.lower()]
    return score

print scrabble_score("Void") #8
print scrabble_score("Enigma") #9

#censor out certain words
def censor(text, word):
    text_array = text.split()
    for index, item in enumerate(text_array):
        if item.lower() == word.lower():
            text_array[index] = "*" * len(word)
    new_string = " ".join(text_array)
    return new_string

print censor("this is some crazy shit", "shit")

#count number of times an item appears in a list
def count(sequence, item):
    count = 0
    for num in sequence:
        if num == item:
            count += 1
    return count

print count([1, 2, 1, 2, 1], 1) # 3

#remove odd numbers from list
def purify(lst):
    result = []
    for item in lst:
        if item % 2 == 0:
            result.append(item)
    return result

print purify([1, 2, 3, 4, 5]) #[2, 4]

#multiply all items in a list
def product(lst):
    product = 1
    for item in lst:
        product *= item
    return product

print product([4, 5, 5]) # 100

#get rid of duplicates in a list
def remove_duplicates(lst):
    new_list = []
    for item in lst:
        if item not in new_list:
            new_list.append(item)
    return new_list

print remove_duplicates([1, 2, 3, 3, 2]) #[1, 2, 3]

#find median of a list of numbers
def median(lst):
    sorted_lst = sorted(lst)
    if len(sorted_lst)% 2 == 0:
        median = (sorted_lst[len(sorted_lst)/2- 1] + sorted_lst[len(sorted_lst)/2])/2.0
    else:
        median = sorted_lst[len(sorted_lst)/2]
    return median


print median([7, 12, 3, 1, 6]) #6
print median([4, 5, 5, 4]) #4.5
