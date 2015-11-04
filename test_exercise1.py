
VOWELS = ("a", "e", "i", "o", "u", "A", "E", "I", "O", "U")
statement = raw_input("Please enter a word: ")
words =  statement.split()
for word in words:
    if word[0] in VOWELS:
        print word + "ay",
    else:
        print word[1:] + word[0] + "ay",