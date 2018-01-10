#hashes are referred to as dictionaries

example_hash = {'key1' : 1, 'key2' : 2, 'key3' : 3}
print example_hash["key1"]
print example_hash["key2"]
print example_hash["key3"]

#dictionaries are mutable, meaning they can be changed (mutated) after being created. Here is adding to it
food_cart = {}
food_cart["chicken and rice"]= 5.50
food_cart["gyro"]=6.00
food_cart["cheesesteak"]= 7.00
print food_cart
menu_count= len(food_cart)
print "There are " + str(menu_count) + " items to choose from at the food cart"

#we can delete from a dictionary as well by 'del dictionary[key]'
zoo_animals = { 'Unicorn' : 'Cotton Candy House',
'Sloth' : 'Rainforest Exhibit',
'Bengal Tiger' : 'Jungle House',
'Atlantic Puffin' : 'Arctic Exhibit',
'Rockhopper Penguin' : 'Arctic Exhibit'}
del zoo_animals["Sloth"]
del zoo_animals["Bengal Tiger"]

#similar to an array, we can overwrite a key-value pair through 'dictionary['key']= new_value'
zoo_animals["Unicorn"] = "On Top of a Mountain"
print zoo_animals

#arrays and hashes can exist within one another, as expected
my_dictionary= {
    "dota_heros": ["luna", "axe", "juggernaut"],
    "money": 2484,
    "day": "Friday"
}
 #to find "juggernaut"
print my_dictionary["dota_heros"][2]
 #to find 'friday'
print my_dictionary["day"]
 #to find f in Friday
print my_dictionary["day"][0]
 #to add 50 to money
my_dictionary['money']+= 50
 #to remove axe
my_dictionary['dota_heros'].remove('axe')
