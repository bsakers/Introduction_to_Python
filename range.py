#range function is used for generating lists

    #the below will give [0, 1, 2, 3, 4, 5]
    #this is really saying range(stop), or "return a list up to, but not including the stop index"
print range(6)

    #the below will give [1, 2, 3, 4, 5]
    #this is really saying range(start, stop)
print range(1, 6)

    #the below will give [1, 5]
    #this is really saying range(start, stop, step). Step means the degree of increment between each item in the list
print range(1, 6, 4)

    #another example. The below will give [0, 2, 4, 6, 8]
    #this is really saying give me a list of index 0 through (but not including) 10, incremented by 2
print range(0, 10, 2)
    #will give [0, 2, 4, 6, 8, 10]
print range(0, 11, 2)

#start will always default to 0, and step will default to 1
