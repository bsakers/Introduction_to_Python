print "Welcome, to the real world, Neo"
def matrix():
    print "You take the blue pill, the story ends. You wake up in your bed and believe whatever you want to believe. You take the red pill, you stay in Wonderland, and I show you how deep the rabbit hole goes"
    answer = raw_input("Type blue or red").lower()
    if answer == "red":
        print "Let\'s see how deep the rabit hole goes"
    elif answer == "blue":
        print "You were never really the one"
    else:
        print "You didn't pick red or blue! Let's try again"
        matrix()

matrix()

#comparators:
    # ==  equal
    # !=  not equal
    # <   less than
    # <=  less than or equal to
    # >   greater than
    # >=  greater than or equal to
