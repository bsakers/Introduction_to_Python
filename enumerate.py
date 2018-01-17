#enumerate supplies a corresponding index as we loop
options = ["pizza", "sushi", "gyro"]
    #normal for loop:
for option in options:
    print option

    #enumerator (note that "index" could be replaced by anything; it's just a placeholder)
for index, option in enumerate(options):
    print index, option

#we can even alter the index count if needed (example, for a list to not start at 1)
for index, option in enumerate(options):
    print index +1, option
