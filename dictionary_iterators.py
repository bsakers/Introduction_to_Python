my_dict= {
  "Name": "Luna",
  "Role": "Carry",
  "Position": 1
}

print my_dict.items()
print my_dict.keys()
print my_dict.values()
#the above methods return tuples, which are essentially immutable (unchangable) lists
#also note that while the order of the items may appear random, they are not. They will return the same order each time

for key in my_dict:
    print key, my_dict[key]

#print each value, no keys, all on the same line:
for key in my_dict:
    print my_dict[key],
