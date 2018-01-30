l = [i ** 2 for i in range(1, 11)]
    #the above list comprehension generates [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print l[2:9:2]
    #will return [9, 25, 49, 81]

#sytax is [start:stop:stride]
    #start defaults to index 0
    #stop defaults to the last index
    #stride defaults to 1 (how many to skip per iteration)

my_list = range(1, 11) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print my_list[::2]
    #the above will return [1, 3, 5, 7, 9]. Note that it skipped every other

#you can even reverse a list with a -1 stride
letters = ['A', 'B', 'C', 'D', 'E']
print letters[::-1]
    #the above will return ['E', 'D', 'C', 'B', 'A']. Think of this just working backwards
    #it essentially sets the start point as -1. In other words [-1::-1] will return the same thing

#can stride by -n
to_one_hundred = range(101)
backwards_by_tens = to_one_hundred[::-10]
print backwards_by_tens
    #[100, 90, 80, 70, 60, 50, 40, 30, 20, 10, 0]

#note that to include start and stride, but NOT stop, you need a secondary colon
to_21 = range(0,22)
odd_numbers = to_21[1::2]
print odd_numbers
    #the above will start at index one, end at the last index, and skip every other item
    #[1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

garbled_message = "!XeXgXaXsXsXeXmX XtXeXrXcXeXsX XeXhXtX XmXaX XI"
translated_message = garbled_message[::-2]
print translated_message
    #"I am the secret message!"
