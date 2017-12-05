print 'Welcome to the Pig Latin Translator!'

original_word = raw_input("Enter a word you would like translated: ").lower()
ending = "ay"

if len(original_word) > 0 and original_word.isalpha():
    translated_word = original_word[1:len(original_word)] + original_word[0] + ending
    print translated_word
else:
    print "Your imput is either empty or contains a non-letter"
