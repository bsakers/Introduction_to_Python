#in javascript:
    #array.forEach((variable)=>{do something})

#in python:
    #for variable in array: do something

number_list = [2, 13, 7, 9, 15]
for number in number_list:
    print 2*number

blade_runner = ["all", "these", "moments", "will", "be", "lost", "in", "time.."]
for word in blade_runner:
    print word


start_list = [5, 3, 1, 2, 4]
square_list = []
for number in start_list:
  square_list.append(number**2)

square_list.sort()
print square_list

#for loops can be interupted with breaks. Note that eric is never called, and the final else is not executed
students = ["justin", "kevin", "han", "spicoli", "eric"]
print "Let\'s run through the roster of students, shall we?"
for student in students:
    if student == "spicoli":
        print "Spicoli? Where is Spicoli? Has anyone seen Spicoli?"
        break
    else:
        print student
else:
  print "Great, we're all here; let's get started"

#same as the above, but the spicoli isn't on the roster for this class
students = ["justin", "kevin", "han", "julie", "eric"]
print "Let\'s run through the roster of students, shall we?"
for student in students:
    if student == "spicoli":
        print "Spicoli? Where is Spicoli? Has anyone seen Spicoli? I refuse to start class until he arrives"
        break
    else:
        print student
else:
  print "Great, we're all here; let's get started"
