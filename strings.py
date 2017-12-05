#Basic string
test_string = "Hello there"
print test_string

#Using an apostraphy breaks the string, so we use a \ to correct
string = "There\'s something on the wing"
print string

#each string character has an index
t= "tool"[0]
print t
s= "lebowsky"[5]
print s

#string length: returns an integer for number of characters in the string
computer = "computer"
print len(computer)

#string to lowercase
excited = "EXCITED".lower()
print excited

#string to uppercase
excited = "excited"
print excited.upper()

#turn variables into strings
pi = 3.14
print str(pi)

#dot notation only works on strings! Hence the above variance. For example:
candy = "sour patch"
print candy.upper()
     # print 234.upper() will not work
print len(str(234))

#string concatenation
print "Life " + "of " + "Brian"
print str(46) + " and " + str(2) +" are just ahead of me"
  #better method:
var_one= "moments"
var_two= "time"
var_three= "rain"
print "All those %s will be lost in %s, like tears in the %s" %(var_one, var_two, var_three)

#check a string for non-letter characters
x = "j123"
print x.isalpha()
    #the above will return false, because it contains non-letters, but the below will return true
y = "somethingdifferent"
print y.isalpha()
