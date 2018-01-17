#zip allows us to compare two or more lists at the same time:

list_a = [4, 10, 13, 15, 22]
list_b = [2, 4, 8, 10, 31, 43, 51, 67, 70, 82, 90]
list_c = [0, 1, 2, 3, 43, 45, 7, 22, 68]

#the below will compare a and b (which are arbitrary placeholders), and print the larger
    #note that the comparison stops at the shorter of the two lists!
for a, b in zip(list_a, list_b):
    print max(a, b)

for a, b, c, in zip(list_a, list_b, list_c):
    print max(a, b, c)
