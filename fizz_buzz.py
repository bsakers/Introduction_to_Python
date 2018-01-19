# Write a program that prints out the numbers from 1 to 100, each on a new line.
    # If the number is divisible by 3, print out the word "Fizz" instead.
    # If the number is divisible by 5, print out the word "Buzz" instead.
    # If the number is divisible by 3 and 5, print out the word "FizzBuzz" instead.

count = 1
while count <=100:
    if count % 3 == 0 and count % 5 != 0:
        print "Fizz"
    elif count % 5 == 0 and count % 3 != 0:
        print "Buzz"
    elif count % 5 == 0 and count % 3 == 0:
        print "FizzBuzz"
    else:
        print count
    count += 1
