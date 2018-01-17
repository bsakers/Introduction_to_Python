#functions similar to ruby
count = 0
while count <= 10:
    print "The count is", count
    count += 1

#using true/false for loop condition. Note the below will only run once
condition = True
while condition:
    print "The condition is true!"
    condition = False

#managing user input
user_input = raw_input('Red or blue pill? (r/b)').lower()
while user_input != "r" and user_input != "b":
    user_input = raw_input('Sorry, that\'s not an option: Red or blue pill? (r/b)').lower()

#break can exit any loop (not just while)
count = 0
while True:
    print count
    count +=1
    if count >=5:
        break

#else statements work with while loops. The else will execute if the loop condition is not met, BUT WILL NOT if a break is hit
from random import randint
print "You have 3 chances to roll a 6"
count = 0
while count < 3:
    num = randint(1, 6)
    print num
    if num == 6:
        print "You Win!"
        break
    count += 1
else:
    print "Sorry, you didn't roll a 6, you lose"

#similar to the above, but with guessing
random_number = randint(1, 10)
print "You have three chances to guess the random number"
guesses_left = 3
while guesses_left >0:
  guess = int(raw_input("Your guess:"))
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."
