#make a list of 0- 50, only even integers
evens_to_50 = [i for i in range(51) if i % 2 == 0]
print evens_to_50

#general syntax:
new_list = [x for x in range(1, 6)]
    #the above will form [1, 2, 3, 4, 5]. Note that we didnt "do" anything to x
print new_list

doubles = [x * 2 for x in range(1, 6)]
    #the above will double each number from 1- 5
print doubles

doubles_by_three = [x * 2 for x in range(1, 7) if (x * 2) % 3 == 0]
print doubles_by_three
    #the above will generate a list of doubles between 1 and 6, only if that number is divisible by 3

even_squares = [x**2 for x in range(1, 11) if (x**2)%2 == 0]
print even_squares
    #the above will generate the sqaures of all even numbers 1 through 10

c = ['C' for x in range(5) if x < 3]
print c
    #the above will generate ['C', 'C', 'C']. Note the list length is 3, since we only have 3 values in range 5 where x < 3

cubes_by_four= [x**3 for x in range(1, 11) if (x**3) % 4 == 0]
print cubes_by_four
    #[8, 64, 216, 512, 1000]

threes_and_fives = [x for x in range(1, 16) if x % 3 == 0 or x % 5 == 0]
print threes_and_fives
    #[3, 5, 6, 9, 10, 12, 15]
