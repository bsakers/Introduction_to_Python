#removing an item from a list (3 options):
    #pop a specific index, and have it returned
n= [1, 2, 5, 9]
n.pop(1)
print n

    #remove a specific item (not the index)
n = [1, 2, 5, 9]
n.remove(9)
print n
array = ["one", "two", "three"]
array.remove("three")
print array

    #delete a specific index, but don't return it
n= [1, 2, 5, 9]
del(n[0])
print n


#easy to modify lists inside functions:
def my_add_function(numbers):
    numbers[0]= numbers[0] + 2
    return numbers

n= [1, 2, 3, 4]
print my_add_function(n)

def my_append_function(numbers):
    numbers.append(9)
    return numbers

n= [1, 2, 3, 4]
print my_append_function(n)

def my_double_list_function(lst):
    for i in range(0, len(lst)):
        lst[i]= lst[i] * 2
    return lst

n= [1, 2, 3, 4]
print my_double_list_function(n)

def list_total(lst):
    total = 0
    for i in range(len(lst)):
        total += lst[i]
    return total

n = [1, 2, 3, 4]
print list_total(n)

#we can do the same for strings
def join_names(words):
    new_word = ""
    for i in range(len(words)):
        new_word += words[i]
    return new_word

names = ["Brian", "Spencer", "Akers"]
print join_names(names)

#there is a built in function to help with this though! Note that between the "" can be replaced with anything
print " ".join(names)

#we can also add lists in our functions
def join_lists(lst1, lst2):
    return lst1 + lst2

x = [0, 1, 2]
y = [3, 4, 5]
print join_lists(x, y)
x = ["Brian", "Han"]
y = ["The Dude", "Walter"]
print join_lists(x, y)

#looping through lists within lists
n= [[1, 2, 3], [4, 5, 6, 7, 8, 9]]

def single_list(lists):
    new_list = []
    for i in range(len(lists)):
        for j in range(len(lists[i])):
            new_list.append(lists[i][j])
    return new_list

print single_list(n)

#another way to complete the above:
def sing_list(lists):
    new_list = []
    for lst in lists:
        for item in lst:
            new_list.append(item)
    return new_list

print sing_list(n)
