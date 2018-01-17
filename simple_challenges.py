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
