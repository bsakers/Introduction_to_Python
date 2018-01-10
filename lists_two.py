#looping througn a dictionary
#note: looping through dictionaries appears to be random
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
    'Sloth' : 'Rainforest Exhibit',
    'Bengal Tiger' : 'Jungle House',
    'Atlantic Puffin' : 'Arctic Exhibit',
    'Rockhopper Penguin' : 'Arctic Exhibit'}
print zoo_animals

#print just the animal name (the key)
for animal in zoo_animals:
    print animal

#print just the description (the value)
for animal in zoo_animals:
    print zoo_animals[animal]

#using a conditional inside a for loop
def fizz_count(x):
  count = 0
  for item in x:
    if item == 'fizz':
      count += 1
  return count

print fizz_count(["fizz","cat","fizz"])

#looping through a string in the same way you do an array
word = "billionsandbillions"
for letter in word:
    print letter

#food_cart
prices = {
  "rice" : 4,
  "chicken"  : 2,
  "gyro" : 1.5,
  "sandwhich"   : 3,
}
stock = {
  "rice" : 6,
  "chicken"  : 0,
  "gyro" : 32,
  "sandwhich"   : 15,
}

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  print

total = 0
for item in prices:
  total += prices[item]*stock[item]
print total

def compute_cost(food):
  total = 0
  for item in food:
    if stock[item] > 0:
      total += prices[item]
      stock[item] -= 1
  return total

print compute_cost(["rice", "gyro"])
print stock["gyro"]
