dota_heros = ["lifestealer", "juggernaut", "luna"]
print len(dota_heros)
print dota_heros[0]
print dota_heros[1]
print dota_heros[2]

#you can easily replace items in the list
dota_heros[0] = "kunka"
print dota_heros
dota_heros[-1]= "io"
print dota_heros

#you can add to the end of an array with .append
dota_heros.append("mirana")
dota_heros.append("the dark lord")
print dota_heros

#you can slice an array using [index: index]. Note the second is NOT included
first_hero = dota_heros[0:1]
print first_hero
first_two_heros = dota_heros[0:2]
print first_two_heros
second_and_third_heros = dota_heros[1:3]
print second_and_third_heros
last_three_heros = dota_heros[2: 5]
print last_three_heros
#you can slice using just the first or last index of interest:
first_three_heros = dota_heros[:4]
print first_three_heros
last_four_heros= dota_heros[1:]
print last_four_heros

#you can slice with strings too, of course
heros= "lunajugkunka"
luna = heros[:4]
print luna
jug= heros[4:7]
print jug
kunka= heros[7:]
print kunka

#we can insert into an array at any position we'd like. The first argument is the index; all items in the list will be moved back after
dota_heros.insert(2, "elder titan")
print dota_heros

#we can find the index of a specific item in the list:
print dota_heros.index("io")
