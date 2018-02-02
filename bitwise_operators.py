#how to use base 2:
#the counting pattern is the same as base 10, except that we carry over whenever we hit 2

#example base 10:
    #0, 1, 2, 3, 4, 5
#example base 2:
    #0, 1, 10, 11, 100, 101

#note in the above we did the same thing as normal counting, except our "limit" was 2 per decimial place
#each decimal place in a binary number system represents a power of 2, or a bit!
#as such, the rightmost decimal is the 1's bit, then the 2's bit, then 4's bit, then 8's bit, etc.

#example: 1010 in binary
    #    1        0        1        0
    # 8's bit, 4's bit, 2's bit, 1's bit
    #   8^1       0       2^1       0
    #    8        +        2     =  10
    # 1010 = 10

#in the example above, we simple looked for bits that were on (not zero), and added the value for each

#another example: 11010
    #binary:        1   1   0   1   0
    #bit position: 16   8   4   2   1
    #calculation:  16 + 8 + 0 + 2 + 0 = 26
    # 11010 = 26

#in python, we can use binary by starting the number sequence with 0b
print 0b1,        #1
print 0b10,       #2
print 0b11,       #3
print 0b100,      #4
print 0b101,      #5
print 0b110,      #6
print 0b111       #7
print 0b1 + 0b11  #4 (1 + 3)
print 0b11 * 0b11 #9 (3 * 3)

#note that each increase in decimal length occurs at 2, 4, 8, 16, 32, 64, 128, etc.
one = 0b1
two = 0b10
three = 0b11
four = 0b100
five = 0b101
six = 0b110
seven = 0b111
eight = 0b1000
nine = 0b1001
ten = 0b1010
eleven = 0b1011
twelve = 0b1100
print twelve

#python has built in operators to help convert base10 into binary:
#note that the resulting value is a STRING! and therefore cannot by used in calcuation, unless converted
print bin(1) # 0b1
print bin(2) # 0b10
print bin(3) # 0b11
print bin(4) # 0b100
print bin(5) # 0b101

#another built in operator is int(), which we're already familiar with
#int() converts a non-integer into an integer
#however, turns out int() can contain a secondary argument, the base that the first argument is currenty in
print int("1",2)            # 1
print int("10",2)           # 2
print int("111",2)          # 7
print int("0b100",2)        # 4
print int(bin(5),2)         # 5 same as (int("0b101"), 2). Essentially going from base10 to base2, back to base 10
print int("0b11001001", 2)  # 201
#remember, int() requires a non-interger first argument, so we use a string. Or in example 5, we used bin(5), which again, returns a string

#shift operators essentially shift the bit sequence by a number of zeros left or right:
# Left Bit Shift (<<)
    # 0b000001 << 2 == 0b000100 (1 << 2 = 4)
    # 0b000101 << 3 == 0b101000 (5 << 3 = 40)

# Right Bit Shift (>>)
    # 0b0010100 >> 3 == 0b000010 (20 >> 3 = 2)
    # 0b0000010 >> 2 == 0b000000 (2 >> 2 = 0)

#left shift essentially adds x number of zeros
#right shift essentially removes x numbers (not just of )

#AND (&) operator compares two numbers at each bit level. If both are on, it returns 1 at that position
#example:
    #      number 1:   00101010   =42
    #      number 2:   00001111   =15
    # ===================
    #         1 & 2:   00001010   =10
print 0b101010 & 0b1010

#OR (|) operator is similar, but returns 1 if EITHER of the corresponding bits of the two numbers are on
#example:
    #     number 1:  00101010  =42
    #     number 2:  00001111  =15
    # ================
    #        1 | 2:  00101111  =47
print 0b00101010 | 0b00101111

#XOR (^) operator returns 1 if ONLY ONE of the corresponding bits are on. If both are on, it returns 0 for that position
    #     number 1:  00101010   =42
    #     number 2:  00001111   =15
    # ================
    #        1 ^ 2:  00100101   =37
print 0b00101010 ^ 0b00001111

#NOT (~) operator flips all of the bits in a single number
#this is complicated, but is equivalent to adding 1 to the number, then making it negative
print ~1    #-2
print ~2    #-3
print ~3    #-4
print ~42   #-43
print ~123  #-124

#a 'bit mask' is simply a variable we can define to check if a certain bit is on or off in a number
#example"
num  = 0b1100
mask = 0b0100
desired = num & mask
if desired > 0:
  print "Bit was on"
#in the above, we define mask as a simply binary number, with only a 1 at the position we'd like to check for in num
#if desired > 0, that means num has a 1 at the same position as the 1 in mask

#another example (as a function):
def check_bit4(input):
    mask = 0b1000
    desired = input & mask
    if desired > 0:
        return "on"
    else:
        return "off"

print check_bit4(0b110011) #off (the 4th bit is 0)
print check_bit4(0b001011) #on  (the 4th bit is 1)

#we can also use a mask with an OR operator to ensure a certain bit is turned on
#example:
a = 0b110 # 6
mask = 0b1 # 1
desired =  a | mask # 0b111, or 7
#in the above, since we used an OR operator, the 1st bit from the right was guaranteed to be 1, while the rest of the bits would remain unchanged

#another example:
a = 0b10111011
mask = 0b100
desired = bin(a | mask)
print desired   #0b10111111
#in the above, we wanted to make sure the 3rd bit from the right was on

#we can also use the mask with an XOR operator to essentially flip all of the bits
a =     0b110 # 6
mask =  0b111 # 7
desired =  a ^ mask # 0b1

#another example:
a = 	0b11101110
mask = 	0b11111111
	   #0b00010001 is the desired reverse
desired = a ^ mask
print bin(desired)
#in other words, just use a mask of 0b with x number of 1's

#one simply way to creating a lengthy mask is to use shift operators
#imagine I wanted to target the 10th bit in a number.. I could write 0b1000000000, or I could write 0b1 << 9 (note we use 9, not 10, since we already have 1 digit defined)
#example to turn on the 10th bit of a number:
a = 0b101
mask = (0b1 << 9)
desired = a ^ mask

#another example of flipping a specific bit:
def flip_bit(number, n):
  mask = (0b1 << (n-1))
  result = number ^ mask
  return bin(result)
print flip_bit(0b10100, 3) #0b10000
