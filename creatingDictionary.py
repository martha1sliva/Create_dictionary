python_words = {"string": "a sequence of characters",\
                "int": "a whole number (integer)"}

key = raw_input("Please enter a key or enter 'stop': ").lower()

while True:
    ##searches for key in existing dictionary
    if key in python_words:
        print python_words[key]
        ##prints definition
        key = raw_input("Please enter a key or enter 'stop': ").lower()
    elif key == "stop":
        break
    ##asks for definition of new word and adds word/def into dictionary
    else:
        print "Not Found"
        definition = raw_input("Please enter the definition: ")
        python_words[key] = definition
        ##adds new key and definition to the dictionary
        print definition
        key = raw_input("Please enter a key or enter 'stop': ").lower()

print "Your dictionary:", python_words
##dictionary alphabetizes the list of definitions
