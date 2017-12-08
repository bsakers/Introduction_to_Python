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
