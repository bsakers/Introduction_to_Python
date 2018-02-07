#general sytax for a class:
class NewClassName(object):
    # code
    pass

#in the above, we simply state the keyword 'class' and whatever we want to name it
#then we state what the class will inherit from (here we inherit from python's object)
#the 'pass' keyword doesnt do anything, but can act as a placeholder to not break our placeholder

#similar to ruby, each class requires an initialize function to actually create class objects
class Hero(object):
    def __init__(self, name, role):
        self.name = name
        self.role = role
    is_from_dota2 = True
    def description(self):
        print self.name
        print self.role


#in the above, the initialize function follows the syntax '__init__(x, y, z)'
#the first argument is almost always 'self', which just refers to that specific object being created
    #technically, you dont have to use 'self', as the first argument will always refer to calling upon that specific object, but this is common practice
#under initialize we define each of the subsequent arguments passed in
    #this is very similar to ruby, where we used @name = name

#since we've made a class, we can now instantiate objects:
jugg = Hero("Juggernaut", "carry")
print jugg.name, jugg.role

#scope
    # global variables/functions, variables that are available everywhere
    # member variables/functions, variables that are only available to members of a certain class
    # instance variables/functions, variables that are only available to particular instances of a class
#in our hero class, we created a member variable, is_from_dota2, meaning all objects of that class have access (and will return the same)
print jugg.is_from_dota2
    #no matter how many heros I create, they will all have true for is_from_dota2

#we also created a member function, description, which also required a self statement
jugg.description()
    #note in the above, I can call .description() on ANY of my class objects since it's a member function
