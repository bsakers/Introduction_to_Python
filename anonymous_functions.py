#functional programming means that you're allowed to pass functions around just as if they were variables or values.
#an anonymous function is a function that we simply do no define

#a named function:
def by_three(x):
    return x % 3 == 0

#an anonymous function, that does the same thing:
lambda x: x % 3 == 0

#we can then use the anonymous function with 'filter':
my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)
    #the above filters for lambda based on the second argument, my_list
    #filter is similar to JS, in that it runs the function, and if true, the value is added to the list
    #if you plan on using the code over and over, you might as well just definte a function though

#another example
languages = ["HTML", "JavaScript", "Python", "Ruby"]
print filter(lambda x: x == "Python", languages)
    #the above will return ["Python"]
    #so it essentially filtered through the array, returning all that met the conditional

squares = [x**2 for x in range(1, 11)]
print filter(lambda x: 30 <= x <= 70, squares)
    #[36, 49, 64]

#remember, this is like using a function. Therefore, we can use more than arrays!
garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
message = filter(lambda x: x != "X", garbled)
print message
    #[I am another secret message!]
