my_array = [i ** 2 for i in range(1, 11)]
    #an array of squares for 1- 10

my_file = open("test_output.txt", "w")
    # we must open the file and specify what we'd like to do with it
    # 'r'	open for reading (default)
    # 'w'	open for writing, truncating the file first
    # 'x'	open for exclusive creation, failing if the file already exists
    # 'a'	open for writing, appending to the end of the file if it exists
    # 'b'	binary mode
    # 't'	text mode (default)
    # '+'	open a disk file for updating (reading and writing)
    # 'U'	universal newlines mode (deprecated)
    #most likely to use r, w, and +, or just a


for item in my_array:
    my_file.write(str(item) + "\n")
    #note that each item must be converted to a string for the write function to work
    #the '\n' simply ensures each item is added to a new line

my_file.close()
    #must close the file when complete!


#if we want to just read the file, we open it, read it, then close it
my_file = open("test_output.txt", "r")
print my_file.read()
my_file.close()


#python also has a built-in function to read just one line at a time
my_file = open('test_text.txt', 'r')
print my_file.readline()
    #this will read the first line
print my_file.readline()
    #this will read the second line
print my_file.readline()
    #this will read the third line, and so on
print my_file.readline()
print my_file.readline()
my_file.close()


#file objects contain a special set of functions. Two of which are __enter__() and __exit__()
#these functions are automatically invoked if we use the following syntax:
    # with open("file", "mode") as variable:
    # in the above, variable is the file_name

#example:
with open("test_output.txt", "w") as my_file:
    my_file.write("9 Planets; Children can count to nine on two hands..")
#note that in the above we did not need to close the file

#we can check if our file objects are open or closed:
f = open("test_text.txt")
print f.closed
# will return False
f.close()
print f.closed
# will return True
#as you can see, 'close()' is a function, whereas 'closed' is simply an attribute that we can read

#because of the above, we can set up a simply statement to ensure our files are closed:
if my_file.closed == False:
    my_file.close()

print my_file.closed
    #will return True
