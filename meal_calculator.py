#let's calculate the cost of a meal with tip and tax

meal = 42.84
tax = 6.75/100
tip = 15.0/100

total = meal + meal*tax + meal*tip
print total

#to round, we use the following (which was found online), and we added a dollar sign
print("$%.2f" % total)
